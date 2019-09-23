n=input()
inp=n.split(" ")
min_inp=min(inp)
gcd=-1
for i in range(1,int(min_inp)+1):
    if(int(inp[0])%i==0 and int(inp[1])%i==0):
        gcd=i
print(gcd)
# clarification: unable to print "-1"


# 18
# Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
# Sample Testcase :
# INPUT
# 10 5
# OUTPUT
# 5