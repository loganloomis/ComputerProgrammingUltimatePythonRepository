
print("make_abc")
def make_abc():
    result = ["a","b","c"]
    return result

print(make_abc())

print("equal_edges")

def equal_edges(num1, num2, num3, num4):

    numList = [num1, num2, num3, num4]
    if num1 == num4:
        return True
    else: 
        return False
print(equal_edges(1,2,3,1))
print(equal_edges(4,2,3,1))
print(equal_edges(6,9,4,6))
print(equal_edges(8,2,3,1))


print("common_edge")


def common_edge(list1, list2):
    if list1[0] == list2[0] or list1[0] == list2[-1] or list1[-1] == list2[-1] or list1[-1] == list2[0]:
        return True
    else: 
        return False
    
print(common_edge([1,2,3],[3,2,1]))
print(common_edge([1,2,3],[4,2,7]))
print(common_edge([8,7,2],[2,4,5]))


print("all_the_same")
    


def all_the_same(list1):
    if list1[0] == list1[1] and list1[0] == list1[2]:
        return True
    else: 
        return False
    
print(all_the_same([1,1,1]))
print(all_the_same([6,3,6]))
print(all_the_same([9,9,9]))



print("all_unique")



def all_unique(list1):
    if list1[0] != list1[1] and list1[0] != list1[2]:
        return True
    else: 
        return False
    
print(all_unique([1,2,3]))
print(all_unique([6,3,6]))
print(all_unique([9,9,9]))
print(all_unique([8,2,3]))


print("Increasing")




def increasing(list1):
    if list1[2] > list1[1] and list1[2] > list1[0]:
        return True
    else:
        return False
print(increasing([1,2,3]))
print(increasing([5,5,5]))
print(increasing([-1,0,1]))



print("all_true")

def all_true(list1):
    if list1[0] == "True" and list1[1] == "True" and list1[2] == "True":
        return True
    else:
        return False

print(all_true(["True","True","True"]))
print(all_true(["False","True","True"]))
print(all_true(["False","False","True"]))




print("mostly_true")

def mostly_true(list1):

    first = list1[0]
    middle = list1[1]
    last = list1[2]
    

    if first == "True" and middle == "True" or  first == "True" and last == "True" or middle == "True" and first == "True" or middle == "True":
        return True
    else:
        return False
print(mostly_true(["True","False","True"]))
print(mostly_true(["False","False","False"]))
print(mostly_true(["True","True","True"]))
print(mostly_true(["False","True","False"]))
print(mostly_true(["True","False","False"]))

print("make_copy")

def make_copy(list1):
    return list1[0], list1[1], list1[2]

print(make_copy([1,2,3]))

print("repeat_thrice")
def repeat_thrice(list1):
    return list1[0], list1[0], list1[0]
print(repeat_thrice([1]))

print("make_reversed_copy")

def make_reversed_copy(list1):
    return list1[2], list1[1], list1[0]
print(make_reversed_copy([1,2,3]))

print("reverse_in_place")

def reverse_in_place(list1):
    first = list1[2]
    last = list1[0]
    middle = list1[1]
    newList = [first, middle, last]


    return(newList)

print(reverse_in_place([1,2,3]))
