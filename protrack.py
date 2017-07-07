"""Module of Protrack app"""

class Skill(object):
    """Skills class used to make objects"""
    def __init__(self, name):
        self.name = name
        self.progress = False


class Protrack:
    """Protrack class"""
    all_skills = []

    def add_skill(self, name_of_skill):
        """Method for adding a new skill"""
        skill1 = Skill(name_of_skill)
        self.all_skills.append(skill1)

    def learn_skill(self, name_of_skill):
        """Method for learning a new skill"""
        for obj in self.all_skills:
            if name_of_skill == obj.name:
                obj.progress = True

    def list_all_skills(self):
        """Method for listing all skills"""
        list_of_all_skills = []
        for obj in self.all_skills:
            list_of_all_skills.append(obj.name)
        return list_of_all_skills

    def list_done_skills(self):
        """Method for listing all done skills"""
        list_of_all_done_skills = []
        for obj in self.all_skills:
            if obj.progress:
                list_of_all_done_skills.append(obj.name)
        return list_of_all_done_skills

    def list_undone_skills(self):
        """Method for listing all undone skills"""
        list_of_all_undone_skills = []
        for obj in self.all_skills:
            if not obj.progress:
                list_of_all_undone_skills.append(obj.name)
        return list_of_all_undone_skills

    def show_progress(self):
        """Method for showing progress"""
        done_skills = []
        for obj in self.all_skills:
            if obj.progress:
                done_skills.append(obj)

        return (len(done_skills) / len(self.all_skills))*100
