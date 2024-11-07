from flask import jsonify, request, abort
from models.student_model import Student
from services.llama_service import generate_summary
from utils.helpers import find_student

students = []

def create_student():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'age' not in data or 'email' not in data:
        abort(400, "Invalid student data")

    if find_student(data['id'], students):
        abort(400, "Student with this ID already exists")

    student = Student.from_dict(data)
    students.append(student)
    return jsonify(student.to_dict()), 201

def get_students():
    return jsonify([student.to_dict() for student in students])

def get_student(student_id):
    student = find_student(student_id, students)
    if not student:
        abort(404, "Student not found")
    return jsonify(student.to_dict())

def update_student(student_id):
    student = find_student(student_id, students)
    if not student:
        abort(404, "Student not found")

    data = request.get_json()
    for key, value in data.items():
        if hasattr(student, key):
            setattr(student, key, value)

    return jsonify(student.to_dict())

def delete_student(student_id):
    student = find_student(student_id, students)
    if not student:
        abort(404, "Student not found")
    
    students.remove(student)
    return jsonify({"message": "Student deleted"})

def student_summary(student_id):
    student = find_student(student_id, students)
    if not student:
        abort(404, "Student not found")

    summary = generate_summary(student)
    return jsonify({"summary": summary})
