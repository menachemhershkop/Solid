#1
class Book:
    def __init__(self,title:str, author:str, content:str):
        self.title=title
        self.author=author
        self.content=content
    # def save_to_file(self,filname):
    #     with open(filname,'w') as file:
    #         file.write(self.content)
    #  wrong exemple

class Write:
    @staticmethod
    def save_to_file(filname,content):
        with open(filname, 'w') as file:
            file.write(content)

#2
class Student:
    def __init__(self,name:str,grades:list[int]):
        self.name=name
        self.grades=grades
    # def average_grade(self):
    #     return sum(self.grades)/len(self.grades)
    # wrong exemple
class GradeCalculator:
    @staticmethod
    def average_grade(grades):
        return sum(grades)/len(grades)

#3
class Order:
    def __init__(self,items:list[str],total_price:float):
        self.items=items
        self.total_price=total_price
    # def print_invoice(self):
    #     print(sorted(self.items))
    #     print(self.total_price)
    #  wrong exemple

class InvoicePrinter:
    @staticmethod
    def print_invoice(item):
        print(sorted(item))
