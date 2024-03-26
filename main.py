from datetime import time

print("welcome to safaricom mpesa app")
print("1. send money")
print("2. withdraw cash")
print("3. loans and savings")
print("4. lipa na mpesa")
print("5. my account")



def spin():
    max_att = 3
    while max_att < 3:
        pinc()
    else:
        print("maximum amount reached terminating process")
        quit()
def pinc():
    p = "1234"
    max_att = 3
    s = input("enter pin: ")
    if s == p:
        pass
    else:
        print("incorrect pin")
        quit()
def pre():
    print("press 1 to accept and 2 to decline")
    ans = input("enter option: ")
    if ans == "1":
         pass
    else:
        quit()

choice = int(input("enter option: "))
if choice == 1:
    print("send money")
    num = input("enter number: ")
    amnt = input("enter amount: ")
    print("send money to", num , "ksh ", amnt, "?")
    pre()

    #pin = input("enter pin: ")
    pinc()
    print("confirmed ksh", amnt, "sent to", num, "at this time")
    #include system produced time

if choice == 2:
    print("option selected is withdraw cash")
    print("1. from agent no")
    print("2. from atm")
    opt = input("enter option: ")
    if opt := 1:
        print("option selected is from agent no")
        agent_no = input("enter agent no: ")
        withd = input("enter amount to withdraw: ")
        print("withdraw ksh", withd, "from no", agent_no, "?")
        pre()
        pinc()
        print("confirmed withdraw", withd, "from agent no", agent_no)
        #recompose this message with systm generated time included.
if choice == 3:
    print("option selected is loans and savings")
    print("1. mshwari")
    print("2. kcb bank")
    m1 = input("enter option: ")
    if m1 := 1:
        print("option selected is mshwari")
        print("1. send to mshwari")
        print("2. withdraw from mshwari")
        print("3. lock savings")
        print("4. check balance")
        print("5. mini statement")
        m2 = input("enter option: ")
        if m2 == "1":
            mamnt = int(input("enter amount: "))
            pre()
            pinc()
            print("confirmed ksh", mamnt, "sent to mshwari on", time,"new mshwari balance is", mamnt )
            quit()
        if m2 == "2":
            #remember to solve this problem tommorow
            wms = input("enter amount: ")
           #bal = mamnt
            pre()
            pinc()
            print("confirmed withdraw ksh: ", wms)
        if m2 == "3":
            print("option selected is lock saving account")
            print("open lock savings account")
            print("1. save")
            print("2. withdraw")
            print("3. check balance")
            print("4. mini statement")
            op1 = input("enter option: ")
            if op1 == "1":
                print("1. from mpesa")
                print("2. from mshwari")
                target = input("enter target: ")
                print("enter period")
                period = input("enter period: ")
                samnt = input("enter amount to save: ")
                pre()
                pinc()
                print("confirmed ksh", samnt, "has been moved from mpesa to lock savings")
                quit(3)

            if op1 == "2":
                want = input("enter amount to withdraw: ")
                pre()
                pinc()
                print("confirmed ksh", want, "has been withdrawn from mshwari")
                #remember to include bal after withdrawal and also figure out how to include bal from above to be used below
            if op1 == "3":
                print("under construction will soon work")
                quit()
        if m2 == "4":
            print("option selected is loan")
            print("1. request loan")
            print("2. pay loan")
            print("3. check loan limit")
            print("4. check loan balance")
            l1 = input("enter option: ")
            if l1 == "1":
                a1 = input("enter amount: ")
                pre()
                pinc()
                print("this amount", a1, "has been advanced as a loan")
            if l1 == "2":
                l2 == input("enter amount: ")
                pre()
                pinc()
                print("am working on this")
                #dont leave this part alone just look for a way to fix it
                quit()
            if l1 == "3":
                pre()
                pinc()
                print("you  don't have a loan limit save more on mshwari to grow your loan limit")
            if l1 == "4":
                pre()
                pinc()
                print("you dont have a loan balance. request for a loan to have a loan limit")
        if m2 == "5":
            pre()
            pinc()
            print("your mshwari balance is ksh ")
            #remember to work on this5
    if choice == "4":
        print("option selected is lipa na mpesa")
        print("1. pay bill")
        print("2. buy goods and services")
        print("3. pochi la biashara")
        f1 = input("enter option")
        if f1  == "1":
            pb = input("enter paybill no: ")
            pamnt = input("enter amount to pay")
            pre()
            pinc()





