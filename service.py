import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_form",
        auth_plugin='mysql_native_password'  # Set the authentication plugin
    )
    return connection


def data_insert(Name, Class, Section, Subject, Grade):
    connection = create_connection()  # Fix: Call the function to create a connection
    cursor = connection.cursor()
    query = "INSERT INTO student_details (Name, Class, Section, Subject, Grade) VALUES (%s, %s, %s, %s, %s)"
    data = (Name, Class, Section, Subject, Grade)
    cursor.execute(query, data)
    connection.commit()
    connection.close()


def retrieve_data():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM student_details"
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data
