from locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def get_txt_val_1(self):
        """Triggers the search"""
        txt_val_1_txt = self.driver.find_element(*MainPageLocators.TXT_VAL_1).text
        return txt_val_1_txt

    def get_txt_val_2(self):
        """Triggers the search"""
        txt_val_2_txt = self.driver.find_element(*MainPageLocators.TXT_VAL_2).text
        return txt_val_2_txt

    def get_txt_val_3(self):
        """Triggers the search"""
        txt_val_3_txt = self.driver.find_element(*MainPageLocators.TXT_VAL_3).text
        return txt_val_3_txt

    def get_txt_val_4(self):
        """Triggers the search"""
        txt_val_4_txt = self.driver.find_element(*MainPageLocators.TXT_VAL_4).text
        return txt_val_4_txt

    def get_txt_val_5(self):
        """Triggers the search"""
        txt_val_5_txt = self.driver.find_element(*MainPageLocators.TXT_VAL_5).text
        return txt_val_5_txt


    def get_lbl_val_1(self):
        """Triggers the search"""
        lbl_1_txt = self.driver.find_element(*MainPageLocators.LBL_VAL_1).text
        assert lbl_1_txt == 'Value 1'

    def get_lbl_val_2(self):
        """Triggers the search"""
        lbl_2_txt = self.driver.find_element(*MainPageLocators.LBL_VAL_2).text
        assert lbl_2_txt == 'Value 2'

    def get_lbl_val_3(self):
        """Triggers the search"""
        lbl_3_txt = self.driver.find_element(*MainPageLocators.LBL_VAL_3).text
        return lbl_3_txt

    def get_lbl_val_4(self):
        """Triggers the search"""
        lbl_4_txt = self.driver.find_element(*MainPageLocators.LBL_VAL_4).text
        return lbl_4_txt

    def get_lbl_val_5(self):
        """Triggers the search"""
        lbl_4_txt = self.driver.find_element(*MainPageLocators.LBL_VAL_4).text
        return lbl_4_txt




