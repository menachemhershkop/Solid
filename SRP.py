class Book:
    def __init__(self,title:str, author:str, content:str):
        self.title=title
        self.author=author
        self.content=content
    # def save_to_file(self,filname):
    #     with open(filname,'w') as file:
    #         file.write(self.content)
    #  wrong exemple

class Write(Book):
    def save_to_file(self,filname):
        with open(filname, 'w') as file:
            file.write(self.content)