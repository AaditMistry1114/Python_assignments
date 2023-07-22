balance = 10000
def money_saving(): #this function is used to add amount you want to save    
    print('Enter amount for savings')
    savings = int(input('Amount: '))
    after_saving_amt = (balance + savings)
    print('After saving your balance: ',after_saving_amt)
