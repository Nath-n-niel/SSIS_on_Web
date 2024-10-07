from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",  # replace with your MySQL username
    password="hostpassword",  # replace with your MySQL password
    database="webssis"  # replace with your database name
)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/student", methods = ["POST" , "GET"])
def student():
	cursor = db.cursor(dictionary=True)
	cursor.execute("SELECT * FROM students")  
	students = cursor.fetchall() 

	# Fetch distinct courses and colleges from the database
	cursor.execute("SELECT DISTINCT courseCode FROM courses")
	courses = cursor.fetchall()

	cursor.execute("SELECT DISTINCT collegeCode FROM colleges")
	colleges = cursor.fetchall()

	return render_template("student.html", students=students, courses=[c['courseCode'] for c in courses], colleges=[c['collegeCode'] for c in colleges])
	
@app.route("/course", methods = ["POST" , "GET"])
def course():
	cursor = db.cursor(dictionary=True)
	cursor.execute("SELECT * FROM courses")  
	courses = cursor.fetchall()

	return render_template("course.html", courses=courses)

@app.route("/college", methods = ["POST" , "GET"])
def college():
	cursor = db.cursor(dictionary=True)
	cursor.execute("SELECT * FROM colleges")  
	colleges = cursor.fetchall()

	return render_template("college.html", colleges=colleges)


# Add student
@app.route("/student/add_student", methods=["POST"])
def add_student():
    studentID = request.form['studentID']
    Name = request.form['Name']
    YearLevel = request.form['year_level']
    Gender = request.form['gender']
    Course = request.form['course']
    College = request.form['college']

    # Insert into the database
    cursor = db.cursor()
    insert_query = """
    INSERT INTO students (studentID, Name, YearLevel, Gender, Course, College)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (studentID, Name, YearLevel, Gender, Course, College)
    
    try:
        cursor.execute(insert_query, values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

    return redirect(url_for("student"))


# Delete student
@app.route("/delete_student/<studentID>", methods=["POST"])
def delete_student(studentID):
    cursor = db.cursor()
    delete_query = "DELETE FROM students WHERE studentID = %s"
    
    try:
        cursor.execute(delete_query, (studentID,))
        db.commit()
        return redirect(url_for('student'))  # Redirect back to the student list page
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
        return "Error deleting student", 500

# Edit Student
@app.route("/student/edit_student/<studentID>", methods=["GET", "POST"])
def edit_student(studentID):
    cursor = db.cursor(dictionary=True)
    
    if request.method == "POST":
        # Get updated data from the form
        Name = request.form['Name']
        YearLevel = request.form['year_level']
        Gender = request.form['gender']
        Course = request.form['course']
        College = request.form['college']
        
        # Update the student's data in the database
        update_query = """
            UPDATE students
            SET Name = %s, YearLevel = %s, Gender = %s, Course = %s, College = %s
            WHERE studentID = %s
        """
        
        try:
            cursor.execute(update_query, (studentID, Name, YearLevel, Gender, Course, College))
            db.commit()
            return redirect(url_for('student'))  # Redirect back to the student list
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback()
            return "Error updating student", 500
    
    # For GET request, fetch the student data to pre-fill the form
    cursor.execute("SELECT * FROM students WHERE studentID = %s", (studentID,))
    students = cursor.fetchone()
    
    return render_template("edit_student.html", students=students)


if __name__ == "__main__":
	app.run(debug=True)


