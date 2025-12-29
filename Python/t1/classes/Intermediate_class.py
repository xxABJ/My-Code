class Student:

    @staticmethod
    def is_valid_age(age):
        if age.isdigit() and 18 < int(age) < 25:
            return True
        return False

    num_students = 0
    longest_major_length = 0

    def set(**kwargs):
        Student.num_students += 1
        return Student(kwargs)
        
    def __init__(self, kwargs):
        print()
        for key, value in kwargs.items():
            setattr(self, key, value)
            #print(self.__dict__)
        ##self.length_of_major()
        
        self.database_entry = {'ID': Student.num_students, **kwargs,'gpa': kwargs['gpa'] if 'gpa' in kwargs else 0.0}
        #print("\nDatabase Entry:\n", self.database_entry)
    
    def length_of_major(self):
        for key, value in self.__dict__.items():
            if key == 'major' and len(value) > Student.longest_major_length:
                Student.longest_major_length = len(str(value))
                print({Student.longest_major_length})

    def print_info(self):
        for key, value in self.__dict__.items():
            if not self.__dict__['database_entry'] == self.__dict__[key]:
                print(f"~    {key:<15}:{str(value):>{Student.longest_major_length + 1}}")
        
    def extract_database_entry(self):
        return self.database_entry

kwargs_list = []
while True:

    student = input("Create a new student? (y/n): ")
    if student.lower() == 'n':
        break
    elif not student.lower() == 'y':
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    if student.lower() == 'y':
        kwargs = {}
        valid = True
        age_check = "not set"
        while True:
            if valid:
                print(f"\n| DATA ENTRY")
                print("| ----------")
                print("|")
                for key, value in kwargs.items():
                    if key == 'age' and not age_check:
                        print(f"| ** age: Invalid age ({value}). Age must be a number between 18 and 25 to be accepted in this special sponsorship program.")
                        #del kwargs['age']
                    else:
                        print(f"|   {key}: {value}", end='\n')
                if not len(kwargs) == 0:
                    print("|")
                    print("| ----------")
                
            more = input("\nAdd fields? (y/n): ")
            if more.lower() == 'n' and (len(kwargs) == 0 or len(kwargs) != 0):
                if len(kwargs) != 0 and (not age_check or age_check == "not set"):
                    print("\nMust provide a valid age before finishing data entry.")
                    ans = input("do you want to continue adding fields? (y/n): ")
                    while True:
                        if ans.lower() == 'y':
                            break
                        elif ans.lower() == 'n':
                            print("\nStudent data deleted.")
                            kwargs = {}
                            break
                        else:
                            ans = input("\nInvalid input. Please enter 'y' or 'n': ")
                    if ans.lower() == 'y':
                        continue
                    else:
                        break
                else:
                    print("\nUser data:")
                    print(kwargs)
                    kwargs_list.append(kwargs)
                    for key, value in kwargs.items():
                        (exec(f"student{len(kwargs_list)} = Student.set(**kwargs)"))
                        break
                    break
            elif more.lower() == 'n':
                print("\nUser data:")
                print(kwargs)
                kwargs_list.append(kwargs)
                for key, value in kwargs.items():
                    (exec(f"student{len(kwargs_list)} = Student.set(**kwargs)"))
                    break
                break
            elif not more.lower() == 'y':
                print("Invalid input. Please enter 'y' or 'n'.")
                valid = False
                continue

            keyword = input("Enter KEY (i.e name, age, major, gpa): ")
            value = input(f"Enter VALUE for {keyword}: ")
            if keyword == 'age':
                age_check = Student.is_valid_age(value)
            kwargs[keyword] = value
            valid = True
          
#print(kwargs)

#for key, value in kwargs.items():
#    (exec(f"student{list(kwargs.keys()).index(key)+1} = Student.set(**kwargs)"))
#    break
#        #new_student = Student.set(name=name, age=age, major=major, gpa=gpa)
#        #print("\nNew student created:")
#        #new_student.print_info()
#        #print("\nDatabase Entry:")
#        #print(new_student.extract_database_entry())

#print(f"print(kwargs): {print(kwargs)}")

for kwargs in kwargs_list:
    print()
    print(f"~ Student ID {kwargs_list.index(kwargs)+1}'s Info:")
    (exec(f"student{kwargs_list.index(kwargs)+1}.print_info()"))
    print("\n• Database Entry:")
    (exec(f"print('• ',student{kwargs_list.index(kwargs)+1}.extract_database_entry())")) 
    print()

#student1 = Student.set(name="Alice", age=20, major="Computer Science")
#student2 = Student.set(name="Bob", age=22, major="Mathematics")
#student3 = Student.set(name="Charlie", age=21, major="Physics", gpa=3.8)
#student4 = Student.set(name="David", age=23, major="Biochemistry and Molecular Biology", gpa=3.5)
#student5 = Student.set(name="Eve", age=20, major="Art History", gpa=3.9)

#print(student1.name)  # Output: Alice
#print(student2.major)  # Output: Mathematics
#print(Student.num_students)  # Output: 2

#print("\nStudent 1 Info:")
#student1.print_info()
#print("\nStudent 2 Info:")
#student2.print_info()
#print("\nStudent 3 Info:")
#student3.print_info()
#print("\nStudent 4 Info:")
#student4.print_info()
#print("\nStudent 5 Info:")
#student5.print_info()

#print("\nDatabase Entries:")
#print(student1.extract_database_entry())
#print(student2.extract_database_entry())
#print(student3.extract_database_entry())
#print()




