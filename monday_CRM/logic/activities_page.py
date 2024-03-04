from selenium.webdriver.common.by import By
from infra.page_base import BasePage


class ActivitiesPage(BasePage):
    ACTIVITIES_ELEMENT = (By.XPATH,
                          '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[6]/div/div/div/div/div')

    NEW_ACTIVITIES_ELEMENT = (By.XPATH,
                              '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')

    TEXT_NEW_ACTIVITIES = (By.XPATH,
                           "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_ACTIVITIES = (By.XPATH,
                           "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_activity(self, activity_name="New activity"):
        return self.add_new(name=activity_name, ELEMENT=self.ACTIVITIES_ELEMENT,
                            NEW_ELEMENT=self.NEW_ACTIVITIES_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_ACTIVITIES, NAME_NEW=self.NAME_NEW_ACTIVITIES, name_new="New "
                                                                                                           "activity")

    def delete_activity(self, activity_name="New activity", select_Type="first"):
        return self.delete_equal(name=activity_name, ELEMENT=self.ACTIVITIES_ELEMENT, select_Type=select_Type)

    def delete_all_activities(self):
        return self.delete_all(self.ACTIVITIES_ELEMENT, NAME_NEW=self.NAME_NEW_ACTIVITIES)

    def undo_delete_all_activities(self):
        _elements = self.delete_all_activities()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_ACTIVITIES)
