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
        page.username("Test1")
        page.password("123")
        page.submit()
        page.wait.text_appear("Документы — Бухгалтерский учет")

    def te1st_contract_with_supplier(self):
        page = ContractWithSupplierPage(self.driver, 5)
        page.select_month("Январь", "2018")
        page.click_by_text("Договор с поставщиком")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.documen_type("Договор")
        page.number("1")
        page.date("10.01.2018")
        page.сounterparty("ПАО \"МегаФон\"")
        page.bank_account_number('40702810838180130496')
        page.uin("123123123")
        page.currency("Российский рубль")
        page.date_begin("10.01.2018")
        page.date_end("10.11.2018")
        page.payment_type("аванс")
        page.subject_contract("Услуги связи")
        page.payment_terms("Ежемесячно равными долями")
        page.note("Авансовые платежи")
        sleep(1)
        # Заполнение строки документа
        page.click_by_text("Детализация по КБК")
        page.click_by_text("Добавить")
        page = ContractWithSupplierPageDetailKBK(self.driver)
        page.financial_year("2018")
        page.entry_date("10.01.2018")
        page.operation("Принятые БО текущего года  (221)")
        page.kbk("0411 0000000000 000")
        page.kosgu("221")
        sleep(5)
        page.amounts_nds_percent("13")
        page.amounts_amount("1200000")
        page.advance("120000")
        page.click_by_text("Сохранить", 2)
        sleep(1)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(2)
        # Создание копии документа

        page = ContractWithSupplierPage(self.driver)
        page.select_month("Январь", "2018")
        page.click_by_text("Добавить")
        page.click_by_text("Копию документа")
        sleep(1)
        page.click_by_text("С обнулением суммы")
        sleep(1)
        page.number("2")
        page.date("10.01.2018")
        page.сounterparty("ФГУ Автобаза №2")
        # page.bank_account_number(r'40702810838180130496 | ПАО "МегаФон"')
        page.bank_account_number('40503810800001009002')
        page.uin("12345678901234567890")
        page.currency("Российский рубль")
        page.date_begin("10.01.2018")
        page.date_end("10.11.2018")
        page.payment_type("аванс")
        page.subject_contract("Трансопртные услуги")
        page.payment_terms("Ежемесячно равными долями")
        page.note("Авансовые платежи")
        sleep(1)
        page.click_by_text("Детализация по КБК")
        page.click_by_text("Открыть")
        sleep(1)
        # Заполнение строки документа
        page = ContractWithSupplierPageDetailKBK(self.driver)
        page.financial_year("2018")
        page.entry_date("10.01.2018")
        page.operation("Принятые БО текущего года  (222)")
        page.kbk("0411 0000000000 000")
        page.kosgu("222")
        sleep(5)
        page.cost_element("Транспортные услуги")
        page.amounts_nds_percent("13")
        page.amounts_amount("1800000")
        page.advance("180000")
        page.click_by_text("Сохранить", 2)
        sleep(1)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(2)

    def test_application_cash_flow(self):
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        sleep(3)
        page.documen_type("Платежное поручение")
        page.number("1")
        page.date("10.01.2018")
        page.limit_date("10.12.2018")
        page.personal_account("ПАО Банк ВТБ")
        page.recipient('ПАО "МегаФон"')
        page.bank_account_number("40702810838180130496")
        page.number_ufk("123456789012345")
        # Расшифровка заявки - добавление строки
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page = DecodingOfTheApplicationPage(self.driver)
        #page.kbk("0411 0000000000 000")
        page.set_select2_wl("kbk", "0411 0000000000 000",  exactly=False, order=2 )
        page.operation("(221) Оплата за услуги связи")
        page.kosgu("221")
        sleep(5)
        page.cost_element("Услуги связи")
        page.amount("100000")
        page.nds_percent("18")
        page.document_foundation_counterparty('ПАО "МегаФон"')
        page.foundation("1 от 10.01.2018")
        page.comment("Оплата за услуги связи Январь 2018")
        page.click_by_text("Сохранить", 2)
        sleep(1)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")



