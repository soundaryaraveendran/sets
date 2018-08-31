string=input().split()
string1=list(string[0])
string2=list(string[1])
if len(string1)>len(string2):
    print(string[0])
elif len(string1)<len(string2):
    print(string[1])
elif len(string1)==len(string2):
    print(string[0])
