from locators import *


class LoginPage(Browser):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")


class MainPage(Browser):

    pass


class CashRequestPage(Browser):

    @property
    def new_document(self):
        return self.NewDocument(self.driver)
    
    class NewDocument(Browser):

        @property
        def new_line(self):
            return self.NewLine(self.driver)

        # Реквизиты документа
        def account_number(self, value):
            self.select_type(CashRequestLocators.NewDocument.account_number, value, "Номер лицевого счета клиента")

        def tracking_number(self, value):
            self.set_text(CashRequestLocators.NewDocument.tracking_number, value, "Учетный номер обязательства")

        def operation(self, value):
            self.select_type(CashRequestLocators.NewDocument.operation, value, "Операция")

        # Информация о документе
        def document_number(self, value):
            self.set_text(CashRequestLocators.NewDocument.document_number, value, "Номер")

        def document_date(self, value):
            self.set_date(CashRequestLocators.NewDocument.document_date, value, "Дата")

        def entry_date(self, value):
            self.set_date(CashRequestLocators.NewDocument.entry_date, value, "Дата проводки")

        def deadline(self, value):
            self.set_date(CashRequestLocators.NewDocument.deadline, value, "Предельная дата исполнения")

        class NewLine(Browser):
            pass
