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
        page.document_type("Договор")
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
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
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
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")


    def te1st_application_cash_flow(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
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
        page.table_select_row_click('Строка для удаления')
        page.click_by_text("Удалить")
        page.click_by_text("Да")
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

        page.click_by_text("Сохранить")

        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 222 - 150000.00)(л/сч )"
                                      "Транспортные услуги,в т.ч.НДС 22881.36")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(3)


    # Проведение документов
    def te1st_carrying_out_of_documents(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
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
        page.wait.text_appear('Результат проведения документов')
        page.click_by_text("Закрыть")
        # Проверка печатных форм
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.table_select_row('ПАО "МегаФон"')
        page.click_by_text("Печать")
        sleep(10)
        #page.file.file_copy('Заявка на кассовый расход.xls')
        page.file.compare_files('Заявка на кассовый расход.xls')

    def te1st_payment_order_through_contract_with_the_supplier(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ContractWithSupplierPage(self.driver, 5)
        page.select_month("Январь", "2018")
        page.click_by_text("Договор с поставщиком")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.document_type("Договор")
        page.number("3")
        page.date("24.01.2018")
        sleep(4)
        page.сounterparty(' Акционерное общество "Ай-Теко"')
        page.bank_account_number('40702810300000114301')
        page.uin("123123123")
        page.currency("Российский рубль")
        page.date_begin("10.01.2018")
        page.date_end("10.11.2018")
        page.payment_type("аванс")
        page.subject_contract("по счетам/этапам")
        page.payment_terms("Факт поставки, подтвержденный накладными")
        page.note("Поставка оборудования")
        sleep(1)
        # Заполнение строки документа
        page.click_by_text("Детализация по КБК")
        page.click_by_text("Добавить")
        page = ContractWithSupplierPageDetailKBK(self.driver)
        page.financial_year("2018")
        page.entry_date("20.01.2018")
        page.operation("Принятие на учет бюджетных обязательств (310)")
        page.kbk("0411 0000000000 000")
        page.kosgu("310")
        sleep(3)
        page.amounts_amount("35000")
        page.checker.check_text_input("amountsAmountWithoutNds","35 000,00")
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")


        # Добавляем документ счет от поставщика
    def te1st_invoice_from_the_supplier(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Счет от поставщика")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page = InvoiceFromTheSupplierPage(self.driver)
        page.document_number("3")
        page.document_date("28.01.2018")
        page.supplier(' Акционерное общество "Ай-Теко"')
        page.supplier_account_detail("40702810300000114301")
        page.account_details("ПАО Банк ВТБ")
        page.department("Департамент внешних коммуникаций")
        page.note('Поставка оборудования , январь 2018')
        sleep(4)

        # Добавляем документ счет от поставщика строку
    def te1st_invoice_from_the_supplier_add_line(self):
        page = InvoiceFromTheSupplierAddLinePage(self.driver)
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.kbk("0411 0000000000 000")
        page.kosgu("310")
        page.cost_element("Увеличение стоимости основных средств")
        page.comment("Поставка оборудования в январе")
        page.amount("125 000,00")
        page.vat_percent("18")
        page.checker.check_text_input("amountWithoutNds", "105 932,20", 2)
        page.checker.check_text_input("ndsAmount", "19 067,80", 2)
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Добавить")
        page.click_by_text("Копию строки")
        page.wait.text_appear("Вопрос")
        page.click_by_text("С обнулением суммы")
        page.table_select_row_click('Увеличение стоимости основных средств', order=2)
        page.click_by_text("Открыть")
        page.comment("Строка для удаления")
        page.click_by_text("Сохранить", 2)
        page.table_select_row_click('Строка для удаления')
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        page.click_by_text("Сохранить")
        page.click_by_text("Группировка по аналитикам")
        # Вставить проверку таблицы
        page.click_by_text("Закрыть", order=2)
        page.click_by_text("Закрыть")

    def te1st_creation_of_a_payment_order_based_on_an_invoice(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Счет от поставщика")
        page = ApplicationCashFlowPage(self.driver)
        page.table_select_row('Акционерное общество "Ай-Теко"')
        page.click_by_text("Действие")
        element=self.driver.find_element(By.XPATH, "//li[a='Создать документ по выбору']")
        page.move_to_element(element)
        page.click_by_text("Заявка на кассовый расход")
        page.checker.check_text_select('documentKind','Заявка на кассовый расход')
        page.number("3")
        page.date("31.01.2018")
        page.limit_date("31.12.2018")
        page.personal_account("УФК л/с 03951000710")
        page.checker.check_text_select('counterparty',' Акционерное общество "Ай-Теко"')
        page.checker.check_text_select('counterpartyAccountDetails',"40702810300000114301")
        page.number_ufk("123456789012345")
        page.operation('Оплата за приобретение ОС')
        # Заполнение вкладки дкоумент основание
        page.click_by_text("Документ-основание")

        page.checker.check_text_select("foundation", '3 от 28.01.2018')
        page.checker.check_text_select("documentFoundaiontKind", 'Счет от поставщика')
        page.checker.check_text_input("documentFoundationNumber", '3')
        page.checker.check_text_input("documentFoundationSubject", 'Поставка оборудования , январь 2018')
        page.checker.check_text_input("documentFoundationDate", '28.01.2018')
        # Расшифровка заявки - добавление строки
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Открыть")

        page = DecodingOfTheApplicationPage(self.driver)
        # page.kbk("0411 0000000000 000")

        page.checker.check_text_input("amountWithoutNds", "105 932,20", 2)
        page.checker.check_text_input("ndsAmount", "19 067,80", 2)
        page.document_foundation_counterparty(' Акционерное общество "Ай-Теко"')
        page.foundation("3 от 28.01.2018")

        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 310 - 125000.00)(л/сч 03951000710)"
                                      "Увеличение стоимости основных средств,в т.ч.НДС 19067.80")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    def te1st_carrying_out_of_documents_two(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.table_select_row('Акционерное общество "Ай-Теко"')
        page.click_by_text("Действия")
        page.click_by_text("Провести помеченные")
        page = carryingOutOfDocumentsPage(self.driver)
        page.lddate_prov("31.01.2018")
        # page.operation_master("") указываем если требуется проводку
        page.click_by_text("Провести", order=3)
        page.wait.text_appear('Результат проведения документов')
        page.click_by_text("Закрыть")
        # Проверка печатных форм
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Январь", "2018")
        page.table_select_row('Акционерное общество "Ай-Теко"')
        page.click_by_text("Печать")
        sleep(10)
        # page.file.file_copy('Заявка на кассовый расход.xls')
        page.file.compare_files('Заявка на кассовый расход (1).xls')
        sleep(10)

    def te1st_turnover_statement_one(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Оборотная ведомость")
        page.select_month("Январь", "2018")
        page = TurnoverStatementPage(self.driver)
        page.date_from("01.01.2018")
        page.date_to("31.01.2018")
        page.click_by_text("Показать")
        page.wait.text_appear('Печать "Оборотная ведомость"')
        page.click_by_text('Печать "Оборотная ведомость"')
        sleep(10)
        page.file.compare_files('Оборотная ведомость.xls')

    def te1st_incoming_order(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Приходный кассовый ордер")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page = IncomingOrderPage(self.driver)
        page.document_kind("Приходный кассовый ордер (получение наличных из банка в кассу по чеку)")
        page.document_number("1")
        page.document_date("21.01.2018")
        page.employee("Старостина Е.В.")
        page.received_from("Снято с расчетного счета")
        page.cash_report_number("1234567890")
        page.foundation("Чек 12125")
        page.operation('Снятие наличных в кассу')

    # добавление строк в пко
    def te1st_incoming_order_add_line(self):
        page = IncomingOrderAddLinePage(self.driver)
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("221")
        page.expense_type("Услуги связи")
        page.amount("120 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "100 000,00")
        page.checker.check_text_input("ndsAmount", "20 000,00")
        page.comment("Услуги связи")
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("222")
        page.expense_type("Транспортные услуги")
        page.amount("95 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "79 166,67")
        page.checker.check_text_input("ndsAmount", "15 833,33")
        page.comment("Транспортные услуги")
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("226")
        page.expense_type("Хозяйственные расходы")
        page.amount("156 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "130 000,00")
        page.checker.check_text_input("ndsAmount", "26 000,00")
        page.comment("Хозяйственные расходы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("290")
        page.expense_type("Прочие расходы")
        page.amount("250 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "208 333,33")
        page.checker.check_text_input("ndsAmount", "41 666,67")
        page.comment("Прочие расходы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("310")
        page.expense_type("строительно-монтажные работы")
        page.amount("145 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "120 833,33")
        page.checker.check_text_input("ndsAmount", "24 166,67")
        page.comment("строительно-монтажные работы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.operation("Снятие наличных в кассу")
        page.kbk("0411 0000000000 000")
        page.kosgu("340")
        page.expense_type("Мягкий инвентарь")
        page.amount("123 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "102 500,00")
        page.checker.check_text_input("ndsAmount", "20 500,67")
        page.comment("Мягкий инвентарь")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)
        page.checker.check_text_input("amount", "889 000,00")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

        page.wait.text_appear(' Приходный кассовый ордер')

        page.table_select_row('Снято с расчетного счета')
        page.click_by_text("Действия")
        page.click_by_text("Провести помеченные")
        page = carryingOutOfDocumentsPage(self.driver)
        page.lddate_prov("22.01.2018")
        # page.operation_master("") указываем если требуется проводку
        page.click_by_text("Провести", order=3)
        page.wait.text_appear('Результат проведения документов')
        page.click_by_text("Закрыть")
        page.table_select_row('Снято с расчетного счета')
        page.click_by_text("Действия")
        page.click_by_text("Просмотр проводок")

        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Приходный кассовый ордер")
        page.table_select_row('Снято с расчетного счета')
        page.click_by_text("Печать")
        sleep(10)
        page.file.compare_files('Приходный кассовый ордер.xls')

    def te1st_incoming_order_copy_doc(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Приходный кассовый ордер")
        page.table_select_row('889 000,00')
        page.click_by_text("Добавить")
        page.click_by_text("Копию документа")
        page = IncomingOrderPage(self.driver)
        page.document_kind("Приходный кассовый ордер (получение наличных из банка в кассу по чеку)")
        page.document_number("2")
        page.document_date("25.01.2018")
        page.employee("Старостина Е.В.")
        page.received_from("Оприходавано в кассу")
        page.cash_report_number("1234567890")
        page.foundation("Чек 12125")
        page.operation('Получение наличных в кассу')

        page = IncomingOrderAddLinePage(self.driver)
        page.table_select_row_click('221')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("120 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "100 000,00")
        page.checker.check_text_input("ndsAmount", "20 000,00")
        page.comment("Услуги связи")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.table_select_row_click('222')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("95 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "79 166,67")
        page.checker.check_text_input("ndsAmount", "15 833,33")
        page.comment("Транспортные услуги")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.table_select_row_click('226')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("156 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "130 000,00")
        page.checker.check_text_input("ndsAmount", "26 000,00")
        page.comment("Хозяйственные расходы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.table_select_row_click('290')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("250 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "208 333,33")
        page.checker.check_text_input("ndsAmount", "41 666,67")
        page.comment("Прочие расходы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.table_select_row_click('310')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("145 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "120 833,33")
        page.checker.check_text_input("ndsAmount", "24 166,67")
        page.comment("строительно-монтажные работы")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.table_select_row_click('340')
        page.click_by_text("Открыть")
        page.operation("Получение наличных в кассу")
        page.amount("123 000,00")
        page.nds_percent("20")
        page.checker.check_text_input("amountWithoutNds", "102 500,00")
        page.checker.check_text_input("ndsAmount", "20 500,67")
        page.comment("Мягкий инвентарь")
        # Мол надо удалить!!!!!!!!!!!!!!!!!!
        page.recepient('МОЛ ФМС')
        page.click_by_text("Сохранить", 2)

        page.checker.check_text_input("amount", "889 000,00")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

        page.table_select_row('Оприходавано в кассу')
        page.click_by_text("Действия")
        page.click_by_text("Провести помеченные")
        page = carryingOutOfDocumentsPage(self.driver)
        page.lddate_prov("25.01.2018")
        # page.operation_master("") указываем если требуется проводку
        page.click_by_text("Провести", order=3)
        page.wait.text_appear('Результат проведения документов')
        page.click_by_text("Закрыть")
        page.table_select_row('Оприходавано в кассу')
        page.click_by_text("Действия")
        page.click_by_text("Просмотр проводок")

        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text("Приходный кассовый ордер")
        page.table_select_row('Оприходавано в кассу')
        page.click_by_text("Печать")
        sleep(10)
        page.file.compare_files('Приходный кассовый ордер (1).xls')

    def te1st_invoice_from_the_supplier_two(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.select_month("Февраль", "2018")
        page.click_by_text("Счет от поставщика")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page = InvoiceFromTheSupplierPage(self.driver)
        page.document_number("5")
        page.document_date("01.02.2018")
        page.supplier('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.supplier_account_detail("40702810500000002308")
        page.account_details("ПАО Банк ВТБ")
        page.department("Департамент внешних коммуникаций")
        page.note('Аудиторские услуги , февраль 2018')
        sleep(4)

        # Добавляем документ счет от поставщика строку

        page = InvoiceFromTheSupplierAddLinePage(self.driver)
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.kbk("0411 0000000000 000")
        page.kosgu("226")
        page.cost_element("Прочие услуги")
        page.comment("Справочно-информационные услуги")
        page.amount("100 000,00")

        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    def te1st_application_cash_flow_two(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Февраль", "2018")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        sleep(1)
        page.documen_type("Заявка на кассовый расход")
        page.number("1")
        page.date("02.02.2018")
        page.limit_date("12.02.2018")
        page.personal_account("ПАО Банк ВТБ")
        page.recipient('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.bank_account_number("40702810500000002308")
        page.number_ufk("123456789012345")
        # Заполнение вкладки дкоумент основание
        page.click_by_text("Документ-основание")
        page.foundation("5 от 01.02.2018")
        page.checker.check_text_select("documentFoundaiontKind", 'Счет от поставщика')
        page.checker.check_text_input("documentFoundationNumber", '5')
        page.checker.check_text_input("documentFoundationSubject", 'Аудиторские услуги , февраль 2018')
        page.checker.check_text_input("documentFoundationDate", '01.02.2018')
        # Расшифровка заявки - добавление строки
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page = DecodingOfTheApplicationPage(self.driver)
        page.kbk("0411 0000000000 000")
        page.draweeKbkType('Классификация расходов бюджетов (КРБ)')
        page.operation("(226) Оплата за прочие услуги")
        page.kosgu("226")
        sleep(5)
        page.cost_element("Прочие услуги")
        page.amount("100000")
        page.document_foundation_counterparty('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.foundation("5 от 01.02.2018")
        page.comment("Оплата аудиторских услуг, Февраль 2018")
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 226 - 100000.00)(л/сч )Прочие услуги.НДС не обл.")
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
        page.click_by_text("Сохранить", 2)

        page.search_string('Строка для удаления', 'Выбор строки для удаления')
        page.table_select_row_click('Строка для удаления')
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")


        page.table_select_row('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.click_by_text("Печать")
        sleep(10)
        page.file.compare_files('Заявка на кассовый расход (2).xls')

        # Создание копии документа
        page.table_select_row('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.click_by_text("Добавить")
        page.click_by_text("Копию документа")
        page = ApplicationCashFlowPage(self.driver)
        sleep(1)
        page.documen_type("Заявка на кассовый расход")
        page.number("2")
        page.date("10.02.2018")
        page.limit_date("20.02.2018")
        page.personal_account("ПАО Банк ВТБ")
        page.recipient('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.bank_account_number("40702810500000002308")
        page.number_ufk("123456789012345")
        # Заполнение вкладки дкоумент основание
        page.click_by_text("Документ-основание")
        page.foundation("5 от 01.02.2018")
        page.checker.check_text_select("documentFoundaiontKind", 'Счет от поставщика')
        page.checker.check_text_input("documentFoundationNumber", '5')
        page.checker.check_text_input("documentFoundationSubject", 'Аудиторские услуги , февраль 2018')
        page.checker.check_text_input("documentFoundationDate", '01.02.2018')
        # Расшифровка заявки - добавление строки
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Открыть")

        page = DecodingOfTheApplicationPage(self.driver)
        page.kbk("0411 0000000000 000")
        page.draweeKbkType('Классификация расходов бюджетов (КРБ)')
        page.operation("(226) Оплата за прочие услуги")
        page.kosgu("226")
        sleep(5)
        page.cost_element("Прочие услуги")
        page.amount("100000")
        page.document_foundation_counterparty('ООО Аудиторская компания "Аудит Проф Гарант"')
        page.foundation("5 от 01.02.2018")
        page.comment("Оплата аудиторских услуг, Февраль 2018")
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Сохранить")
        page.click_by_text("Реквизиты документа")
        page.click_by_text("Назначения платежа")
        page.checker.check_text_input("paymentPurpose",
                                      "(07104110000000000000 226 - 100000.00)(л/сч )Прочие услуги.НДС не обл.")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    def test_application_cash_flow_export_UFK(self):
        page = MenuPage(self.driver)
        page.click_to_eagle()
        page = ApplicationCashFlowPage(self.driver)
        page.click_by_text("Заявка на кассовый расход")
        page.select_month("Февраль", "2018")
        page.table_select_row('10.02.2018')
        page.click_by_text("Действия")
        page.click_by_text("Экспорт в УФК")
        page.wait.text_appear('Экспорт данных в СУФД ФК')
        page = exportUFKPage(self.driver)
        page.account_details("ПАО Банк ВТБ")
        page.file_number("1")
        page.click_by_text("Сохранить")
        sleep(5)
        File.checking_file_export_UFK()







































