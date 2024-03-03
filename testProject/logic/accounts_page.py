from selenium.webdriver.common.by import By
from infra.page_base import BasePage


class AccountsPage(BasePage):
    ACCOUNTS_ELEMENT = (By.XPATH,
                    '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[5]/div/div/div/div/div')

    NEW_ACCOUNTS_ELEMENT = (By.XPATH,
                        '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')

    TEXT_NEW_ACCOUNTS = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_ACCOUNTS = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_accounts(self, account_name="New account"):
        return self.add_new(name=account_name, ELEMENT=self.ACCOUNTS_ELEMENT, NEW_ELEMENT=self.NEW_ACCOUNTS_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_ACCOUNTS, NAME_NEW=self.NAME_NEW_ACCOUNTS, name_new="New account")

    def delete_accounts(self, accounts_name="New account", select_Type="first"):
        return self.delete_equal(name=accounts_name, ELEMENT=self.ACCOUNTS_ELEMENT, select_Type=select_Type)

    def delete_all_accounts(self):
        return self.delete_all(self.ACCOUNTS_ELEMENT, NAME_NEW=self.NAME_NEW_ACCOUNTS)

    def undo_delete_all_accounts(self):
        _elements = self.delete_all_accounts()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_ACCOUNTS)
