import collections

# easy way to initialize a class
Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")

class Library():

    def __init__(self, *books) -> None:
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)

print(len(l1))
print(len(l2))

arr = [7, 69 ,2 ,221, 8974]

print(sum(sorted(arr[0:-1])), sum(sorted(arr[1:])))
print(sorted(arr))

print()

x = [1, 2, 3]

def hla(i=1, name):
    pass
