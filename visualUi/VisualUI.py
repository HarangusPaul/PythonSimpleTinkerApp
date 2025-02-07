import tkinter as tk
from tkinter import messagebox

from domain.Lab_assigment import Lab_assigment
from domain.Laboratory import Laboratory
from domain.Student import Student
from repository.FileRepository import FileRepository
from repository.Repository import Repository
from service.StudentService import StudentService
from service.LaboratoryProblem import LaboratoryService
from service.serviceManager import ServiceManager
from domain.Validators import StudentExeption


class TinkererUI:
    def __init__(self, root, student_service: StudentService, lab_service: LaboratoryService,
                 service_manager: ServiceManager):
        self.root = root
        self.root.title("Student & Lab Management")

        self.student_service = student_service
        self.lab_service = lab_service
        self.service_manager = service_manager

        self.create_widgets()

    def create_widgets(self):
        self.menu_list = [
            ("Add Student", self.add_new_stud),
            ("Delete Student", self.del_stud),
            ("Add Lab", self.add_new_lab),
            ("Delete Lab", self.del_lab),
            ("Update Student", self.update_stud),
            ("Update Lab", self.update_lab),
            ("Find Student by ID", self.find_stud),
            ("Find Lab by ID", self.find_problem),
            ("Assign Lab", self.add_assignment),
            ("Grade Student", self.add_grade),
            ("Students in Lab", self.raport_per_lab),
            ("Students with Bad Grades", self.raport_bad_grades)
        ]

        for idx, (label, command) in enumerate(self.menu_list):
            btn = tk.Button(self.root, text=label, command=command, width=25)
            btn.grid(row=idx, column=0, pady=5)

    def get_input(self, prompt):
        def submit():
            self.user_input = entry.get()
            input_window.destroy()

        input_window = tk.Toplevel(self.root)
        input_window.title("Input Required")
        tk.Label(input_window, text=prompt).pack()
        entry = tk.Entry(input_window)
        entry.pack()
        tk.Button(input_window, text="Submit", command=submit).pack()
        input_window.wait_window()
        return self.user_input

    def add_new_stud(self):
        try:
            student = self.get_input("Student (Id/Name/Group):").split("/")
            self.student_service.add_Student(int(student[0]), student[1], student[2])
            messagebox.showinfo("Success", "Student added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def del_stud(self):
        try:
            id_stud = int(self.get_input("Student ID:"))
            self.student_service.del_student(id_stud)
            messagebox.showinfo("Success", "Student deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_new_lab(self):
        try:
            lab = self.get_input("Lab (id_lab/lab_number/problem_number/description/deadline DD:MM):").split("/")
            self.lab_service.add_lab(int(lab[0]), int(lab[1]), int(lab[2]), lab[3], lab[4])
            messagebox.showinfo("Success", "Lab added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def del_lab(self):
        try:
            id_lab = int(self.get_input("Lab ID:"))
            self.lab_service.del_lab(id_lab)
            messagebox.showinfo("Success", "Lab deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_stud(self):
        try:
            student = self.get_input("Update Student (Id/Name/Group):").split("/")
            self.student_service.update_student(int(student[0]), student[1], student[2])
            messagebox.showinfo("Success", "Student updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_lab(self):
        try:
            lab = self.get_input("Update Lab (id_lab/lab_number/problem_number/description/deadline DD:MM):").split("/")
            self.lab_service.update_lab(int(lab[0]), int(lab[1]), int(lab[2]), lab[3], lab[4])
            messagebox.showinfo("Success", "Lab updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def find_stud(self):
        try:
            id_stud = int(self.get_input("Student ID:"))
            student = self.student_service.return_student_by_id(id_stud)
            messagebox.showinfo("Student Info", str(student))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def find_problem(self):
        try:
            id_lab = int(self.get_input("Lab ID:"))
            lab = self.lab_service.return_lab_by_id(id_lab)
            messagebox.showinfo("Lab Info", str(lab))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_grade(self):
        try:
            student_id = int(self.get_input("Student ID:"))
            lab_id = self.get_input("Lab ID:")
            grade = self.get_input("Grade:")
            self.service_manager.note_student(student_id, lab_id, grade)
            messagebox.showinfo("Success", "Grade assigned successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_assignment(self):
        try:
            student_id = int(self.get_input("Student ID:"))
            lab_id = int(self.get_input("Lab ID:"))
            self.service_manager.assigne_lab_and_stud(student_id, lab_id)
            messagebox.showinfo("Success", "Lab assigned successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def raport_per_lab(self):
        try:
            lab_id = int(self.get_input("Lab ID:"))
            students = self.service_manager.return_stud_for_given_lab(lab_id)
            messagebox.showinfo("Students in Lab", str(students))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def raport_bad_grades(self):
        try:
            students = self.service_manager.return_bad_stud()
            messagebox.showinfo("Students with Bad Grades", str(students))
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    option = 2
    if option == 1:
        student_Rep = Repository()
        lab_Rep = Repository()
        assigment_Rep = Repository()

        assigment_service = ServiceManager(assigment_Rep, student_Rep)
        stud_Service = StudentService(student_Rep)
        lab_Service = LaboratoryService(lab_Rep)

        app = TinkererUI(root, stud_Service, lab_Service, assigment_service)
        root.mainloop()
    else:
        student_Rep = FileRepository("Files/Student_File_Repository", Student)
        lab_Rep = FileRepository("Files/Laboratory_File_Repository", Laboratory)
        assigment_Rep = FileRepository("Files/Assigments_File_Repository", Lab_assigment)

        assigment_service = ServiceManager(assigment_Rep, student_Rep)
        stud_Service = StudentService(student_Rep)
        lab_Service = LaboratoryService(lab_Rep)

        app = TinkererUI(root, stud_Service, lab_Service, assigment_service)
        root.mainloop()
