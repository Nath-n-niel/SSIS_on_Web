from flask import Blueprint, request, redirect, url_for, render_template
import mysql.connector

add_student = Blueprint("add_student", __name__, static_folder = "static", template_folder = None)

db = mysql.connector.connect(
    host="localhost",
    user="root",  # replace with your MySQL username
    password="hostpassword",  # replace with your MySQL password
    database="webssis"  # replace with your database name
)

@add_student.route("/add_student", methods=["POST"])
def add_student():
    student_id = request.form['student_id']
    Name = request.form['Name']
    year_level = request.form['year_level']
    gender = request.form['gender']
    course = request.form['course']
    college = request.form['college']

    # Insert into the database
    cursor = db.cursor()
    insert_query = """
    INSERT INTO students (student_id, Name, year_level, gender, course, college)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (student_id, Name, year_level, gender, course, college)
    
    try:
        cursor.execute(insert_query, values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

    return redirect(url_for("student"))