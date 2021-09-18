
y=str(input("enter the character:"))
x=""
for char in y:
   
   x+=str((ord(char)))
print(x)   
print()
print(len(x))

z=str(input("are you wanna go back to the original?\n"))
if z=="yes":
   y=""
   
   for i in range(0,(len(x)-1),2):
      w=x[i]+x[i+1]
      y+=chr(int(w))
   print(y)   
else:
   print("tata bye")
   

  
   
