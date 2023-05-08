# Lab1  Exercise #9 (Part 1)
#
# A program to compute the two roots of a quadratic equation.
#
# Import the math module to access function "math.sqrt()".

import math

A = float( input( "\nEnter the coefficient A: \n" ) )

B = float( input( "\nEnter the coefficient B: \n" ) )

C = float( input( "\nEnter the coefficient C: \n" ) )

print( "\nThe coefficients of the equation are:\n" )
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )

if A!=0:
    # ****Modify that program to compute the two roots of a quadratic equation, as described in the program comments. ****
    discriminant = (B**2)-(4*A*C)

    root1 = (-B + (((B**2)-(4*A*C))**0.5)) / (2*A)  # replace 0.0 with the quadratic formula to calculate the roots
    root2 = (-B - (((B**2)-(4*A*C))**0.5)) / (2*A)

    print( "\nThe roots of the equation:\n" )
    print( "  Root #1 = ", round(root1,2) )  # round the result to two decimal places before printing
    print( "  Root #2 = ", round(root2,2) )

else:
    print("\nIt has no roots \n A quadratic equation must have a non-zero coefficient for the squared term")