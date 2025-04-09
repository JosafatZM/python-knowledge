# A class attribute can be used whenever 
# there is a piece of data that does not need 
# to be copied among all objects. An example is 
# a constant value that will not be changed or 
# mutated.

class Counter():
    count = 0
    
    def __init__(self) -> None:
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counter: {cls.count}")
        return two_counters
    
print(Counter.count)
c1 = Counter()
print(Counter.count)

c2, c3 = Counter.create_two()
print(Counter.count)

print(c1.count)
print(c2.count)
print(c3.count)

c4 = Counter()

print(c1.count)
print(c2.count)
print(c3.count)
