a=input("Radius Of Cylinder = ")
a=float(a)
b=input("Height Of Cylinder = ")
b=float(b)
c=input("Entre Your Calculated Answer = ")
c=float(c)
d=((6.32*a*b)+(6.32*a*a))
d=float(d)
if (c!=d):print("your answer is incorrect, ","correct answer is ",d)
if (c==d):print("Congratulation's your answer is correct")