from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint, current_app, make_response

from cloudinary import CloudinaryImage
from cloudinary.uploader import upload

from app.Models import Student
from app.Models import College
from app.Models import Course

from app.Forms import AddCollege

collegebp = Blueprint('college',__name__)


@collegebp.route('/college')
def college():
    form = AddCollege()
    colleges = College.get_colleges()

    return render_template('college.html', colleges=colleges, form=form)


@collegebp.route('/college/add_college', methods=['GET', 'POST'])
def add_college():
    collegeName = request.form['collegeName']
    collegeCode = request.form['collegeCode']

    College.add_college(collegeName,collegeCode)

    flash('College added successfully')
    return redirect(url_for('college.college'))


@collegebp.route('/college/delete_college/<collegeCode>', methods=['GET', 'POST'])
def delete_college(collegeCode):
    College.delete_college(collegeCode)

    flash('College deleted successfully')
    return redirect(url_for('college.college'))


@collegebp.route('/college/edit_college/', methods=['GET', 'POST'])
def edit_college():
    # Retrieve the form data from the modal
    collegeName = request.form['collegeName']
    collegeCode = request.form['collegeCode']  # This is a hidden field and not editable

    College.update_college(collegeName,collegeCode)
    flash('College updated successfully')
    return redirect(url_for('college.college'))