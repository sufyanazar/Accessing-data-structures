#Assigning elements to different lists
a=[]
b=[]
n=int(input("Enter length of list1 :"))
print("Enter elements :")
for i in range(0,n):
    x=str(input())
    a.append(x)
print(a)
m=int(input("Enter length of list2 :"))
print("Enter elements :")
for i in range(0,m):
    y=str(input())
    b.append(y)
print(b)


#Accessing elements from a tuple
tuple1=(1,2,3,4,5,6)
print(a)
x=int(input("Enter the index of the element to be accessed :"))
print("The element is :",a[x])


#Deleting different dictionary elements
dict1={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(dict1)
d=int(input("Enter the element to be deleted:"))
dict1.pop(d)
print(dict1)

