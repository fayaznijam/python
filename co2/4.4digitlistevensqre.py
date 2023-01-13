
import math


start = int (input("Enter a starting number ( 4 digit ) : "))
end = int (input("Enter a ending number ( 4 digit ) : "))

l=[]
for i in range(start,end):
    for j in str(i):
        if int(j)%2!=0:
            break
        s=math.sqrt(i)
        if(s%1==0):
            l.append(i)
print(l)
