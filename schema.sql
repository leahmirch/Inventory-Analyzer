DROP TABLE IF EXISTS software;
CREATE TABLE software (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    license TEXT NOT NULL,
    usage INTEGER NOT NULL,
    notes TEXT
);