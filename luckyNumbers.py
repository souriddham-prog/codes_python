import math
def eliminate(array,p):
    
    new_array=[]
    for i in range(len(array)):
        if (i+1)%p!=0:
            new_array.append(array[i])
    return new_array

def displayLuckyNumbers(number):
    print(f"the lucky numbers upto {number} are")
    num_array=[]
    for i in range(number):
        num_array.append(i+1)
    
    print("\n")
    k=2
    while k<len(num_array):
        num_array=eliminate(num_array,k)
        k+=1
        print(num_array)
    

    print (num_array)

displayLuckyNumbers(45)
def isLucky(number,counter=2):
    if counter>number:
        return True
    elif number%counter==0:
        return False
    else:
        return isLucky(number-number//counter,counter+1)

for i in range(1,78):
   if isLucky(i):
       print(i,end=" ")


#displayLuckyNumbers(18)