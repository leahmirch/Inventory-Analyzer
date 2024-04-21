# Inventory Analyzer

Inventory Analyzer is a Flask-based web application developed to help organizations manage software inventories with features to add, view, export, and delete software entries.

## System Requirements

- Python 3.x
- Flask
- SQLite3

## Installation and Setup

### Prerequisites

Ensure Python is installed on your system. If not, download it from:

- For macOS: [Python for macOS](https://www.python.org/downloads/mac-osx/)
- For Windows: [Python for Windows](https://www.python.org/downloads/windows/)


### macOS Setup and Execution

1. **Check Python Installation:**
   ```
   make check
   ```
   This command checks for the Python installation, specifically looking for `python3`.

2. **Setup and Run the Application:**
   ```
   make mac
   paste http://127.0.0.1:5000 into a browser
   ```
   This command sequence does the following:
   - `cleanmac`: Removes any existing virtual environments and temporary files to ensure a clean state.
   - `check-python`: Verifies the presence of Python and instructs on installation if missing.
   - `setupmac`: Creates and activates a new Python virtual environment, then installs Flask.
   - `runmac`: Launches the Flask application.
 

### Windows Setup and Execution

1. **Check Python Installation:**
   ```
   make check
   ```
   This command ensures that Python is available on the system, checking for the `python` executable as it's typically installed on Windows.

2. **Setup and Run the Application:**
   ```
   make windows
   paste http://127.0.0.1:5000 into a browser
   ```
   The steps involved are:
   - `cleanwindows`: Cleans up any pre-existing virtual environments and temporary files.
   - `check-python`: Checks for and guides on installing Python if it's not found.
   - `setupwindows`: Sets up a virtual environment, activates it, and installs Flask.
   - `runwindows`: Executes the Flask server.

### Manual Setup (Alternative to Makefile)

If you choose to set up the environment manually or encounter issues with the Makefile, follow these instructions:

1. **Create and Activate a Virtual Environment:**
   - macOS:
     ```
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - Windows:
     ```
     python -m venv myenv
     myenv\Scripts\activate
     ```

2. **Install Dependencies:**
   ```
   pip install Flask
   ```

3. **Run the Application:**
   - macOS:
     ```
     python3 backend.py
     ```
   - Windows:
     ```
     python backend.py
     ```

4. **See the UI:**
   ```
   paste http://127.0.0.1:5000 into a browser
   ```

## Application Structure and Functionality

- **backend.py**: Main Flask application file. Handles routing and database operations for adding, viewing, exporting, and deleting software entries.
- **schema.sql**: Contains SQL schema for creating the software table in the SQLite database.
- **styles.css**: Provides styling for the HTML templates to ensure a consistent and clean user interface.
- **HTML Templates**: Each represents a different view within the application:
  - **add_software.html**: Form for adding new software entries.
  - **help.html**: Help page with frequently asked questions and contact information.
  - **home.html**: Landing page that provides an overview of the application features.
  - **view_inventory.html**: Displays the inventory of software and includes functionalities to search, view, and delete entries.

## Credits

Developed by Leah Mirch. For further information or support, please contact Leah via email at lmirch@umich.edu.
