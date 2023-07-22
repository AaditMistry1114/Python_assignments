balance = 10000
def withdraw_money(): #this function is used to withdraw money 
    print('Enter an Amount to withdraw: ')
    wtd_money = int(input('Amount: '))
    if wtd_money > 0:
        current_balance = (balance - wtd_money)
        print('Amount withdrawed successfully !!!')
        print('Withdrawed amount: ',wtd_money)
        print('Current Balance',current_balance)
    
        