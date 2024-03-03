from selenium.webdriver.common.by import By
from infra.page_base import BasePage


class ContactsPage(BasePage):
    CONTACTS_ELEMENT = (By.XPATH,
                        '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div')

    NEW_CONTACTS_ELEMENT = (By.XPATH,
                            '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')

    TEXT_NEW_CONTACTS = (By.XPATH,
                         "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_CONTACTS = (By.XPATH,
                         "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_contacts(self, contact_name="New contact"):
        return self.add_new(name=contact_name, ELEMENT=self.CONTACTS_ELEMENT, NEW_ELEMENT=self.NEW_CONTACTS_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_CONTACTS, NAME_NEW=self.NAME_NEW_CONTACTS, name_new="New contact")

    def delete_contacts(self, contact_name="New contact", select_Type="first"):
        return self.delete_equal(name=contact_name, ELEMENT=self.CONTACTS_ELEMENT, select_Type=select_Type)

    def delete_all_contacts(self):
        return self.delete_all(self.CONTACTS_ELEMENT, NAME_NEW=self.NAME_NEW_CONTACTS)

    def undo_delete_all_contacts(self):
        _elements = self.delete_all_contacts()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_CONTACTS)
