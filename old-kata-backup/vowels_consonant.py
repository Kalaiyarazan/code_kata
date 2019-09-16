char=input()
char=char.lower()
vow=("a","e","i","o","u")
def vowels():
    if char in vow:
        print("Vowels")
    else:
        print("Consonant")
if(char>='a' and char<='z'):
    vowels()
else:
    print("Invalid")