def make_abc():
    result = ["a","b","c"]
    return result

print(make_abc())

print("################")

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


print("################")


def common_edge(list1, list2):
    if list1[0] == list2[0] or list1[0] == list2[-1] or list1[-1] == list2[-1] or list1[-1] == list2[0]:
        return True
    else: 
        return False
    
print(common_edge())
    







