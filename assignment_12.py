#Aadit
import ATM.module1 as a1
import ATM.module2 as a2
import ATM.module3 as a3
import ATM.module4 as a4
import ATM.module5 as a5

balance = 10000  #global amount is used for balance
while True:
    print('--------ATM Management System--------')
    print('1.PIN')
    print('2.Balance')
    print('3.Withdraw money')
    print('4.Save money') 
    print('5.Exit')

    try:
        choice = int(input('Enter Your Choice: '))
        if choice == 1: #module 1
                a1.pin()
        if choice == 2: #module 2
                a2.balance_amount()
        if choice == 3: #module 3
                a3.money_saving()
        if choice == 4: #module 4
                a4.withdraw_money()
        if choice == 5: #module 5
                a5.exit_()
    except Exception as e:
        print('Ivalid choice') #if number is not within 1 - 5 exception is raised