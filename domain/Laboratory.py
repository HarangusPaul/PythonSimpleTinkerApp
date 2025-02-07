class Laboratory:
    def __init__(self, id_lab, labnumber, problemnumber, description, deadline):
        self.__lab_id = id_lab
        self.__number_lab = labnumber
        self.__number_problem = problemnumber
        self.__description = description
        self.__deadline = deadline

    def get_id(self):
        return self.__lab_id

    def get_number_lab(self):
        return self.__number_lab

    def get_number_problem(self):
        return self.__number_problem

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_id(self, value):
        self.__lab_id = value

    def set_number_lab(self, value):
        self.__number_lab = value

    def set_number_problem(self, value):
        self.__number_problem = value

    def set_description(self, value):
        self.__description = value

    def set_deadline(self, value):
        self.__deadline = value

    def __eq__(self, other):
        return self.__lab_id == other.get_id()

    def __str__(self):
        return "{0}/{1}/{2}/{3}".format(self.__lab_id, self.__number_lab, self.__number_problem,
                                        self.__description, self.__deadline)

    def __repr__(self):
        return "{0}/{1}/{2}/{3}\n".format(self.__lab_id, self.__number_lab, self.__number_problem,
                                        self.__description, self.__deadline)