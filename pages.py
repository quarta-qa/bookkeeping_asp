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


class CashPullRequestPage(Browser):

    @property
    def new_document(self):
        return self.NewDocument(self.driver)

    @property
    def holding_request(self):
        return self.HoldingRequest(self.driver)

    def filter(self, value):
        self.set_text(CashPullRequestLocators.filter, value + Keys.RETURN, "Поиск записи")
        self.set_checkbox((By.XPATH, "//tr[contains(., '%s')]//input" % value))

    class HoldingRequest(Browser):

        def lddate_prov(self, value):
            self.set_date(CashPullRequestLocators.HoldingRequest.lddate_prov, value, "Дата проводки")

        def typical_operation(self, value):
            self.set_type(CashPullRequestLocators.HoldingRequest.typical_operation, value, "Типовая операция")

        def submit(self):
            self.click(CashPullRequestLocators.HoldingRequest.submit)

    class NewDocument(Browser):

        @property
        def new_line(self):
            return self.NewLine(self.driver)

        # Реквизиты документа

        def account_number(self, value):
            self.set_type(CashPullRequestLocators.NewDocument.account_number, value, "Номер лицевого счета клиента")

        def tracking_number(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.tracking_number, value, "Учетный номер обязательства")

        def operation(self, value):
            self.set_type(CashPullRequestLocators.NewDocument.operation, value, "Операция")

        # Информация о документе

        def document_number(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.document_number, value, "Номер")

        def document_date(self, value):
            self.set_date(CashPullRequestLocators.NewDocument.document_date, value, "Дата")

        def entry_date(self, value):
            self.set_date(CashPullRequestLocators.NewDocument.entry_date, value, "Дата проводки")

        def deadline(self, value):
            self.set_date(CashPullRequestLocators.NewDocument.deadline, value, "Предельная дата исполнения")

        # Дополнительно - Доверенность

        def trustee(self, value):
            self.set_type(CashPullRequestLocators.NewDocument.trustee, value, "Доверенное лицо")

        def trustee_name_dative_case(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.trustee_name_dative_case, value, "ФИО в дательном падеже")

        def trustee_position(self, value):
            self.set_type(CashPullRequestLocators.NewDocument.trustee_position, value, "Должность")

        def trustee_position_dative_case(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.trustee_position_dative_case,
                          value, "Должность в дательном падеже")

        def foundation(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.foundation, value, "Основание")

        # Дополнительно - Чек

        def check_series(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.check_series, value, "Серия чека")

        def check_number(self, value):
            self.set_text(CashPullRequestLocators.NewDocument.check_number, value, "Номер чека")

        def check_date(self, value):
            self.set_date(CashPullRequestLocators.NewDocument.check_date, value, "Дата чека")

        def check_valid_till(self, value):
            self.set_date(CashPullRequestLocators.NewDocument.check_valid_till, value, "Срок действия чека")

        # Дополнительно - Подписывающие лица

        def manager(self, value):
            self.scroll_to_bottom()
            self.set_type(CashPullRequestLocators.NewDocument.manager, value, "Руководитель")

        def chief_accountant(self, value):
            self.scroll_to_bottom()
            self.set_type(CashPullRequestLocators.NewDocument.chief_accountant, value, "Главный бухгалтер")

        class NewLine(Browser):

            def kbk(self, value):
                self.set_type(CashPullRequestLocators.NewDocument.NewLine.kbk, value, "КБК")

            def kbk_type(self, value):
                self.set_select(CashPullRequestLocators.NewDocument.NewLine.kbk_type, value, "Тип БК")

            def kosgu(self, value):
                self.set_type(CashPullRequestLocators.NewDocument.NewLine.kosgu, value, "КОСГУ")

            def costs_type(self, value):
                self.set_type(CashPullRequestLocators.NewDocument.NewLine.costs_type, value, "Вид затрат")

            def operation(self, value):
                self.set_type(CashPullRequestLocators.NewDocument.NewLine.operation, value, "Операция")

            def funds_source(self, value):
                self.set_select(CashPullRequestLocators.NewDocument.NewLine.funds_source,
                                value, "Вид средств для исполнения обязательств")

            def cash_transaction_code(self, value):
                self.set_select(CashPullRequestLocators.NewDocument.NewLine.cash_transaction_code,
                                value, "Кассовый символ")

            def code_goal(self, value):
                self.set_text(CashPullRequestLocators.NewDocument.NewLine.code_goal, value, "Код цели")

            def payment_purpose(self, value):
                self.set_text(CashPullRequestLocators.NewDocument.NewLine.payment_purpose, value, "Назначение платежа")

            def amount(self, value):
                self.set_text(CashPullRequestLocators.NewDocument.NewLine.amount, value, "Сумма")

            def comment(self, value):
                self.set_text(CashPullRequestLocators.NewDocument.NewLine.comment, value, "Примечание")
