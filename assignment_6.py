#Aadit
def ds(roll_no, name):
  
  # List
  lst = [roll_no, name]
  print("List:", lst)

  # Tuple
  tup = (roll_no, name)
  print("Tuple:", tup)

  # Set
  st = {roll_no, name}
  print("Set:", st)

  # Dictionary
  dct = {"roll_no": roll_no, "name": name}
  print("Dictionary:", dct)

  
  # List
  lst[0] = roll_no + 1 
  lst[1] = name = ('hello')
  print("Modified list:", lst)
  
  # Tuple
  name = 'Bye'
  tup = (roll_no + 2, name) # Create a new tuple with modified values
  print("Modified tuple:", tup)
  
  # Set
  st.remove(roll_no) 
  st.add(roll_no + 3) 
  print("Modified set:", st)
  
  # Dictionary
  dct["roll_no"] = roll_no + 4 
  dct["name"] = name[-1]  
  print("Modified dictionary:", dct)

  # Delete these data structures
  del lst, tup, st, dct


ds(114, "Aadit")
