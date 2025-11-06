import mysql.connector
from mysql.connector import Error

try:
    # 1️⃣ CONNECT TO MYSQL SERVER (without specifying a database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # Replace with the password you set during MySQL installation
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server successfully.")

        # 2️⃣ CREATE DATABASE
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
        print("📦 Database 'school_db' created (or already exists).")

        # Switch connection to use the new database
        connection.database = "school_db"

        # 3️⃣ CREATE TABLE
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("🧱 Table 'students' created (or already exists).")

        # 4️⃣ INSERT DATA
        insert_query = "INSERT INTO students (first_name, last_name, age) VALUES (%s, %s, %s)"
        students = [
            ("John", "Doe", 22),
            ("Alice", "Smith", 20),
            ("Michael", "Brown", 23)
        ]
        cursor.executemany(insert_query, students)
        connection.commit()
        print(f"✅ {cursor.rowcount} records inserted successfully into 'students' table.")

        # 5️⃣ SELECT DATA
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        print("\n📋 Data from 'students' table:")
        for row in rows:
            print(row)

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    # 6️⃣ CLOSE CONNECTION
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\n🔒 MySQL connection closed.")
