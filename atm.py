# ATM Mini Project 

balance = 10000
pin = "1234"

entered_pin = input("Enter ATM PIN: ")

if entered_pin == pin:
   
   while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")   
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Current Balance: ₹", balance)   

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹")) 
        balance += amount
        print("Deposited Successful!.")
        print("New Balance: ₹", balance)


    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹")) 

        if amount <= balance:
           balance -= amount
           print("Please collect your cash.")
           print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":  
        print("Thank you for using the ATM!")
        break  

    else:   
        print("Invalid choice! Please try again.")   

else:
    print("Incorrect PIN!")            

            
