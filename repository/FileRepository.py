import os

from domain.Generator import Generator
from service.Repository import Repository
from repository.Validators import EntityException


class FileRepository(Repository):
    def __init__(self, filename,class_type):
        super().__init__()
        self._ensure_file_exists(filename)
        self.__filename = filename
        self.__class = class_type
        self.__generator = Generator()

    def _ensure_file_exists(self,filepath):
        """Ensure that the file and its directory exist."""
        directory = os.path.dirname(filepath)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            pass  # Create all missing parent directories

        # Create the file if it doesn't exist
        if not os.path.exists(filepath):
            pass
            print(f"File '{filepath}' created.")
        else:
            print(f"File '{filepath}' already exists.")
    def save(self, object_class):
        if self.return_object_by_id(object_class.get_id()) is None:
            pass
            file = open(self.__filename,"a")
            file.write(str(object_class))
            file.close()
            return
        raise EntityException("Type:{0} already created".format(self.__filename))

    def delete(self, object_class):
        list_of_entity = self.return_all()
        if super().return_object_by_id(object_class.get_id()) == object_class:
            super().delete(object_class)
        file = open(self.__filename, "w")
        for object in list_of_entity:
            file.write(str(object))
        file.close()

    def return_all(self):
        file = open(self.__filename, "r")
        for line in file:
            object = self.__generator.generate_student_class(line, self.__class)
            if super().return_object_by_id(object.get_id()) is None:
                super().save(object)
        return super().return_all()

    def return_object_by_id(self, id_object):
        if super().return_object_by_id(id_object) is not None:
            return super().return_object_by_id(id_object)
        file = open(self.__filename, "r")
        for lines in file:
            line = lines.split("/")
            if id_object == line[0]:
                super().save(self.__generator.generate_class(self.__class, lines))
                return super().return_object_by_id(id_object)
        return None

    def update(self, object):
        list_of_entity = self.return_all()
        if super().return_object_by_id(object.get_id()) is not None:
            super().update(object)
            file = open(self.__filename, "w")
            for object in list_of_entity:
                file.write(str(object))
            file.close()
        if super().return_object_by_id(object.get_id()) is None:
            error = self.__filename.split("_")
            raise EntityException("Type:{0} not created".format(error[0]))
