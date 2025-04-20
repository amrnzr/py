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


"""
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name::TEXT, p.phone::TEXT
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
"""
# SELECT * FROM search_pattern('Mes');

def search_pattern():
    pattern = input("Enter part of name or phone: ")
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

"""
CREATE OR REPLACE PROCEDURE insert_or_update(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = ph_name) THEN
        UPDATE phonebook SET phone = ph_phone WHERE name = ph_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (ph_name, ph_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
"""
# CALL insert_or_update('Green', '654321');

def from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("CALL insert_or_update(%s, %s)", (row[0], row[1]))
    conn.commit()

def from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update(%s, %s)", (name, phone))
    conn.commit()

"""
CREATE OR REPLACE PROCEDURE insert_many(ph_names TEXT[], ph_phones TEXT[], OUT invalid TEXT[])
AS $$
DECLARE
    i INT := 1;
    current_name TEXT;
    current_phone TEXT;
    incorrect TEXT[] := '{}';
BEGIN
    WHILE i <= array_length(ph_names, 1) LOOP
        current_name := ph_names[i];
        current_phone := ph_phones[i];

        IF current_name ~ '^[A-Za-z]+$' AND current_phone ~ '^[0-9+]+$' THEN
            CALL insert_or_update(current_name, current_phone);
        ELSE
            incorrect := array_append(incorrect, current_name || ' (' || current_phone || ')');
        END IF;

        i := i + 1;
    END LOOP;
    invalid := incorrect;
END;
$$ LANGUAGE plpgsql;
"""
# CALL insert_many(ARRAY['Leha', 'Ali', '12345'], ARRAY['345890', 'phone number', '33333'], NULL);

def insert_many():
    names = []
    phones = []
    nothing = []
    n = int(input("How many contacts do you want to add? "))
    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)
    cur.execute("CALL insert_many(%s, %s, %s)", (names, phones, nothing))
    conn.commit()

"""
CREATE OR REPLACE FUNCTION paginated_contacts(ph_limit INT, ph_offset INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name::TEXT, p.phone::TEXT
    FROM phonebook p
    ORDER BY p.id
    LIMIT ph_limit OFFSET ph_offset;
END;
$$ LANGUAGE plpgsql;
"""
# SELECT * FROM paginated_contacts(5, 0);

def paginated_query():
    limit = int(input("How many contacts to show? "))
    offset = int(input("From which row? "))
    cur.execute("SELECT * FROM paginated_contacts(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)

"""
CREATE OR REPLACE PROCEDURE delete_contact(ph_name TEXT DEFAULT NULL, ph_phone TEXT DEFAULT NULL)
AS $$
BEGIN
    IF ph_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = ph_name;
    END IF;
    IF ph_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = ph_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
"""
# CALL delete_contact('12345', NULL);
# CALL delete_contact(NULL, '123');
# CALL delete_contact('Ali', '123');

def delete_contact():
    name = input("Name to delete (press Enter to skip): ")
    phone = input("Phone to delete (press Enter to skip): ")
    cur.execute("CALL delete_contact(%s, %s)", (name or None, phone or None))
    conn.commit()


if __name__ == "__main__":
    create_table()

    while True:
        print("\nPhoneBook Menu:")
        print("1 — Search contacts by pattern")
        print("2 — Add or update contact from console")
        print("3 — Add or update contacts from CSV")
        print("4 — Insert multiple contacts manually")
        print("5 — View contacts (pagination)")
        print("6 — Delete contact")
        print("7 — Exit")

        choice = input("Choose an option (1–8): ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            from_console()
        elif choice == "3":
            path = "contacts.csv"
            from_csv(path)
        elif choice == "4":
            insert_many()
        elif choice == "5":
            paginated_query()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Invalid option")

    cur.close()
    conn.close()