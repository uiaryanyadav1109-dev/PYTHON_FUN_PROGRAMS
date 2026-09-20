#Python Program to find the Average of th first n natural numbers 
n=int(input("Enter the value of n:"))
avg=0.0
s=0
for i in range(1,n+1):
    s=s+i
avg=s/i
print("The Sum of first",n,"natural numbers is:",s)
print("The Avg of first",n,"natural numbers is:",avg)
