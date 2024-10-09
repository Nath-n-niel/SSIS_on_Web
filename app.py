from flask import Flask, redirect, url_for, render_template, request, flash
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",  # replace with your MySQL username
    password="hostpassword",  # replace with your MySQL password
    database="webssis"  # replace with your database name
)
cursor = db.cursor()

@app.route("/")
def home():
	return render_template("base.html")

# Student Main
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


# Course Main
@app.route("/course", methods = ["POST" , "GET"])
def course():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")  
    courses = cursor.fetchall()
    
    # Fetch distinct colleges from the database
    cursor.execute("SELECT DISTINCT collegeCode FROM colleges")
    colleges = cursor.fetchall()
    
    return render_template("course.html", courses=courses, colleges=[c['collegeCode'] for c in colleges])

# College Main
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
@app.route("/student/delete_student/<studentID>", methods=["POST"])
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
    

#Edit Student
@app.route('/student/edit_student', methods=['POST'])
def edit_student():
    # Get the data from the form
    if request.method == "POST":
        studentID = request.form["studentID"]
        name = request.form["name"]
        year_level = request.form["YearLevel"]
        gender = request.form["gender"]
        course = request.form["course"]
        college = request.form["college"]
        
        cursor = db.cursor()

        query = """
        UPDATE students 
        SET Name = %s, YearLevel = %s, Gender = %s, Course = %s, College = %s
        WHERE studentID = %s
        """
        
        cursor.execute(query, (name, year_level, gender, course, college, studentID))
        db.commit()
        cursor.close()

        return redirect(url_for("student"))
    

# Add Course
@app.route("/course/add_course", methods=["POST"])
def add_course():
    courseCode = request.form['courseCode']
    courseName = request.form['courseName']
    collegeCode = request.form['college']

    # Insert into the database
    cursor = db.cursor()
    insert_query = """
    INSERT INTO courses (courseName, collegeCode, courseCode)
    VALUES (%s, %s, %s)
    """
    values = (courseName, collegeCode, courseCode)
    
    try:
        cursor.execute(insert_query, values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

    return redirect(url_for("course"))

# Delete Course
@app.route("/course/delete_course/<courseCode>", methods=["POST"])
def delete_course(courseCode):
    cursor = db.cursor()
    delete_query = "DELETE FROM courses WHERE courseCode = %s"
    
    try:
        cursor.execute(delete_query, (courseCode,))
        db.commit()
        return redirect(url_for('course'))  # Redirect back to the student list page
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
        return "Error deleting course", 500
    

# Edit Course
@app.route('/course/edit_course', methods=['POST'])
def edit_course():
    # Retrieve the form data from the modal
    courseCode = request.form['courseCode']
    courseName = request.form['courseName']
    college = request.form['college']

    # SQL query to update the course
    cursor = db.cursor()
    query = """
        UPDATE courses 
        SET courseName = %s, collegeCode = %s
        WHERE courseCode = %s
    """
    cursor.execute(query, (courseName, college, courseCode))
    db.commit()
    cursor.close()

    # After updating, redirect to the courses page
    return redirect(url_for('course'))
    

# Add College
@app.route("/college/add_college", methods=["POST"])
def add_college():
    collegeName = request.form['collegeName']
    collegeCode = request.form['collegeCode']


    # Insert into the database
    cursor = db.cursor()
    insert_query = """
    INSERT INTO colleges (collegeName, collegeCode)
    VALUES (%s, %s)
    """
    values = (collegeName, collegeCode)
    
    try:
        cursor.execute(insert_query, values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

    return redirect(url_for("college"))


# Delete College
@app.route("/college/delete_college/<collegeCode>", methods=["POST"])
def delete_college(collegeCode):
    cursor = db.cursor()
    delete_query = "DELETE FROM colleges WHERE collegeCode = %s"
    
    try:
        cursor.execute(delete_query, (collegeCode,))
        db.commit()
        return redirect(url_for('college'))  # Redirect back to the college list page
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
        return "Error deleting course", 500

@app.route('/college/edit_college', methods=['POST'])
def edit_college():
    # Retrieve the form data from the modal
    college_name = request.form['collegeName']
    college_code = request.form['collegeCode']  # This is a hidden field and not editable

    # SQL query to update the college
    cursor = db.cursor()
    query = """
        UPDATE colleges
        SET collegeName = %s
        WHERE collegeCode = %s
    """
    cursor.execute(query, (college_name, college_code))
    db.commit()
    cursor.close()

    # After updating, redirect to the colleges page
    return redirect(url_for('college'))

if __name__ == "__main__":
	app.run(debug=True)


