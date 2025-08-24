# ATM Process 
Cardno = 12345
Cardpin = 1234
balance = 9050
action = 0
deposit = 0
withdraw = 0

Usercard = int(input("Enter the Usercard Number:\n"))
Userpin = int(input("Enter the Userpin Number:\n"))

if (Cardno == Usercard and Cardpin == Userpin):
    print("--User Validated, Please Select Action:--\n")

    print("Press 1. for Balance Enquiry:\n")

    print("Press 2. for Deposit:\n")

    print("Press 3. for Withdraw:\n")

    print("Press 4. for Mini Statement:\n")

    action = int(input("Please Choose, Which Action do you want to Work:\n\n"))
    if (action == 1):
        print("Your Balance is:", balance)
    elif(action == 2):
        deposit= int(input("Enter the Amount, How much you want to deposit:\n"))
        balance = balance + deposit
        print("Your Updated balance after deposit is:\n", balance)
    elif(action == 3):
        withdraw = int(input("Enter the Amount, How much you want to withdraw:\n"))
        if(withdraw > balance):
            print("You have Insufficient Balance:\n")
        else:
            balance = balance - withdraw
            print("Your updated Balance after Withdraw is:\n", balance)

    elif(action == 4):
        print("Your Bank Statement is present here:\n")
        print("Date         Transaction     Amount:\n")
        print("25/07/2025   Withdraw        1000.00\n")
        print("26/07/2025   Withdraw        2500.00\n")
        print("27/07/2025   ATM Charge      450.00\n")
        print("28/07/2025   Flipkart Shop   1500.00\n")
        print("29/07/2025   Jio Mart Shop   2000.00\n")

else:
    print("Your CardNo or Pin is wrong, Please try Again:\n")
    print("Thank You for Banking with us:\n")
    