"""Module for the tests of PROTRACK"""
import unittest
from protrack import Protrack


class ProtractTestCases(unittest.TestCase):
    """TestCases for PROTRACK application"""
    def setUp(self):
        self.example1 = Protrack()

    def test_for_adding_skill(self):
        """Test for adding a skill"""
        self.example1.add_skill('Collaboration')
        self.assertEqual(len(self.example1.all_skills), 1,
                         msg="The skill is not being added")

    def test_for_learning_skill(self):
        """Test for checking if skill was learnt"""
        self.example1.add_skill('Communication Skills')
        self.example1.learn_skill('Communication Skills')
        self.example1.learn_skill('Collaboration')
        print(self.example1.all_skills)
        self.assertTrue(all(obj.progress for obj in self.example1.all_skills),
                        msg="The Learning function is not working")

    def test_list_of_all_skills(self):
        """Test for returning all the skills"""
        self.assertEqual(len(self.example1.list_all_skills()), 2,
                         msg="This is not being returned correctly")

    def test_list_of_all_done_skills(self):
        """Test for checking done skills"""
        self.assertEqual(len(self.example1.list_done_skills()), 2,
                         msg="List of done skills not being returned correctly")

    def test_list_of_all_undone_skills(self):
        """Test for checking undone skills"""
        self.assertEqual(len(self.example1.list_undone_skills()), 0,
                         msg="List of undone skills not being returned correctly.")

    def test_for_progress(self):
        """Test for checking for progress"""
        self.assertEqual(self.example1.show_progress(), 100,
                         msg="The progress is incorrect.")
