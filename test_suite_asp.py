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
        pass

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
