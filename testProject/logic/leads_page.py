from selenium.webdriver.common.by import By
from infra.page_base import BasePage


class LeadsPage(BasePage):
    LEADS_ELEMENT = (By.XPATH,
                     '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div/div')

    NEW_LEADS_ELEMENT = (By.XPATH,
                         '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')

    TEXT_NEW_LEADS = (By.XPATH,
                      "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_LEADS = (By.XPATH,
                      "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_leads(self, lead_name="New lead"):
        return self.add_new(name=lead_name, ELEMENT=self.LEADS_ELEMENT, NEW_ELEMENT=self.NEW_LEADS_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_LEADS, NAME_NEW=self.NAME_NEW_LEADS, name_new="New lead")

    def delete_leads(self, leads_name="New lead", select_Type="first"):
        return self.delete_equal(name=leads_name, ELEMENT=self.LEADS_ELEMENT, select_Type=select_Type)

    def delete_all_leads(self):
        return self.delete_all(self.LEADS_ELEMENT, NAME_NEW=self.NAME_NEW_LEADS)

    def undo_delete_all_leads(self):
        _elements = self.delete_all_leads()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_LEADS)
