class Repository:
    def __init__(self):
        self.__repository = []

    def return_all(self):
        return self.__repository

    def save(self, object_class: object):
        self.__repository.append(object_class)

    def delete(self, object_class: object):
        self.__repository.remove(object_class)

    def return_object_by_id(self, id_object: int):
        object_class = [object for object in self.__repository if object.get_id() == id_object]
        try:
            return object_class[0]
        except IndexError:
            return None

    def update(self,object):
        for inter,obj in enumerate(self.__repository):
            if object.get_id() == obj.get_id():
                self.__repository[inter] = object





