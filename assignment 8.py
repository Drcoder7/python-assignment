a=int(input("enter first numbers"))
b=int(input("enter second numbers"))
c=int(input("enter third numbers"))
print(a,b,c)
if(a<=b and a<=c):
    print(a,"is the smallest")

elif(b<=a and b<=c):
    print(b,"is thhe smalleest")

else:
  print(c,"is the smallest")
