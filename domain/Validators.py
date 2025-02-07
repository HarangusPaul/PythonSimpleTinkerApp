class StudentExeption(Exception):
    pass

class EntityException(Exception):
    pass

class FileExeption(Exception):
    pass

class EntityValidator:
    def validate_student(self,list_of_objects,id_object):
        for object in list_of_objects:
            if object.get_id() == id_object:
                raise StudentExeption("Student already exist!")
