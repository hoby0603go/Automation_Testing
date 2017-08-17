# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class test_explore(unittest.TestCase):

    def setUp(self):
        self.KKBOX = webdriver.Chrome()
        self.KKBOX.maximize_window()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.get("https://play.kkbox.com")
        account = "andrew.hsu0603@gmail.com"
        self.KKBOX.implicitly_wait(10)
        inputElement = self.KKBOX.find_element_by_id("uid")
        inputElement.send_keys(account)
        password = "kkboxtest"
        inputElement = self.KKBOX.find_element_by_id("pwd")
        inputElement.send_keys(password) 
        self.KKBOX.find_element_by_id("login-btn").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_link_text("線上精選").click()
        
    def tearDown(self):
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-user-dropdown").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("a[ng-click='app.logout()']").click()
        self.KKBOX.quit()

    def test_prereleasemode(self): #4
        self.KKBOX.implicitly_wait(10)
        prerelease = self.KKBOX.find_element_by_css_selector("div[context-menu='right-main-preReleaseMode'] div[class='img-wrap']")
        play_btn = self.KKBOX.find_element_by_css_selector("a[analytics-category='Explore_PreRelease']")
        ActionChains(self.KKBOX).move_to_element(prerelease).click(play_btn).perform()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()

    def test_focusplaylists(self): #2
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("li[ng-repeat='special in explore.specials | limitTo: 6']").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-40-headerplay").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()
       
    def test_top1(self): #5
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-32-crown").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-28-b-play").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()

    def test_newrelease(self): #3
        self.KKBOX.implicitly_wait(10)
        newrelease = self.KKBOX.find_element_by_css_selector("div[context-menu='right-main-newReleaseMode'] div[class='img-wrap']")
        play_btn = self.KKBOX.find_element_by_css_selector("a[analytics-category='Explore_NewRelease']")
        ActionChains(self.KKBOX).move_to_element(newrelease).click(play_btn).perform()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()

    def test_famousplaylists(self): #1
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("li[ng-repeat='playlist in explore.famousPlaylists']").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-40-headerplay").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()


class test_mylibrary(unittest.TestCase):

    def setUp(self):
        self.KKBOX = webdriver.Chrome()
        self.KKBOX.maximize_window()
        self.KKBOX.get("https://play.kkbox.com")
        account = "andrew.hsu0603@gmail.com"
        self.KKBOX.implicitly_wait(10)
        inputElement = self.KKBOX.find_element_by_id("uid")
        inputElement.send_keys(account)
        password = "kkboxtest"
        inputElement = self.KKBOX.find_element_by_id("pwd")
        inputElement.send_keys(password) 
        self.KKBOX.find_element_by_id("login-btn").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_link_text("我的音樂庫").click()

    def tearDown(self):
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-user-dropdown").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("a[ng-click='app.logout()']").click()
        self.KKBOX.quit()
        
    def test_myplaylists(self): #6
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_link_text("test").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-40-headerplay").click()
        time.sleep(3)
        self.KKBOX.find_element_by_css_selector("i.icon-32-next").click()
        time.sleep(3)
        self.KKBOX.find_element_by_css_selector("i.icon-32-prev").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()
        

class test_search(unittest.TestCase):

    def setUp(self):
        self.KKBOX = webdriver.Chrome()
        self.KKBOX.maximize_window()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.get("https://play.kkbox.com")
        account = "andrew.hsu0603@gmail.com"
        self.KKBOX.implicitly_wait(10)
        inputElement = self.KKBOX.find_element_by_id("uid")
        inputElement.send_keys(account)
        password = "kkboxtest"
        inputElement = self.KKBOX.find_element_by_id("pwd")
        inputElement.send_keys(password) 
        self.KKBOX.find_element_by_id("login-btn").click()
        self.KKBOX.implicitly_wait(10)
        inputElement = self.KKBOX.find_element_by_css_selector("input.search_hint")
        inputElement.send_keys(u"林俊傑")
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-search").click()

    def tearDown(self):
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-user-dropdown").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("a[ng-click='app.logout()']").click()
        self.KKBOX.quit()
    
    def test_singer(self): #9
        self.KKBOX.implicitly_wait(10)
        singer = self.KKBOX.find_element_by_css_selector("li[ng-repeat='artist in ::search.artists | limitTo:5 track by artist.artist_id'] div[class='cover'] div[class='img-wrap']")
        singer.click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon.icon-28.icon-28-b-play").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()
        
    def test_album(self): #7
        self.KKBOX.implicitly_wait(10)
        album = self.KKBOX.find_element_by_css_selector("div[context-menu='right-main-albumMode'] div[class='img-wrap']")
        play_btn = self.KKBOX.find_element_by_css_selector("a[analytics-category='Search']")
        ActionChains(self.KKBOX).move_to_element(album).click(play_btn).perform()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()

    def test_playlist(self): #8
        self.KKBOX.find_element_by_css_selector("div.playlist").click()
        self.KKBOX.implicitly_wait(10)
        self.KKBOX.find_element_by_css_selector("i.icon-40-headerplay").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()

    def test_songs(self): #10
        self.KKBOX.find_element_by_css_selector("td.num").click()
        time.sleep(5)
        btn = self.KKBOX.find_element_by_id("pauseBtn")
        pauseStyle = btn.get_attribute("style")
        self.assertEqual('display: inline;', pauseStyle)
        self.KKBOX.find_element_by_css_selector("i.icon-32-pause").click()


if __name__ == '__main__':
    unittest.main()