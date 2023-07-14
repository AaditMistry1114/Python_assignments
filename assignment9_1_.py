from assignment9_2_ import Add,Sub,Mul,Div,FloorDiv,Exponent,Mod

# to raise error use Add.add(None,None)
#pass both arguments as None
choice = int(input('Enter your choice: '))
if choice == 1:
    Add.add(10,20) #Addition if choice is 1
elif choice == 2:
    Sub.sub(10,20) #Subtraction if choice is 2
elif choice == 3:
    Mul.mul(10,20) #Multiplication if choice is 3
elif choice == 4:
    Div.div(10,20) #Division if choice is 4
elif choice == 5:
    FloorDiv.floordivdiv(10,20) #Floor Division if choice is 5, for expected output in floor divison convert input to int 
elif choice == 6:
    Exponent.expo(10,20) #Exponent if choice is 6
elif choice == 7:
    Mod.mod(10,20) #Modulous if the choice is 7
else:
    print('incorrect choice ,the number chosen is',choice,'which is not available')





