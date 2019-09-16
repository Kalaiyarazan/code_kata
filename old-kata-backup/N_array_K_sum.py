n=int(input())
k=int(input())
array=[]
sum=0
for i in range(n):
    element=int(input())
    array.append(element)
    if(i<k):
        sum=sum+element
print(array)
print(sum)
