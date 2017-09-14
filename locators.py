from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='UserName']")
    password = (By.XPATH, "//input[@id='Password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(Browser):
    pass


class CashRequestLocators(Browser):

    class NewDocument(Browser):
        account_number = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        tracking_number = (By.XPATH, "//input[@id='TrackingNumber']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")

        document_number = (By.XPATH, "//input[@id='DocumentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        entry_date = (By.XPATH, "//input[@id='EntryDate']")
        deadline = (By.XPATH, "//input[@id='Deadline']")
