from calculator import *

print(creator)

# gives me back a NameError because 
# with the under score i tell python not to 
# export year

# print(_year)


def twoSum( nums: list[int], target: int) -> list[int]:
        
    # Array of the indicies
    answer = []
                # get our firts number as reference
    for index1, number1 in enumerate(nums):
        if len(answer) == 2:
            break
            # get the second number as reference i want to add to the first one
        for index2, number2 in enumerate(nums):

            # To make shure the same index/number doesn't appears twice
            if number1 == number2 and index1 == index2:
                continue
            elif number1 + number2 == target:
                # adds both indices to our answer array
                answer.append(index1)
                answer.append(index2)
                break
            else:
                continue
        
    return answer
print(twoSum([3, 2, 4], 6))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3,3], 6))
