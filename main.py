from datetime import datetime
import random
import string


def generate_code():
    """Generates a random 8-character alphanumeric code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
trcode = generate_code()

def change_pin():
    if validate_pin():
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            baldict["pin"] = new_pin
            print("PIN updated successfully.")
        else:
            print("Entered PINs do not match. Please try again.")
    else:
        print("PIN validation failed.")
    print(f"Current stored PIN: {baldict['pin']}")


baldict = {
    "balances": 2000,
    "mbal": 2000,
    "pin": "1234" 
}


def transaction(amount, action="withdraw"):
   
    if action == "withdraw":
        if amount > baldict["balances"]:
            print("Insufficient funds!")
            return
        baldict["balances"] -= amount
        print(f"You have withdrawn {amount}. New balance: {baldict['balances']}")
    elif action == "deposit":
        baldict["balances"] += amount
        print(f"You have deposited {amount}. New balance: {baldict['balances']}")
    else:
        print("Invalid transaction type.")


print("1. send money")
print("2. withdraw cash")
print("3. loans and savings")
print("4. lipa na mpesa")
print("5. my_acount")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_pin():
    max_att = 3
    for attempt in range(max_att):
        s = input("Enter PIN: ")
        print(f"Validating PIN: {s} against stored PIN: {baldict['pin']}")
        if s == baldict["pin"]:
            return True
        else:
            print(f"Incorrect PIN. {max_att - attempt - 1} attempts left.")
    print("Maximum attempts reached. Exiting.")
    return False

    return False
def sendmoney():
    print("Send money")
    num = input("Enter number: ")
    amnt = input("Enter amount: ")
    print(f"Send Ksh {amnt} to {num}?")
    pre()
    validate_pin()
    
    print(f"{trcode} - Confirmed: Ksh {amnt} sent to {num} at {current_time}")


def withdraw():
    print("Option selected is withdraw cash")
    print("1. From agent number")
    print("2. From ATM")
    opt = input("Enter option: ")
    if opt == "1":
        print("Option selected is from agent number")
        agent_no = input("Enter agent number: ")
        withd = input("Enter amount to withdraw: ")
        print(f"Withdraw Ksh {withd} from agent number {agent_no}?")
        pre()
        validate_pin()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{trcode} - Confirmed: Ksh {withd} withdrawn from agent number {agent_no} on {current_time}")
    elif opt == "2":
        print("Option selected is from ATM")
        agent_no = input("Enter ATM number: ")
        withd = input("Enter amount to withdraw: ")
        print(f"Withdraw Ksh {withd} from ATM number {agent_no}?")
        pre()
        validate_pin()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{trcode} - Confirmed: Ksh {withd} withdrawn from ATM number {agent_no} on {current_time}")
    else:
        print("Invalid option")
        quit()
def loans():
    print("Option selected is loans and savings")
    print("1. Mshwari")
    print("2. KCB bank")
    m1 = input("Enter option: ")
    if m1 == "1":
        print("Option selected is Mshwari")
        print("1. Send to Mshwari")
        print("2. Withdraw from Mshwari")
        print("3. Lock savings")
        print("4. Check balance")
        print("5. Mini statement")
        m2 = input("Enter option: ")
        if m2 == "1":
            mamnt = int(input("Enter amount: "))
            pre()
            validate_pin()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{trcode} - Confirmed: Ksh {mamnt} sent to Mshwari on {current_time}")
        elif m2 == "2":
            wms = input("Enter amount: ")
            pre()
            validate_pin()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{trcode} - Confirmed: Ksh {wms} withdrawn from Mshwari, at {current_time}")
        elif m2 == "3":
            print("Lock savings option selected")
            print("Saving is in progress...")
            pre()
            validate_pin()
        else:
            print("Invalid option")
            quit()
def lipa():
    print("Option selected is lipa na mpesa")
    print("1. Pay bill")
    print("2. Buy goods and services")
    f1 = input("Enter option: ")
    if f1 == "1":
        pb = input("Enter paybill number: ")
        pamnt = input("Enter amount to pay: ")
        pre()
        validate_pin()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{trcode} - Confirmed: Ksh {pamnt} paid to paybill number {pb} , at {current_time}")
    else:
        print("Invalid option")

    if f1 == "2":
        print("option selected is buy goods and services")
        bill = input("enter bill no: ")
        bill_amount = input("enter amount to send: ")
        print(f"would you like to send", bill_amount, "to", bill, "?") 
        pre()
        validate_pin()
        print(f"{trcode} - confirmed ksh {bill_amount}, sent to {bill}, on {current_time}")
def my_acc():
    print("1. mini statement")
    print("2. check balance")
    print("3. check pin")
    choosing = input("enter option: ")
    if choosing == "1":
        print("this option is under maintainance please wait. you will be notified when it is available.")
    if choosing == "2":
        print(f"{trcode}, confirmed you balance is ksh: {baldict["balances"]}, at {current_time}")
    if choosing == "3":
        change_pin()
def pre():
    print("Press 1 to accept and 2 to decline")
    ans = input("Enter option: ")
    if ans == "1":
        pass
    else:
        print("Invalid option")
        quit()

choice = int(input("Enter option: "))


if choice == 1:
     sendmoney()
    

elif choice == 2:
    withdraw()

elif choice == 3:
   loans()

elif choice == 4:
    lipa()
if choice == 5:
    my_acc()