import psycopg2
import csv
 
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="1488228"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()

def from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

def from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

def update(old_name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))
    conn.commit()

def search(filter_name=""):
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + filter_name + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone =%s", (phone,))
    conn.commit()

if __name__ == "__main__":
    create_table()

    while True:
        print("PhoneBook Menu:")
        print("1 — Add contact from console")
        print("2 — Add contacts from CSV")
        print("3 — Update contact")
        print("4 — Search contacts")
        print("5 — Delete contact")
        print("6 — Exit")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            from_console()

        elif choice == "2":
            file_path = "contacts.csv"
            from_csv(file_path)

        elif choice == "3":
            old_name = input("Old name: ")
            new_name = input("New name (press enter for number): ")
            new_phone = input("New phone number (press enter to exit): ")
            update(old_name, new_name or None, new_phone or None)

        elif choice == "4":
            query = input("Name to search: ")
            search(query)

        elif choice == "5":
            name = input("Name to delete (press enter for number): ")
            phone = input("Phone number to delete (press enter to exit): ")
            delete(name=name or None, phone=phone or None)

        elif choice == "6":
            print("Exit")
            break

        else:
            print("Invalid option")

    cur.close()
    conn.close()