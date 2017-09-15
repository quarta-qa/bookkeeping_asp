from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='UserName']")
    password = (By.XPATH, "//input[@id='Password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):
    pass


class CashPullRequestLocators(object):

    filter = (By.XPATH, "//input[@placeholder='Все поля']")

    class NewDocument(object):
        # Реквизиты документа
        account_number = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        tracking_number = (By.XPATH, "//input[@id='TrackingNumber']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")
        # Информация о документе
        document_number = (By.XPATH, "//input[@id='DocumentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        entry_date = (By.XPATH, "//input[@id='EntryDate']")
        deadline = (By.XPATH, "//input[@id='Deadline']")
        # Дополнительно - Доверенность
        trustee = (By.XPATH, "(//button[@title='Выбрать'])[3]")
        trustee_name_dative_case = (By.XPATH, "//input[@id='TrusteeNameDativeCase']")
        trustee_position = (By.XPATH, "(//button[@title='Выбрать'])[4]")
        trustee_position_dative_case = (By.XPATH, "//input[@id='TrusteePositionDativeCase']")
        foundation = (By.XPATH, "//input[@id='Foundation']")
        # Дополнительно - Чек
        check_series = (By.XPATH, "//input[@id='CheckSeries']")
        check_number = (By.XPATH, "//input[@id='CheckNumber']")
        check_date = (By.XPATH, "//input[@id='CheckDate']")
        check_valid_till = (By.XPATH, "//input[@id='CheckValidTill']")
        # Дополнительно - Подписывающие лица
        manager = (By.XPATH, "(//button[@title='Выбрать'])[5]")
        chief_accountant = (By.XPATH, "(//button[@title='Выбрать'])[6]")

        class NewLine(object):
            kbk = (By.XPATH, "(//button[@title='Выбрать'])[7]")
            kbk_type = (By.XPATH, "//select[@name='kbkType']")
            kosgu = (By.XPATH, "(//button[@title='Выбрать'])[8]")
            costs_type = (By.XPATH, "(//button[@title='Выбрать'])[9]")
            operation = (By.XPATH, "(//button[@title='Выбрать'])[10]")
            funds_source = (By.XPATH, "//select[@name='fundsSource']")
            cash_transaction_code = (By.XPATH, "//select[@name='CashTransactionCode']")
            code_goal = (By.XPATH, "//input[@id='CodeGoal']")
            payment_purpose = (By.XPATH, "//input[@id='PaymentPurpose']")
            amount = (By.XPATH, "//input[@id='amount']")
            comment = (By.XPATH, "//input[@id='Comment']")
