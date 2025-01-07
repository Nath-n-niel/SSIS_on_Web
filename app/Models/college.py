from app.database import db_connection
import pymysql.cursors

class College:

    @staticmethod
    def get_colleges():
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM colleges")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def get_collegeCode():
        connection = db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT DISTINCT collegeCode FROM colleges")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    @staticmethod
    def add_college(collegeName, collegeCode):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "INSERT INTO colleges (collegeName,collegeCode) VALUES(%s, %s)"
        sqlValues = (collegeName, collegeCode)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete_college(collegeCode):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "DELETE FROM colleges WHERE collegeCode = %s"
        sqlValues = (collegeCode,)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update_college(collegeName, collegeCode):
        connection = db_connection()
        cursor = connection.cursor()
        sqlQuery = "UPDATE colleges SET collegeName = %s WHERE collegeCode = %s"
        sqlValues = (collegeName, collegeCode)
        cursor.execute(sqlQuery, sqlValues)
        connection.commit()
        cursor.close()
        connection.close()
