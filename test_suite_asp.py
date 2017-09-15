from pages import *
from links import Links


class TestSuite:

    driver = webdriver.Chrome("driver\\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_login(self):
        """
        Авторизация на портале
        """
        page = LoginPage(self.driver)
        page.username("Пользователь 1")
        page.password("111")
        page.submit()
        page.wait.text_appear("Бухгалтерский учет")

    def test_cash_expense_request(self):
        page = CashExpenseRequestPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")

        page.document_header.document_number("")
        page.document_header.document_date("")
        page.document_header.document_kind("")
        page.document_header.ofk_number("")
        page.document_header.entry_date("")
        page.document_header.operation("")
        page.document_header.current_organization_account("")
        page.document_header.short("")
        page.document_header.limit_date("")
        page.document_header.tracking_number("")
        page.document_header.federal_targeted_investment_program("")
        page.document_header.priority("")
        page.document_header.currency_amount("")
        page.document_header.currency_nds_amount("")
        page.document_header.currency_classifier("")
        page.document_header.amount("")
        page.document_header.nds_amount("")
        page.document_header.amount_without_nds("")
        page.document_header.is_advance("")
        page.document_header.payment_priority("")
        page.document_header.payment_form("")
        page.document_header.payment_purpose("")
        page.document_header.document_foundation("")
        page.document_header.document_foundation_kind("")
        page.document_header.document_foundation_number("")
        page.document_header.document_foundation_date("")
        page.document_header.document_foundation_subject("")
        page.document_header.counterparty("")
        page.document_header.counterparty_account_details("")
        page.document_header.is_employee("")
        page.document_header.is_tax("")
        page.document_header.chief("")
        page.document_header.chief_account("")
        page.click_by_text("Реквизиты документа-основания")
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.requisites.document("")
        page.requisites.document_type("")
        page.requisites.document_number("")
        page.requisites.document_date("")
        page.requisites.subject("")
        page.click_by_text("Сохранить")
        page.click_by_text("Расшифровка заявки на кассовый расход")
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.transcript.activity_kind("")
        page.transcript.kbk("")
        page.transcript.drawee_kbk_type("")
        page.transcript.kosgu("")
        page.transcript.cost_element("")
        page.transcript.recepient_kbk("")
        page.transcript.recepient_kbk_type("")
        page.transcript.goal_code("")
        page.transcript.department("")
        page.transcript.expenditure_goal_act("")
        page.transcript.document_foundation_counterparty("")
        page.transcript.foundation("")
        page.transcript.report_code("")
        page.transcript.operation("")
        page.transcript.currency_amount("")
        page.transcript.currency_nds_amount("")
        page.transcript.amount("")
        page.transcript.nds_amount("")
        page.transcript.amount_without_nds("")
        page.transcript.nds_percent("")
        page.transcript.payment_purpose("")
        page.transcript.comment("")
        page.transcript.drawee_subsidy_code("")
        page.transcript.recepient_subsidy_code("")
        page.transcript.act("")
        page.click_by_text("Сохранить")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        page.click_by_text("Закрыть")

    def test_getting_cash_request(self):
        page = CashRequestPage(self.driver)
        page.click_by_text("Заявка на получение наличных денег")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")

        page.new_document.account_number("Администрато")
        page.new_document.tracking_number("1233")
        page.new_document.operation("Снятие наличных (деньги в пути) (Все КОСГУ)")

        page.new_document.document_number("123")
        page.new_document.document_date("14.09.2017")
        page.new_document.entry_date("14.09.2017")
        page.new_document.deadline("24.09.2017")

        sleep(10)
