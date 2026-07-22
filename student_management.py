import json

class Student():

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def to_dict(self):
        dict = {"name" : self.name, "marks" : self.marks} 
        return dict

    def save_to_file(self):
        save = self.to_dict()
        with open("Records.json", "w") as f:
            json.dump(save,f)

    @classmethod
    def load_from_file(cls):
        with open("Records.json","r") as f:
            data = json.load(f)
            stud = cls(data["name"],data["marks"])
            return stud

s1 = Student("vini",82)
s1.save_to_file()
s = Student.load_from_file()
print(s1.name,s1.marks)



            



    