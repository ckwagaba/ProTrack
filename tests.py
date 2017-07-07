import unittest
from protrack import Skill, Protrack


class ProtractTestCases(unittest.TestCase):
    def setUp(self):
        self.example1 = Protrack()


    def test_for_adding_skill(self):
        self.example1.add_skill('Collaboration')
        self.assertEqual( len(self.example1.all_skills), 1, msg="The skill is not being added")
