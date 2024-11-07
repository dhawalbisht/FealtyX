class Student:
    def __init__(self, student_id, name, age, email):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['age'], data['email'])
