#author Erik Smith
#build an ATM task
current_account_balance = 2000
saving_account_balance = 10000
options_menu = ["Option 1 see current account balance", "Option 2 see savings account balance", "Option 3 withdraw money"]

print ("please insert your card")
entered_pin_num = int(input("please enter your pin number"))

while entered_pin_num != 1234:
    print("The pin number is incorrect, try again")
    entered_pin_num = int(input("please enter your pin number"))

while True: 
    print("What would you like to do?")  

    for option in options_menu:
        print(option)

    user_choice = int(input("please select what you would like to do?"))

    if user_choice == 1:
        print ("Current account balance:", current_account_balance)
    elif user_choice == 2:
         print("Savings account balance:", saving_account_balance)
    elif user_choice == 3:
         withdraw_amount = int(input("How much would you like to withdraw?"))
         if withdraw_amount <= current_account_balance:
             current_account_balance -= withdraw_amount
             print ("Your", withdraw_amount, "cash is being withdrawn") 
             print ("Your current account balance is now" , current_account_balance)
             print ("please take your cash")
         else:
             print ("it cannot proceed as the amount is more than the cash in your account")
    else: 
        print("Invalid option, please choose again")

    return_to_menu = input("Would you like to return to the main menu? (yes/no) ")
    if return_to_menu.lower() != "yes":
     print("Please take your card.")
     break
    
