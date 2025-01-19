#Assignment2
#q1
L=[10,20,30,40,50,60,70,80]
L.append(200)
L.append(300)
print(L)
L.remove(10)
L.remove(30)
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
#q2
T=(45,89.5,76,45.4,89,92,58,45)
print('Max',max(T))
print('Index:',T.index(max(T)))
print('\n')
print('Min',min(T))
print('Count:',T.count(min(T)))
print('\n')
L=list(reversed(T))
print('Reversed tuple as List:',L)
num=eval(input('Enter a number to check:'))

if(num in T):
    print('Present at:',T.index(num))
else:
    print(num,' is not in tuple')
#q3
import random

def isPrime(a):
    for i in range(2,int(a/2) +1):
        if(a%i==0):
            return False

    return True


L = []
for i in range(100):
    L.append(random.randint(100, 900))

count_prime = 0
count_even = 0
count_odd = 0

for i in L:

    if (i % 2 == 0):
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

    if (isPrime(i)):
        count_prime = count_prime + 1

print('Number of even:  ', count_even)
print('Number of odd:   ', count_odd)
print('Number of prime: ', count_prime)
#q4
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
C = set()

C = A | B

print('Union: ', C)

D = set()
D = A & B

print('Intersection: ', D)

E = set()
E = A.symmetric_difference(B)

print('A-B UNION B-A: ', E)

if (A.issubset(B) or B.issuperset(A)):
    print('A is subset of B')
else:
    print('A is not a subset of B')

num = int(input('Enter a number to remove from A: '))

if (num in A):
    A.discard(num)
else:
    print(num, ' is not present in A')
print('A: ', A)
#q5
sample_dict={
    "name"  : "Kelly",
    "age:"  : 25,
    "salary":8000,
    "city"  :"New york"
}

print(sample_dict)
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
