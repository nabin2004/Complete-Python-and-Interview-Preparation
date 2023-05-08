
#taking five input
num_1=float(input("Enter the number "))
num_2=float(input("Enter the number "))
num_3=float(input("Enter the number "))
num_4=float(input("Enter the number "))
num_5=float(input("Enter the number "))

#mean ccalculation
mean=(num_1 + num_2 + num_3 + num_4 + num_5) /5

#Variance calculation
variance = (((num_1 - mean)**2 +(num_2-mean)**2 + (num_3-mean)**2 + (num_4-mean)**2 + (num_5-mean)**2)/5)

#Standard deviation calculating
std_devi = variance ** 0.5

#printing result
print(f"Population standard deviation is : {std_devi}")
