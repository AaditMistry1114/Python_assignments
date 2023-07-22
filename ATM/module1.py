def pin():
   name = input('Enter your name: ')
   pin_no = int(input('Enter your pin no: '))
   if name == 'aadit' and pin_no == 123:
      f = open('details.txt','+at') #to store user name and pin_no in details.txt
      f.write('Welcome User !!\n')
      f.write(f'\n Name: {name}\n Pin no: {pin_no} \n')
   else:
      print('Invalid User Details')

    