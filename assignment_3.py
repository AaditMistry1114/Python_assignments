#Aadit
#Calulator for all the Arithmetic Operators

number1 = float(input('Enter first number:'))
number2 = float(input('Enter Second number:'))

choice = int(input('Enter your choice:'))

if choice == 1:
    print(number1 + number2) #Addition if choice is 1
elif choice == 2:
    print(number1 - number2) #Subtraction if choice is 2
elif choice == 3:
    print(number1 * number2) #Multiplication if choice is 3
elif choice == 4:
    print(number1 / number2) #Division if choice is 4
elif choice == 5:
    print(number1 // number2) #Floor Division if choice is 5, for expected output in floor divison convert input to int 
elif choice == 6:
    print(number1 ** number2) #Exponent if choice is 6
elif choice == 7:
    print(number1 % number2) #Modulous if the choice is 7
else:
    print('incorrect choice ,the number chosen is',choice,'which is not available')

#Output 
'''
(choice == 1)
Enter first number:10
Enter Second number:20
Enter your choice:1
30.0

(choice == 2)
Enter first number:30
Enter Second number:20
Enter your choice:2
10.0

(choice == 3)
Enter first number:10
Enter Second number:10
Enter your choice:3
100.0

(choice == 4)
Enter first number:100
Enter Second number:10
Enter your choice:4
10.0

(choice == 5)
Enter first number:124
Enter Second number:13
Enter your choice:5
9.0

(choice == 6)
Enter first number:2
Enter Second number:3
Enter your choice:6
8.0

(choice == 7)
Enter first number:10
Enter Second number:2
Enter your choice:7
0.0

(choice == 8)
Enter first number:114
Enter Second number:12
Enter your choice:8
incorrect choice ,the number chosen is 8 which is not available
'''

