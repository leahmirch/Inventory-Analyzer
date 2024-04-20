import sqlite3
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')
DATABASE = 'inventory.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_software():
    if request.method == 'POST':
        db = get_db()
        db.execute('''INSERT INTO software (name, version, license, usage, notes)
                      VALUES (?, ?, ?, ?, ?)''',
                   [request.form['name'], request.form['version'], request.form['license'], 
                    request.form['usage'], request.form['notes']])
        db.commit()
        return redirect(url_for('view_inventory'))
    return render_template('add_software.html')

@app.route('/inventory', methods=['GET', 'POST'])
def view_inventory():
    db = get_db()
    query = "SELECT * FROM software"
    if request.method == 'POST':
        search_query = '%' + request.form['search'] + '%'
        query += " WHERE name LIKE ?"
        cur = db.execute(query, [search_query])
    else:
        cur = db.execute(query)
    inventory = cur.fetchall()
    return render_template('view_inventory.html', inventory=inventory)

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM software WHERE id = ?', [id])
    db.commit()
    return redirect(url_for('view_inventory'))

from datetime import datetime
import os

@app.route('/export')
def export_inventory():
    try:
        export_dir = os.path.join(os.getcwd(), 'exports')
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'inventory_{timestamp}.csv'
        file_path = os.path.join(export_dir, filename)

        db = get_db()
        cur = db.execute('SELECT * FROM software')
        inventory = cur.fetchall()
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Version', 'License', 'Usage', 'Notes'])
            for item in inventory:
                writer.writerow([item['id'], item['name'], item['version'], item['license'], item['usage'], item['notes']])
        
        return jsonify({'message': 'Export successful!', 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
