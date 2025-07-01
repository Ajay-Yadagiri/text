'''input("enter the a ")
b= input("enter the b")
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")'''
'''a=[1,5,4,5,2,6]
s=set(a)
print(s)
if 3 in s:
    print("element is found")
else:
    print("element is not found")'''
'''for i in range(0,10,):
    print(i,end= " ")'''
'''i=1
while i<=10:
    print(i,end=' ')
    i+=1'''
'''a=[1,3,4,3,43,2,3,2,3,4,5,6]
n=len(a)
target=10
for i in range (n):
    if a[i]==target:
        print("true")
        break
    else:
        print("false"
        )
        break'''

"""d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
"""
a = [1, 2, 1, 2, 1, 4, 5, 6, 7, 8, 8, 2, 2, 1]
largest = a[0]

for i in a:
    if i > largest:
        largest = i

print("Largest number is:", largest)
