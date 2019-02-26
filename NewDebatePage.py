from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class NewDebate(object):

    def __init__(self, driver):
        self.driver = driver

    def getNewDebate(self):
        self.driver.find_element_by_id("postButton").click()

    def setNewDebate(self):
        self.driver.find_element_by_xpath('//button[@id="popSubmitButton"]').click()

    def cancelNewDebate(self):
        self.driver.find_element_by_id("popCancelButton").click()

    def FirstQ(self, question):
        self.driver.find_element_by_id("question").send_keys(question)

    def GoogleImg(self, image):
        self.driver.find_element_by_id("googTab").click()
        self.driver.find_element_by_class_name("searchMore").send_keys(image)
        self.driver.find_element_by_xpath('//a[@class="search-for button2 button-gray"]').click()

    #def SecQ(self, question):

class ErrorMsgs(object):

    def __init__(self, driver):
        self.driver = driver

    def ErrorOne(self):
        try:
            e1 = self.driver.find_element_by_xpath('//span[contains(text(),"Please provide at least 3 words.")]').text
            return e1
        except NoSuchElementException:
            print("Wrong/Missing text")

    def ErrorTwo(self):
        try:
             e2 = self.driver.find_element_by_xpath('//span[@class="error"][contains(text(),"Required")]').text
             return e2
        except NoSuchElementException:
             print("Wrong/Missing text")

    def ErrorThree(self):
        try:
             e3 = self.driver.find_element_by_xpath('//div[contains(text(),"3. Add an Image")]//span[@class="error"][contains(text(),"Required")]').text
             return e3
        except NoSuchElementException:
              print("Wrong/Missing Text")

