class Student:
    def __init__(self, name, age=13, grade='12th'):
        self._name = name
        self._age = age
        self._grade = grade
              
    #get_name
    @property
    def get_name(self):
        return self._name
    
    #set_name
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Name must be a string.')
            
    #get_age
    @property
    def get_age(self):
        return self._age
    
    #set_age
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 11 and new_age < 18:
            self._age = new_age
        else:
            print('Age must be an integer between 11 and 18.')
            
    #get grade
    @property
    def get_grade(self):
        return self._grade
    
    #set_grade
    @get_grade.setter
    def set_grade(self, new_grade):
        if isinstance(new_grade, int) and new_grade >= 9 and new_grade <= 12:
            self._grade = str(new_grade) + "th"
        else:
            print('Grade must be an integer between 9 and 12.')
    
    #__str__
    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Grade: {self._grade}" 
    
    #study
    #optional advance

john = Student("John", 16, "11th")
jane = Student("Jane")
print(john)
print(jane.get_age)
john.set_grade = 13
jane.set_age = 15
print(jane.get_age)
print(john)
