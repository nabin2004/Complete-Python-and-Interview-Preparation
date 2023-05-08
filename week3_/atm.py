print("*******WELCOME TO OUR BANK*******")

user_name=input(("Your name: "))

balance = 1000
op=True

while op: #student completes while loop
    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit:")
    choice = input("Please choose transactions:")
    if choice == "1": #user chooses 'deposit'
         #student completes while loop
        amount = float(input("Enter deposit amount: £"))
        balance += amount
        print("Deposit of £" + str(amount) + " successful.")

    elif choice == "2":
       #student completes while loop
        amount = float(input("Enter withdrawal amount: £"))
        if amount > balance:
            print("It is not possible to withdraw beyond the account balance.")
        else:
            balance -= amount
            print("Withdrawal of £" + str(amount) + " successful.")
        
    elif choice=="3":
        #student does this part too
        print("Your current balance is £" + str(balance))
      
    elif choice == "Q" or choice == "q":  #user chooses 'exit'
        
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op= False #student does this part too
    else:
        print("Wrong transaction! Try again.")