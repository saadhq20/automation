from selenium.common.exceptions import NoSuchElementException
class PageLinks(object):

    def __init__(self, driver):
        self.driver = driver

    def getNewText(self):
        try:
            new = self.driver.find_element_by_xpath('//a[contains(text(),"Newest")]').text
            return new
        except NoSuchElementException:
            print("Error in 'Newest' text")

    def getPopText(self):
        try:
            pop = self.driver.find_element_by_xpath('//a[contains(text(),"Popular")]').text
            return pop
        except NoSuchElementException:
            print("Error in 'Popular' text")

    def getRUText(self):
        try:
            ru = self.driver.find_element_by_xpath('//a[contains(text(),"Recently Updated")]').text
            return ru
        except NoSuchElementException:
            print("Error in 'Recently Updated' text")

    def getMaText(self):
        try:
            ma = self.driver.find_element_by_xpath('//a[contains(text(),"Most Agreed")]').text
            return ma
        except NoSuchElementException:
            print("Error in 'Most Agreed' text")

    def getMDText(self):
        try:
            md = self.driver.find_element_by_xpath('//a[contains(text(),"Most Disagreed")]').text
            return md
        except NoSuchElementException:
            print("Error in 'Most Disagreed' text")

    def getUaText(self):
        try:
            ua = self.driver.find_element_by_xpath('//a[contains(text(),"Unanswered")]').text
            return ua
        except NoSuchElementException:
            print("Error in 'UnAnswered' text")

