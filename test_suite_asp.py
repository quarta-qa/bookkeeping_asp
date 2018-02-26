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
        page.checker.check_text_input("amountsAmountWithoutNds","1 061 946,90")
        page.checker.check_text_input("amountsNdsAmount", "138 053,10")
        page.click_by_text("Сохранить", 2)
        sleep(1)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(2)
        # Проверка заполненой суммы

        # Создание копии документа

        page = ContractWithSupplierPage(self.driver)
        page.select_month("Январь", "2018")
        page.table_select_row('ПАО "МегаФон"','Выбор документа из которого будем делать копию')
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
        page.subject_contract("Транспортные услуги")
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
        page.checker.check_text_input("amountsAmountWithoutNds", "1 592 920,35")
        page.checker.check_text_input("amountsNdsAmount", "207 079,65")
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
        sleep(1)
        page.documen_type("Платежное поручение")
        page.number("1")
        page.date("10.01.2018")
        page.limit_date("10.12.2018")
        page.personal_account("ПАО Банк ВТБ")
        page.recipient('ПАО "МегаФон"')
        page.bank_account_number("40702810838180130496")
        page.number_ufk("123456789012345")
        # Заполнение вкладки дкоумент основание
        page.click_by_text("Документ-основание")
        page.foundation("1 от 10.01.2018")
        page.checker.check_text_select("documentFoundaiontKind",'Договор с поставщиком')
        page.checker.check_text_input("documentFoundationNumber", '1')
        page.checker.check_text_input("documentFoundationSubject", 'Услуги связи')
        page.checker.check_text_input("documentFoundationDate", '10.01.2018')
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
        page.checker.check_text_input("amountWithoutNds", "84 745,76",2)
        page.checker.check_text_input("ndsAmount", "15 254,24",2)
        page.document_foundation_counterparty('ПАО "МегаФон"')
        page.foundation("1 от 10.01.2018")
        page.comment("Оплата за услуги связи Январь 2018")
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        sleep(1)
        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 221 - 100000.00)(л/сч )Услуги связи,в т.ч.НДС 15254.24")
        page.click_by_text("Сохранить")
           # Добавляем копию строки
        page.click_by_text("Расшифровка заявки")
        # Исправить после доработки функционала!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # page.click_by_text("Добавить")
        # page.click_by_text("Копию строки")

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.comment("Строка для удаления")
        sleep(5)
        #page.wait.text_disappear("Документ сохранён")
        page.click_by_text("Сохранить", 2)

        page.search_string('Строка для удаления', 'Выбор строки для удаления')
        sleep(3)
        page.table_select_row_click('Строка для удаления')
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        sleep(2)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

        # Создание копии документа
        page.table_select_row('ПАО "МегаФон"')
        page.click_by_text("Добавить")
        page.click_by_text("Копию документа")
        page = ApplicationCashFlowPage(self.driver)
        sleep(1)
        page.documen_type("Платежное поручение")
        page.number("2")
        page.date("10.01.2018")
        page.limit_date("10.12.2018")
        page.personal_account("ПАО Банк ВТБ")
        page.recipient('ФГУ Автобаза №2')
        page.bank_account_number("40503810800001009002")
        page.number_ufk("123456789012345")
        # Заполнение вкладки дкоумент основание
        page.click_by_text("Документ-основание")
        page.foundation("2 от 10.01.2018")
        page.checker.check_text_select("documentFoundaiontKind", 'Договор с поставщиком')
        page.checker.check_text_input("documentFoundationNumber", '2')
        page.checker.check_text_input("documentFoundationSubject", 'Транспортные услуги')
        page.checker.check_text_input("documentFoundationDate", '10.01.2018')

        #редактируем строку
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Открыть")
        page = DecodingOfTheApplicationPage(self.driver)
        page.kbk("0411 0000000000 000")
        page.operation("(222) Оплата за транспортные услуги")
        page.kosgu("222")
        sleep(5)
        page.cost_element("Транспортные услуги")
        page.amount("150000")
        page.nds_percent("18")
        page.checker.check_text_input("amountWithoutNds", "127 118,64", 2)
        page.checker.check_text_input("ndsAmount", "22 881,36", 2)
        page.document_foundation_counterparty('ФГУ Автобаза №2')
        page.foundation("2 от 10.01.2018")
        page.comment("Оплата транспортных услуг Январь 2018")
        page.click_by_text("Сохранить", 2)
        sleep(3)
        page.click_by_text("Сохранить")
        sleep(1)
        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 222 - 150000.00)(л/сч )"
                                      "Транспортные услуги,в т.ч.НДС 22881.36")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(3)


        # Проведение документов
    def test_carrying_out_of_documents(self):
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.table_select_row('ПАО "МегаФон"')
        page.table_select_row('ФГУ Автобаза №2')
        page.click_by_text("Действия")
        page.click_by_text("Провести помеченные")
        page = carryingOutOfDocumentsPage(self.driver)
        page.lddate_prov("10.01.2018")
        #page.operation_master("") указываем если требуется проводку
        page.click_by_text("Провести", order=3)
        # Проверка печатных форм
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.table_select_row('ПАО "МегаФон"')
        page.click_by_text("Печать")










