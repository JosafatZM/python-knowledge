class Student():

    def __init__(self, math, history, writing) -> None:
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    # dunder eq must alwars return a boolean 
    def __eq__(self, __value: object) -> bool:
        return self.grades == __value.grades
    
roberto = Student(math=100, history=100, writing=100)
raul = Student(math=80, history=90, writing=80)
chritian = Student(math=100, history=80, writing=70)

print(roberto.grades, raul.grades, chritian.grades)

print(roberto == raul)
print(raul == chritian)
print(roberto != raul)
print(raul != chritian)