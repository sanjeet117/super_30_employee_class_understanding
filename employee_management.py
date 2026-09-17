class Employee:
    def __init__(self,employee_id,name,salary,department):
        self.employee_id = employee_id 
        self.name = name 
        self.salary = salary 
        self.department = department 

    def display_details(self):
        print('\n ------employee Details---------')
        print(f'Employee_ID:  {self.employee_id}')
        print(f'name: {self.name}')
        print(f'salary: {self.salary}')
        print(f'department: {self.department}')

class Developer(Employee):
    def __init__(self,employee_id,name,salary,department,programming_language,experience):
        super().__init__(employee_id,name,salary,department)
        self.programming_language = programming_language 
        self.experience = experience 

    def display_developer_details(self):
        self.display_employee_details()
        print(f'Programming_language: {self.programming_language}')
        print(f'experience: {self.experience} years')


# creating Developer objects 
developer1 = Developer('E101','Sanjeet',70000,'IT','Python',3)
developer2 = Developer('E102','Rahul Sharma',80000,'IT','Java',3)
developer3 = Developer('E103','Amit Mishra',90000,'IT','C++',4)

# Program Execution code 
if __name__ == '__main__':

    # display developer details 
    developer1.display_developer_details() 
    developer2.display_developer_details()
    developer3.display_developer_details()

    # Demonstrating parent class functionality 
    print('\n --- Parent Class Method Access ---')
    developer1.display_details() 




    

