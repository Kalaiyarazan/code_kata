N=int(input())
range=input()
num_range=range.split(" ")
if int(num_range[0])<N and N<int(num_range[1]):
    print("yes")
else:
    print("no")