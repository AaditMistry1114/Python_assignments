#Aadit 

def file_function(file='assignment.txt'):
    try:
        f = open(file,'+a')
        f.writelines(input('Enter your name: '))
        f.writelines(input('Enter your roll no : '))
        f.writelines(input('Enter your class: '))
        f.seek(0)
        print(f.readlines())

    except IOError:
        print('Incomplete Details')

file_function()

#output
# Enter your name: aadit 
# Enter your roll no : 114 
# Enter your class: b 
# ['aadit 114 b ']