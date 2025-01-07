from app.database import db_connection
import pymysql.cursors

class Student:

    @staticmethod
    def get_students():
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def add_student(studentId, Name, YearLevel, Gender, Course,College, photo_url):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO students (studentId, Name, YearLevel, Gender, Course, College, Photo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        sqlValues = (studentId, Name, YearLevel, Gender, Course,College, photo_url)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete_student(studentId):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "DELETE FROM students WHERE studentId = %s"
        sqlValues = (studentId,)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update_student(studentId, Name, YearLevel, Gender, Course, College, photo_url):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "UPDATE students SET Name = %s, YearLevel = %s, Gender = %s, Course = %s, College = %s, Photo = %s WHERE studentId = %s"
        sqlValues = (Name, YearLevel, Gender, Course, College, photo_url, studentId)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def search_student_ID(studentID):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "SELECT * FROM students WHERE studentID = %s"
        # sqlValues = (studentID,)
        cursor.execute(sqlQuery, (studentID,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def search_student_course(Course):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "SELECT * FROM students WHERE Course = %s"
        # sqlValues = (Course,)
        cursor.execute(sqlQuery, (Course,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def search_student_college(College):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "SELECT * FROM students WHERE College = %s"
        # sqlValues = (College,)
        cursor.execute(sqlQuery, (College,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def search_student_year_level(YearLevel):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "SELECT * FROM students WHERE YearLevel = %s"
        # sqlValues = (YearLevel,)
        cursor.execute(sqlQuery, (YearLevel,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def search_student_gender(Gender):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "SELECT * FROM students WHERE Gender = %s"
        # sqlValues = (Gender,)
        cursor.execute(sqlQuery, (Gender,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    
    @staticmethod
    def update_enrollment_status(studentID, EnrollmentStatus):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "UPDATE students SET EnrollmentStatus = %s WHERE studentID = %s"
        sqlValues = (EnrollmentStatus, studentID)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    
