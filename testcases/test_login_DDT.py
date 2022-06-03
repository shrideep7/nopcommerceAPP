import pytest

from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutils


class Test_002_Login_DDT:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    path = './/testdata/LoginData.xlsx'

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        self.logger.info("**************** Test_002_Login_DDT ****************** ")
        self.logger.info("****************verifying Login DDT title ****************** ")
        self.driver = setup
        self.driver.implicitly_wait(10)

        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows = xlutils.getrowcount(self.path, 'Sheet1')
        print("number of rows in excel sheet:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = xlutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = xlutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()


            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*********passed********")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********failed********")
                    self.lp.clicklogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*********failed********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*********passed********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test is failed")
            self.driver.close()
            assert False

        self.logger.info("*************end of login ddt test case")
        self.logger.info("******************** completed Test_002_Login_DDT")
