a = float(input("Enter the the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

#To confirm whether it is a side of the triangle or not
if a>=b+c or b>=a+c or c>=b+a or a<=0 or b<=0 or c<=0:
    print(f"the given numbers are not sides of a valid triangle")
    
else:
    #calculating semi-perimeter
    s = (a+b+c) / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    print(f"The area of the triangle is {area}")