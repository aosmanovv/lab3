import math
import random
from itertools import permutations

def gramToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

def FtoC(F):
    C = (5 / 9) * (F - 32)
    return C

def solve(numheads, numlegs):
    for i in range(0,numheads+1):
        if (i*4+(numheads-i)*2==numlegs):
            print (f"{i} rabbits and {numheads-i} chickens")

def filter_prime(l):
    new_l=[]
    def find_divisors(n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors
    for i in l:
        if (len(find_divisors(i))==2):
            new_l.append(i)
    return new_l

def perm(s):
    return list(permutations(s))

def revWords(s):
    l=s.split(" ")
    l=list(reversed(l));
    return l;

def has_33(nums):
    l=0;
    ans=False
    for i in nums:
        if l==3 & i==3:
            ans=True
        l=i
    return ans
def spy_game(nums):
    l=1;
    ll=1
    ans=False
    for i in nums:
        #print(f"{ll}{l}{i}")
        if l==0 and ll==0 and i==7:
            ans=True
        ll=l
        l=i
    return ans

def vol(r):
    return (math.pi*r*r)

def uniq(l=[]):
    l.sort()
    new_l=[]
    new_l.append(l[0]);

    for i in range(1,len(l)):
        #print(f"{l[i]}{l[i-1]}")
        if l[i]!=l[i-1]:
            new_l.append(l[i])
    return new_l

def hist(l=[]):
    for i in l:
        print("*"*i)
def isPal(s):
    if list(s)==list(reversed(s)):
        return True
    else:
        return False

def kbtu():
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    r=random.randint(1,20)
    g=0
    c=0
    while g!=r:
        c+=1
        print("Take a guess.")
        g=int(input())
        if g<r:
            print("Your guess is too low.")
        if g>r:
            print("Your guess is too high.")
    print(f"Good job, {name}! You guessed my number in {c} guesses!")

print(gramToOunces(12))
print(FtoC(12))
solve(35,94)
print(filter_prime([1,2,3,4,5,6,7,8,9,10]))
print(perm("abc"))
print(revWords("We are ready"))
print(has_33([1,2,3,3,1,2]))
print(spy_game([1,0,0,7,1,2]))
print(vol(3))
print(uniq([1,2,3,3,1,2]))
print(isPal("aga"))
hist([1,2,3])
kbtu()