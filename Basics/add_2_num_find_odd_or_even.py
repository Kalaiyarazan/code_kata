nm_input=input()
nm_input_array=nm_input.split(" ")
n=int(nm_input_array[0])
m=int(nm_input_array[1])
sum=n+m
if sum%2==0:
    print("even")
elif sum%2==1:
    print("odd")
else:
    print("Input error")



# 1
# Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
# Sample Testcase :
# INPUT
# 9 2
# OUTPUT
# odd