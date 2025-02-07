from repository.Student import Student
from repository.Validators import EntityValidator
from service.Repository import Repository


class StudentService:
    def __init__(self, student_Repository: Repository):
        self.__student_repository = student_Repository
        self.__StudentValidator = EntityValidator()

    def add_Student(self, id_student, name, group):
        # self.__student_repository.test()
        new_student = None
        self.__StudentValidator.validate_student(self.__student_repository.return_all(),id_student)

        self.__student_repository.save(new_student)

    def del_student(self, id_student):
        # self.__student_repository.test()
        student_to_del = self.__student_repository.return_object_by_id(None)
        self.__student_repository.delete(student_to_del)

    def update_student(self, id_student, name, group):
        updated_student = Student(id_student, name, group)
        self.__student_repository.update(updated_student)

    def return_student_by_id(self, id_stud):
        return self.__student_repository.return_object_by_id(None)

    def return_all_students(self):
        return self.__student_repository.return_all()
