import unittest
from protrack import Skill, Protrack


class ProtractTestCases(unittest.TestCase):
    def setUp(self):
        self.example1 = Protrack()

    def test_for_adding_skill(self):
        self.example1.add_skill('Collaboration')
        self.assertEqual( len(self.example1.all_skills), 1, msg="The skill is not being added")

    def test_for_learning_skill(self):
        self.example1.add_skill('Communication Skills')
        self.example1.learn_skill('Communication Skills')
        self.example1.learn_skill('Collaboration')
        print(self.example1.all_skills)
        self.assertTrue(all( obj.progress for obj in self.example1.all_skills), msg="The Learning function is not working")


