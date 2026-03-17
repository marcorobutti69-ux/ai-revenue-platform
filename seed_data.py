from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM users")

cursor.executemany("""
INSERT INTO users (username, password, hotel)
VALUES (?, ?, ?)
""", [
    ("admin", "admin123", "Hotel Milano"),
    ("manager", "manager123", "Hotel Roma")
])

cursor.execute("DELETE FROM bookings")

data = [
("2025-01-01", 45, "Hotel Milano"),
("2025-01-02", 60, "Hotel Milano"),
("2025-01-03", 70, "Hotel Milano"),
("2025-01-04", 80, "Hotel Milano")
]

cursor.executemany("""
INSERT INTO bookings (date, rooms_sold, hotel)
VALUES (?, ?, ?)
""", data)

conn.commit()
conn.close()

print("Database popolato")
