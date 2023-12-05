def count_failing_grades(percents):
    count = 0
    for percents in percents:
        if percents < 60:
            count = count + 1
    return count

inputList = ([90,67,40,23,59,89])
returnvalue = count_failing_grades(inputList)
print(returnvalue)

print("################")
def count_act_scores(scores):
    count = 0
    for score in scores:
        if score <= 36 and score >= 1:
            count = count + 1
    return count

print(count_act_scores([45,12,34,-6]))

print("###############")
def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
print(number_sum([5,3,2,5]))

print("##############")
def average_act_score(scores):
        count = 0
        totalScore = 0
        for score in scores:
            if score <= 36 and score >= 1:
                count = count + 1
                totalScore = totalScore + score
                avg = totalScore / count
        return avg
print(average_act_score([1,45,23,32,90]))
print("################")
def all_true(list1):
    for TorF in list1:
        if TorF == "False":
            return False
    else:
        return True
print(all_true(["True","True","True"]))
print(all_true(["False","False","True"]))
print(all_true(["True","True","True"]))
print("############")
def any_true(list1):
        for TorF in list1:
            if TorF == "True":
                return True
        else:
         return False
        
print(any_true(["False","True","True"]))
print(any_true(["False","False","True"]))
print(any_true(["False","False","False"]))
print("###########")
def mostly_true(list1):
    TCount = 0
    FCount = 0
    for TorF in list1:
        if TorF == "True":
            TCount = TCount + 1
        elif TorF == "False":
            FCount = FCount + 1
    if TCount > FCount:
        return True
    else:
        return False
    
print(mostly_true(["True","False","False","False"]))
print(mostly_true(["True","True","True","False"]))
print(mostly_true(["True","True","False","False"]))
      
print("###########")

def has_vowel(List1):
    for vowel in List1:
        if vowel in ["a","e","i","o","u"]:
            return True
        else:
            return False
        
print(has_vowel(["a","t","w"]))
print(has_vowel(["i","g","p"]))
print(has_vowel(["q","r","w"]))
print("#############")
def all_the_same(list1):
    first = list1[0]
    for number in list1:
        if first != list1[1]:
            return False
        
        return True
            
        
print(all_the_same([1,1,1]))
print(all_the_same([1,2,3]))
print(all_the_same([5,6,3]))

print("############")
def increasing(list1):
    first = list1[0]
    previous = list1[0]-1
    last = list1[-1]
    for num in list1:
        if num > previous and num > first and num > last:
            return True
    else:
        return False
    
print(increasing([1,2,2]))
print(increasing([3,2,1]))
print(increasing([1,2,3,4,5]))
  

#def is_incrementing():
    



