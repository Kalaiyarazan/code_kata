n=int(input())
numbers=input()
num_array=numbers.split()
int_array=[]
if len(num_array)==n:
    for i in num_array:
        int_array.append(int(i))
    print(min(int_array),max(int_array))
    
else:
    print(f'Enter exactly {n} numbers')













# Given a number N followed by N numbers. Find the smallest number and largest number and print both the indices(1based indexing).
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 1 5

