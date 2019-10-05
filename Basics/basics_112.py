import functools
n=int(input())
lis=list(map(int,input().split(" ")[:n]))
print(functools.reduce(lambda x,y:x|y,lis))