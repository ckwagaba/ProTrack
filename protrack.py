class Skill(object):
    def __init__(self, name):
        self.name = name
        self.progress = False


class Protrack(Skill):
    all_skills= []

    def add_skill(self, name_of_skill):
        skill1 = Skill(name_of_skill)
        self.all_skills.append(skill1)

    def learn_skill(self, name_of_skill):
        for obj in self.all_skills:
            if name_of_skill == obj.name:
                obj.progress = True

    def list_all_skills(self):
        for obj in self.all_skills:
            print(obj.name)


    def list_done_skills(self):
        for obj in self.all_skills:
            if obj.progress:
                print(obj.name)


    def list_undone_skills(self):
        for obj in self.all_skills:
            if not obj.progress:
                print(obj.name)

    def show_progress(self):
        pass