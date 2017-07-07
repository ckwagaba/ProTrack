skills_list = ["collaboration", "integrity"]
new_skill_list = []
studied_list = []

def add_skills(new_skill):
	# add new skills to our list
	new_skill_list.append(new_skill)
	print("You have added {} skills".format(len(new_skill_list)))
	new_skill_list.append(new_skill)
def show_list_of_added_skills():
	# print out the list
	print("Here is your list of added skills: ")
	print(new_skill_list)
	for item in new_skill_list:
		print(item)
def add_studied(studied):
	# add skills studied
	studied_list.append(studied)
	print("You have studied {} skills".format(len(studied_list)))
def show_list_of_studied():
	# show list of skills studied
	print("Here is your list of studied skills: ")
	for item in studied_list:
		print(item)
def show_list_of_not_studied():
	# show list of skills not studied
	print("Here is your list of skills that you are yet to study: ")
	asy_difference_set = set(skills_list).symmetric_difference(set(studied_list))
	asy_difference_list = list(asy_difference_set)
	if len(asy_difference_list) > 0:
		for item in asy_difference_list:
			print(item)
def get_progress():
	# get user progress
	study_length = len(studied_list)
	skills_length = len(skills_list)
	progress = (study_length/skills_length)*100
	print(progress)
	return progress
def interface():
    while True:
        new_skill = input("Enter a new skill: ")
        if new_skill == 'DONE':
            break
        elif new_skill == 'SHOW':
            show_list_of_added_skills()
            continue
        elif new_skill == 'NOT STUDIED':
            show_list_of_not_studied()
            continue
        elif new_skill == 'PROGRESS':
            get_progress()
            continue
        elif new_skill == 'STUDIED':
            studied = input("Enter skills studied: ")
            add_studied(studied)
            continue
        elif new_skill == 'SEE STUDIED':
            show_list_of_studied()
            continue
        add_skills(new_skill)
        show_list_of_studied()
        show_list_of_studied()


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
        interface()
elif choice == 2:
        print ("Show progress Method")
elif choice == 3:
        print ("Show Available method")
else:    ## default ##
        print ("Invalid number. Try again...")
