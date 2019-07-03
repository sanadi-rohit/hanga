#a python code to demonstrate the working of oops
class student:
    school= "bec"
    def  __init__(self,name):
        self.name=name
    class sport:
        def __init__(self,sportname,prize):
            self.sportname=sportname
            self.prize=prize
    def set_age(self,age):
        self.age = age
    def get_info(self):
        print(f'name={self.name}\nschool={self.school}\nage={self.age}\nsports name={self.sp1.sportname}')
    @classmethod
    def set_school(cls,school):
        cls.school=school

class teacher(student):
    class project:
        def __init__(self,project_name):
            self.project_name=project_name
    def get_info(self):
        print(f'name={self.name}\nage={self.age}\nproject={self.p1.project_name}')




s1=student("rohit")
s1.set_age(21)
student.set_school("forbes")
s1.sp1=student.sport("football","prize")
s1.get_info()
t1=teacher("sanadi")
t1.set_age(35)
t1.p1=teacher.project("python")
t1.get_info()

