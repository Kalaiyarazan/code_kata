n=input()
inp=n.split(" ")
min_inp=min(inp)
gcd=-1
for i in range(1,int(min_inp)+1):
    if(int(inp[0])%i==0 and int(inp[1])%i==0):
        gcd=i
print(gcd)
