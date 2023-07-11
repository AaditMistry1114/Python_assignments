#Aadit

my_list = list()

my_list = [12,65,232,21,64]
print(sum(my_list)) # Sum of numbers

print(min(my_list)) #Minimum of numbers

print(max(my_list)) #Maximum of numbers

my_list.sort() # Ascending numbers
print(my_list)

my_list.sort(reverse=True) #Descending numbers
print(my_list)

my_tuple = tuple(my_list) #conversion of list to tuple
print(my_tuple)

#output
# 394
# 12
# 232
# [12, 21, 64, 65, 232]
# [232, 65, 64, 21, 12]
# (232, 65, 64, 21, 12)

