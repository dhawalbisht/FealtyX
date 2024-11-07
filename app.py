# app.py

from flask import Flask
from controllers.student_controller import create_student, get_students, get_student, update_student, delete_student, student_summary

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student_route():
    return create_student()

@app.route('/students', methods=['GET'])
def get_students_route():
    return get_students()

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    return get_student(student_id)

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_route(student_id):
    return update_student(student_id)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    return delete_student(student_id)

@app.route('/students/<int:student_id>/summary', methods=['GET'])
def student_summary_route(student_id):
    return student_summary(student_id)

if __name__ == '__main__':
    app.run(debug=True)
