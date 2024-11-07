def find_student(student_id, students):
    return next((student for student in students if student.id == student_id), None)
