First_Name = input('Please enter your first name:')
Last_Name = input('Please enter your last name:')
Greeting = 'Hello,'

Length_Of_Greeting = len(Greeting)
Length_Of_First_Name = len(First_Name)
Length_Of_Last_Name = len(Last_Name)
Max_Length = max(Length_Of_Greeting,Length_Of_Last_Name,Length_Of_First_Name)

print('***','*'*Max_Length,'***', sep='')
print('**',Greeting+' '*(Max_Length - Length_Of_Greeting) ,'**')
print('**',First_Name+' '*(Max_Length - Length_Of_First_Name),'**')
print('**',Last_Name+' '*(Max_Length - Length_Of_Last_Name),'**')
print('***','*'*Max_Length,'***', sep='')