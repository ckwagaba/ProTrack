'''This is the ProTrack module which adds skills, gets skills studied, skills
not studied and progress'''
from __future__ import division
class ProTrack(object):
    '''This is the class that holds all our functions'''
    def __init__(self):
        #we are getting the total number of skills and the skill name
        get_skills = raw_input("How many skills are there?\n")
        skills = int(get_skills)
        count_skills = 0
        self.skills_list = []
        num_of_skills = skills
        while num_of_skills > count_skills:
            name_of_skills = raw_input("Please input skill {0}\n".format(count_skills + 1))
            self.skills_list.append(name_of_skills)
            count_skills += 1
        #We are getting the number of skills studied by the user and the skill name
        get_skills_studied = raw_input("Hello, How many skills Have you studied?\n")
        skills = int(get_skills_studied)
        count_skills = 0
        self.studied_skills_list = []
        num_of_skills_studied = skills
        #checking if the number of skills input by user equals the total number of skills studied
        while num_of_skills_studied > count_skills:
            name_of_skills = raw_input("Please input skill {0}\n".format(count_skills + 1))
            if name_of_skills == 0:
                print("You have not yet studied any skill")

            self.studied_skills_list.append(name_of_skills)
            count_skills += 1

    def not_studied_skills(self):
        '''This function generates a list of skills not yet studied by the user'''
        all_skills = self.skills_list
        studied = self.studied_skills_list
        subjects = set(all_skills)-set(studied)
        if self.studied_skills_list == []:
            exit()
        else:
            return "This is/are the skill(s) you have not studied:\n" + str(list(subjects)) + "\n"

    def studied_skills(self):
        '''This functions generates a list of the skills studied by user'''
        if self.studied_skills_list == []:
            return "You have not studied any of these skills below:\n" + str(self.skills_list) + "\n" + self.get_progress(0,0)
        else:
            return "These are the skills you have studied:\n" + str(self.studied_skills_list) + "\n"


    def get_progress(self, total_skills, finished_skills):
        '''This function gets the users progress basing on the number of skills completed
        compared to total number of skills'''
        total_skills = len(self.skills_list)
        finished_skills = len(self.studied_skills_list)
        print "Your total Progress is: " + "{:.0%}".format(finished_skills/total_skills) + "\n"
        exit()



access_skills = ProTrack()
print access_skills.studied_skills()
print access_skills.not_studied_skills()
print access_skills.get_progress(0, 0)
