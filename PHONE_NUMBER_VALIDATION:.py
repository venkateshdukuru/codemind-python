import re # Importing re module
n=input()  # Reading input from the user
r=re.fullmatch('[6-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
if r!=None: # checking whether it is none or not 
     print('Valid')
else:
     print('Invalid')