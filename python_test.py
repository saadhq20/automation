import unittest
from selenium import webdriver
from NewDebatePage import *
from SubMenuText  import*
from Category import*


class CreateNew(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.debate.org/opinions/")


    def test_tc002(self):

        text = PageLinks(self.driver)

        self.assertEqual(text.getNewText(),"Newest", "Textual Error in 'Newest' filter")
        self.assertEqual(text.getPopText(),"Popular", "Textual Error in 'Popular' filter")
        self.assertEqual(text.getRUText(),"Recently Updated", "Textual Error in 'Recently Updated' filter")
        self.assertEqual(text.getMaText(),"Most Agreed", "Textual Error in 'Most Agreed' filter")
        self.assertEqual(text.getMDText(),"Most Disagreed", "Textual Error in 'Most Disagreed' filter")
        self.assertEqual(text.getUaText(),"Unanswered", "Textual Error in 'Unanswered' filter")

    def test_tc008(self):
        create = NewDebate(self.driver)
        error = ErrorMsgs(self.driver)
        create.getNewDebate()
        create.setNewDebate()
        self.assertEqual(error.ErrorOne(),"Please provide at least 3 words.", "Error Text for Question 1 missing")
        self.assertEqual(error.ErrorTwo(),"Required", "Error Text for Question 2 missing")
        self.assertEqual(error.ErrorThree(),"Required", "Error Text for Question 3 missing")


    def test_tc009(self):

        create = NewDebate(self.driver)
        cat = Category(self.driver)
        create.getNewDebate()
        create.FirstQ("What is life?")
        cat.getArts()
        create.GoogleImg("life")
        create.cancelNewDebate()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()