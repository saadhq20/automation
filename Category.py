from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
class Category(object):
    def __init__(self, driver):
        self.driver = driver

    def getArts(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Arts")]').click()
        except NoSuchElementException:
            print('Arts Category is missing')

    def getCars(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Cars")]').click()
        except NoSuchElementException:
             print('Cars Category is missing')

    def getEconomics(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Economics")]').click()
        except NoSuchElementException:
            print('Economics Category is missing')


    def getEducation(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Education")]').click()
        except NoSuchElementException:
            print('Education Category is missing')

    def getEntertainment(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Entertainment")]').click()
        except NoSuchElementException:
            print('Entertainment Category is missing')

    def getFashion(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Fashion")]').click()
        except NoSuchElementException:
            print('Fashion Category is missing')

    def getFunny(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Funny")]').click()
        except NoSuchElementException:
            print('Funny Category is missing')

    def getGames(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Games")]').click()
        except NoSuchElementException:
            print('Games Category is missing')

    def getHealth(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Health")]').click()
        except NoSuchElementException:
            print('Health Category is missing')

    def getMiscellaneous(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Miscellaneous")]').click()
        except NoSuchElementException:
            print('Miscellaneous Category is missing')


    def getMovies(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Movies")]').click()
        except NoSuchElementException:
            print('Movies Category is missing')

    def getMusic(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Music")]').click()
        except NoSuchElementException:
            print('Music Category is missing')

    def getNews(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"News")]').click()
        except NoSuchElementException:
            print('News Category is missing')

    def getPeople(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"People")]').click()
        except NoSuchElementException:
            print('People Category is missing')

    def getPhilosophy(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Philosophy")]').click()
        except NoSuchElementException:
            print('Philosophy Category is missing')

    def getPlaces(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Places-Travel")]').click()
        except NoSuchElementException:
            print('Movies Category is missing')

    def getPolitics(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Politics")]').click()
        except NoSuchElementException:
            print('Politics Category is missing')

    def getReligion(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Religion")]').click()
        except NoSuchElementException:
            print('Religion Category is missing')

    def getScience(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Science")]').click()
        except NoSuchElementException:
            print('Science Category is missing')

    def getSociety(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Society")]').click()
        except NoSuchElementException:
            print('Society Category is missing')


    def getSports(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Sports")]').click()
        except NoSuchElementException:
            print('Sports Category is missing')

    def getTechnology(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"Technology")]').click()
        except NoSuchElementException:
            print('Technology Category is missing')

    def getTV(self):
        try:
            self.driver.find_element_by_xpath('//span[contains(text(),"TV")]').click()
        except NoSuchElementException:
            print('TV Category is missing')