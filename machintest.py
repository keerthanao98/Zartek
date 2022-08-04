

def addindex(numbers,target):
    A ={}
    for i in range(len(numbers)):
        A[numbers[i]]= i
    for i in range(len(numbers)):
        B= target - numbers[i]
        if B in A:
            return [i,A[B]]
print(addindex([2,7,11,15],9))

