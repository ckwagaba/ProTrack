
# make a list to hold onto our items
skills_list = ["collaboration", "integrity"]
new_skill_list = []
studied_list = []

def add_skills(new_skill):
    # add new skills to our list
    new_skill_list.append(new_skill)
    print("You have added {} skills".format(len(new_skill_list)))
    skills_list.append(new_skill)


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


while True:
    # ask for new skills
    new_skill = input("Enter a new skill: ")

# be able to quit the app
    if new_skill == 'DONE':
        break
    # show the list of added skills
    elif new_skill == 'SHOW':
        show_list_of_added_skills()
        continue
    # enter a skill that has been studied
    elif new_skill == 'STUDIED':
        studied = input("Enter skills studied: ")
        add_studied(studied)
        continue
    # View studied skills
    elif new_skill == 'SEE STUDIED':
        show_list_of_studied()
        continue
    # view skills that have not been studied
    elif new_skill == 'NOT STUDIED':
        show_list_of_not_studied()
        continue
    # view user progress
    elif new_skill == 'PROGRESS':
        get_progress()
        continue

    add_skills(new_skill)
show_list_of_studied()
show_list_of_studied()
