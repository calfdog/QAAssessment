import unittest
from selenium import webdriver
import page
import time


class AmountValidation(unittest.TestCase):
    """A test class to validate the amounts"""

    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe')
        self.driver.get("https://exercise1.com/values")

    def to_money(self, amt):
        """Parses the string and returns a numerical value"""
        number = amt.strip("$")
        [num, dec] = number.rsplit('.')
        dec = int(dec)
        aside = str(dec)
        x = int('1' + '0' * len(aside))
        price = float(dec) / x
        num = num.replace(',', '')
        num = int(num)
        price = num + price
        return price

    def test_amounts(self):
        """
        Tests
        """
        # Values can be driven from excel or pandas instead of hard coded values
        expected_lbl_1 = "Value 1"
        expected_lbl_2 = "Value 2"
        expected_lbl_3 = "Value 3"
        expected_lbl_4 = "Value 4"
        expected_lbl_5 = "Value 5"

        # Amount Values
        amt_vals = {"expected_val_1": "$122,365.24",
                "expected_val_2": "$599.00",
                "expected_val_3": "850,139.99",
                "expected_val_4": "$23,329.50",
                "expected_val_5": "$566.27"}

        # Expected total amount
        expected_total_amt = "$1,000,000.00"

        x = amt_vals['expected_val_1']


        # Get the main page object
        main_page = page.MainPage(self.driver)

        # Verify lables
        lbl_1_txt = main_page.get_lbl_val_1()
        assert lbl_1_txt == expected_lbl_1

        lbl_2_txt = main_page.get_lbl_val_2()
        assert lbl_2_txt == expected_lbl_2

        lbl_3_txt = main_page.get_lbl_val_3()
        assert lbl_3_txt == expected_lbl_3

        lbl_4_txt = main_page.get_lbl_val_4()
        assert lbl_4_txt == expected_lbl_4

        lbl_5_txt = main_page.get_lbl_val_5()
        assert lbl_5_txt == expected_lbl_5

        # Get an verify values is not zero and the values match
        val_1_txt = main_page.get_txt_val_1()
        amt1 = self.to_money(val_1_txt)
        assert amt1 > 0
        assert val_1_txt == amt_vals['expected_val_1']

        val_2_txt = main_page.get_txt_val_2()
        amt2 = self.to_money(val_2_txt)
        assert val_2_txt == amt_vals['expected_val_2']

        val_3_txt = main_page.get_txt_val_3()
        amt3 = self.to_money(val_3_txt)
        assert val_2_txt == amt_vals['expected_val_3']

        val_4_txt = main_page.get_txt_val_4()
        amt4 = self.to_money(val_4_txt)
        assert val_4_txt == amt_vals['expected_val_4']

        val_5_txt = main_page.get_txt_val_5()
        amt5 = self.to_money(val_4_txt)
        assert val_5_txt == amt_vals['expected_val_5']

        amt1 = self.to_money("$122,365.24")
        amt2 = self.to_money("$599.00")
        amt3 = self.to_money("$850,139.99")
        amt4 = self.to_money("$23,329.50")
        amt5 = self.to_money("$566.27")
        total = (amt1 + amt2 + amt3 + amt4 + amt5)
        assert total == expected_total_amt # This should fail

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()