import pytest

from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepagetitle(self, setup):

        self.logger.info("****************Test_001_Login****************** ")
        self.logger.info("****************verifying homepage title ****************** ")
        self.driver = setup

        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("****************Home page title test is passed****************** ")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("****************home page title test is failed****************** ")
            assert False
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************verifying admin page title ****************** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("****************admin page title test is passed****************** ")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************admin page title test is failed****************** ")
            assert False
