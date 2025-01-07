from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint, current_app, make_response

from cloudinary import CloudinaryImage
from cloudinary.uploader import upload

from app.Models import Student
from app.Models import College
from app.Models import Course
from app.Forms import AddCourse
coursebp = Blueprint('course',__name__)

@coursebp.route('/course')
def course():
    form = AddCourse()
    coureses = Course.get_courses()
    colleges = College.get_collegeCode()

    form.college.choices = [(college['collegeCode'], college['collegeCode']) for college in colleges]
    return render_template('course.html', courses=coureses, colleges=colleges, form=form)

@coursebp.route('/course/add_course', methods=['POST'])
def add_course():
    courseCode = request.form['courseCode']
    courseName = request.form['courseName']
    collegeCode = request.form['college']

    Course.add_course(courseCode, courseName,collegeCode)
    flash('Course added successfully', 'success')
    return redirect(url_for('course.course'))

@coursebp.route('/course/delete_course/<courseCode>', methods=['GET', 'POST'])
def delete_course(courseCode):
    Course.delete_course(courseCode)
    flash('Course deleted successfully', 'success')
    return redirect(url_for('course.course'))

@coursebp.route('/course/edit_course', methods=['GET', 'POST'])
def edit_course():
    # Retrieve the form data from the modal
    courseCode = request.form['courseCode']
    courseName = request.form['courseName']
    collegeCode = request.form['college']

    Course.update_course(courseCode, courseName, collegeCode)
    flash('Course updated successfully', 'success')
    return redirect(url_for('course.course'))