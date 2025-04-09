class FilmMaker():
    def give_interview(self):
        print("I love making movies!")

class Director(FilmMaker):
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love making scripts!")

class JackOfAllTrades(Director, Screenwriter):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

# <class '__main__.FilmMaker'> is at the end because it's going to 
# occur multiple times in the search hierarchy so python
# removes all earlier occurrences of the object superclass
# up until the very last one
print(JackOfAllTrades.mro())
# [<class '__main__.JackOfAllTrades'>, 
# <class '__main__.Director'>, 
# <class '__main__.Screenwriter'>,
# <class '__main__.FilmMaker'>, 
# <class 'object'>]