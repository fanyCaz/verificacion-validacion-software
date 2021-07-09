def f(x):
  return 
  return 1/(x**1.1)

a = float(input("what is your starting point?"))
b = float(input("where do you want to end"))

n = int(input("how many intervals do you want?"))

width = (b-a)/n
print("width of one interval=", width)

i = 0
Area = 0

while(i<= (n-1)):
  Area = f(b+width*i)*width + Area
  i=(i+1)

print("The approximate area is = ", Area)
