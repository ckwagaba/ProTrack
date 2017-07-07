
skl = Protrack()
    
print (30 * '-')
print ("   P R O T R A C                  ")
print (30 * '-')
print ("1. Add Skill")
print ("2. Show Progress")
print ("3. Show All Available Skills")
print (30 * '-')
 

choice = input('Enter your choice [1-3] : ')

 

choice = int(choice)
 

if choice == 1:
    skl.add_skill()
elif choice == 2:
    print ("Show progress Method will go here")
elif choice == 3:
    print ("Show Available method will go here")
else:
    print ("Invalid number. Try again...")
