
# The smaller you make things, the smaller resposinility that 
# each object has, the more stable the program will be 

class Paper():
    def __init__(self, text, case):
        self.text = text 
        self.case = case 

class Briefcase():
    def __init__(self, price):
        self.price = price 
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]


class Lawyer():
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        print(self.briefcase.view_notes())


cheap_briefcase = Briefcase(price = 19.99)
Juan = Lawyer("Juan", briefcase= cheap_briefcase)

Juan.write_note("Hi my name is Juan and I'm your lawyer", "1")
Juan.write_note("I need more money!", "1")

Juan.view_notes()

# el proposito de esta leccion fue mostrarme que la mejor manera de 
# diseñar codigo es dividiendolo en pequeñas clases las cuales hacen mas 
# solido y facil de cambiar el codigo ya que no todo se encuentra dentro 
# de una enorme clase que contiene todo y a la hora de querer hacer 
# modificaciones se puede tornar un poco tedioso

