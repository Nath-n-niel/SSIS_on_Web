from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint, current_app, make_response

from cloudinary import CloudinaryImage
from cloudinary.uploader import upload

from app.Models import Student
from app.Models import College
from app.Models import Course

from app.Forms import AddStudent

studentbp = Blueprint('student',__name__)


@studentbp.route("/student")
def student():
    students = Student.get_students()

    # Pagination logic
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_students = len(students)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_students = students[start:end]

    # College and course fetching
    colleges = College.get_collegeCode()
    courses = Course.get_courseCode()
    form = AddStudent()

    # Extract course and college codes for validation
    existing_courses = {course['courseCode'] for course in courses}
    existing_colleges = {college['collegeCode'] for college in colleges}

    # Update enrollment status
    for student in paginated_students:
        course_exists = student['Course'] in existing_courses
        college_exists = student['College'] in existing_colleges

        if course_exists and college_exists:
            enrollment_status = "Enrolled"
        elif not course_exists and not college_exists:
            enrollment_status = "Not Enrolled"
        elif not course_exists:
            enrollment_status = "No course"
        elif not college_exists:
            enrollment_status = "No college"

        if student['EnrollmentStatus'] != enrollment_status:
            Student.update_enrollment_status(student['studentID'], enrollment_status)

    # Update form choices
    form.Course.choices = [(course['courseCode'], course['courseCode']) for course in courses]
    form.College.choices = [(college['collegeCode'], college['collegeCode']) for college in colleges]

    # Render template with pagination variables
    return render_template(
        'student.html', 
        students=paginated_students, 
        colleges=colleges, 
        courses=courses, 
        form=form, 
        page=page, 
        total_students=total_students,
        per_page=per_page
    )

@studentbp.route("/student/add_student", methods=['GET', 'POST'])
def add_student():
    studentID = request.form['studentID']
    Name = request.form['Name']
    YearLevel = request.form['year_level']
    Gender = request.form['gender']
    Course = request.form['course']
    College = request.form['college']

    # Check if a file is part of the request
    photo_url = None
    if 'profile_picture' in request.files:
        profile_picture = request.files['profile_picture']
        if profile_picture.filename != '':
            try:
                # Upload the image to Cloudinary
                upload_result = upload(profile_picture)
                photo_url = upload_result['url']
            except Exception as e:
                print(f"Error uploading to Cloudinary: {e}")

    Student.add_student(studentID, Name, YearLevel, Gender, Course, College, photo_url)
    flash("Student added successfully")
    return redirect(url_for('student.student'))

@studentbp.route("/student/delete_student/<studentID>", methods=['GET', 'POST'])
def delete_student(studentID):

    Student.delete_student(studentID)
    flash("Student deleted successfully")
    return redirect(url_for('student'))

@studentbp.route("/student/edit_student", methods=['GET', 'POST'])
def edit_student():
    if request.method == "POST":
        studentID = request.form["studentID"]
        name = request.form["name"]
        year_level = request.form["YearLevel"]
        gender = request.form["gender"]
        course = request.form["course"]
        college = request.form["college"]

        # Check if a new picture is uploaded
        photo = request.files.get("profile_picture")
        photo_url = None

        if photo:
            # Upload the new photo to Cloudinary
            try:
                upload_result = upload(
                    photo,
                    folder="students",
                    public_id=studentID,  # Use studentID as the identifier for the file
                    overwrite=True
                )
                photo_url = upload_result["secure_url"]
            except Exception as e:
                print(f"Error uploading photo: {e}")
                return "Error uploading photo", 500
            
        Student.update_student(studentID, name, year_level, gender, course, college, photo_url)
        flash("Student updated successfully")
        return redirect(url_for('student.student'))

@studentbp.route("/search", methods=["GET", "POST"])
def student_search():
    search_query = request.form.get("search_query")
    search_type = request.form.get("search_type")
    form = AddStudent()
    # If searching by ID
    if search_type == "ID":
        result = Student.search_student_ID(search_query)
    if search_type == "course":
        result = Student.search_student_course(search_query)
    if search_type == "college":
        result = Student.search_student_college(search_query)
    if search_type == "gender":
        result = Student.search_student_gender(search_query)
    if search_type == "YearLevel":
        result = Student.search_student_year_level(search_query)

    # # If searching by Course, College, Gender, or Year Level
    # else:
    #     query = f"SELECT studentID, Name, {search_type} FROM students WHERE {search_type} = %s"
    #     cursor.execute(query, (search_query,))
    #     result = cursor.fetchall()

    return render_template("student.html", search_results=result, search_type=search_type, search_query=search_query, form = AddStudent())

