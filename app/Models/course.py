from app.database import db_connection
import pymysql.cursors

class Course:

    @staticmethod
    def get_courses():
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM courses")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def get_courseCode():
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT DISTINCT courseCode FROM courses")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def add_course(courseCode, courseName, collegeCode):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "INSERT INTO courses (courseCode, courseName, collegeCode) VALUES (%s, %s, %s)"
        sqlValues = (courseCode, courseName, collegeCode)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete_course(courseCode):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "DELETE FROM courses WHERE courseCode = %s"
        sqlValues = (courseCode,)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update_course(courseCode, courseName, collegeCode):
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "UPDATE courses SET courseName = %s, collegeCode = %s WHERE courseCode = %s"
        sqlValues = (courseName, collegeCode, courseCode)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()