import sqlite3

conn = sqlite3.Connection("mydb.sqlite")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

cursor.execute("INSERT INTO customers (name,city) VALUES ('Anmol', 'Delhi')")
cursor.execute("INSERT INTO customers (name,city) VALUES ('Riya', 'Mumbai')")
cursor.execute("INSERT INTO customers (name,city) VALUES ('Aman', 'Bangalore')")

cursor.execute("INSERT INTO orders (customer_id,amount) VALUES (1, 800)")
cursor.execute("INSERT INTO orders (customer_id,amount) VALUES (1, 1200)")
cursor.execute("INSERT INTO orders (customer_id,amount) VALUES (2, 4400)")
cursor.execute("INSERT INTO orders (customer_id,amount) VALUES (3, 2345)")

conn.commit()
conn.close()

print("Database seeded successfully")
