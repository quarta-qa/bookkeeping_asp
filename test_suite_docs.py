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
        page.wait.text_appear("Бухгалтерский учет")

    def te1st_getting_cash_request(self):
        page = CashPullRequestPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Заявка на получение наличных денег")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        # Реквизиты документа
        page.new_document.account_number("Администратор")
        page.new_document.tracking_number("1233")
        page.new_document.operation("Снятие наличных (деньги в пути) (Все КОСГУ)")
        # Информация о документе
        page.new_document.document_number("88005553535")
        page.new_document.document_date("14.09.2017")
        page.new_document.entry_date("14.09.2017")
        page.new_document.deadline("24.09.2017")
        page.new_document.click_by_text("Дополнительно")
        # Доверенность
        page.new_document.trustee("Попов В.А.")
        page.new_document.trustee_name_dative_case("Попову В.А.")
        page.new_document.trustee_position("Советник")
        page.new_document.trustee_position_dative_case("Советнику")
        page.new_document.foundation("Основание")
        # Чек
        page.new_document.check_series("ME")
        page.new_document.check_number("12333333")
        page.new_document.check_date("12.09.2017")
        page.new_document.check_valid_till("12.09.2018")
        # Подписывающие лица
        page.new_document.manager("Портная Н.О.")
        page.new_document.chief_accountant("Дорофеева Т.Н.")
        page.new_document.click_by_text("Строки документа")
        page.new_document.click_by_text("Добавить")
        page.new_document.click_by_text("Новую строку")
        page.new_document.new_line.kbk("110 1 11 02012 01 0000 120")
        page.new_document.new_line.kbk_type("Группировочный КБК (гКБК)")
        page.new_document.new_line.kosgu("110")
        # page.new_document.new_line.costs_type("")
        page.new_document.new_line.operation("Снятие наличных (деньги в пути) (Все КОСГУ)")
        page.new_document.new_line.funds_source("1 - Средства бюджета")
        page.new_document.new_line.cash_transaction_code("53 Прочие выдачи")
        page.new_document.new_line.code_goal("123334")
        page.new_document.new_line.payment_purpose("Назначение")
        page.new_document.new_line.amount("2300000")
        page.new_document.new_line.comment("Примечание")
        page.new_document.new_line.click_by_text("Сохранить", 2)
        page.new_document.click_by_text("Сохранить")
        page.new_document.click_by_text("Закрыть", 2)
        page.new_document.click_by_text("Закрыть")
        page.filter("88005553535")
        page.click_by_text("Печать")
        page.click_by_text("Действие")
        page.click_by_text("Провести")
        page.holding_request.lddate_prov("12.09.2017")
        page.holding_request.typical_operation("Снятие наличных (деньги в пути) (Все КОСГУ)")
        page.holding_request.submit()
        page.click_by_text("Закрыть")

    def te1st_pko(self):
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ Информация о документе
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ Информация о документе")
        page = PKOPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Приходный кассовый ордер")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.set_select2_wl("documentKind", "Приходный кассовый ордер", "поле Вид документа")
        page.set_text_wl("documentNumber", "2", "Номер")
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ Принято от
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ Принято от")
        page.set_select2_wl("employee", "Петров А.В.", "Сотрудник")
        page.set_select2_wl("organization", "МИФНС России № 46", "Организация", exactly=False)
        assert page.checker.check_text_input("receivedFrom", " УФК по г. Москве (МИФНС России № 46 по г.Москве)")
        page.set_select2_wl("operation", "Выдача из кассы в подотчет (прочие расходы)", "Типовая операция")
        page.set_select2_wl("departmentUnit", "ФАМИРТ", "Группа учета")
        page.set_text_wl("cashReportNumber", "25", "Номер кассового отчета")
        page.set_text_wl("foundation", "Текст заполнения поля Основание", "Основание")
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Строки документа
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Строки документа")
        page.click_by_text("Строки документа")
        page.line.click_by_text("Добавить")
        page.line.click_by_text("Новую строку")
        sleep(2)
        page.line.set_select2_wl("operation",
                                 "Выдача из кассы в подотчет (прочие расходы)", "Типовая операция", order=2)
        page.line.set_select2_wl("kosgu", "290", "КОСГУ", exactly=False)
        page.line.set_select2_wl("inventory", "TV кабель", "Номенклатура")
        page.line.set_select2_wl("kbk", "(2017) - Больницы", "КБК", exactly=False)
        page.line.set_select2_wl("expenseType", "Прочие расходы", "Вид затрат")
        page.line.set_text_wl("quantity", "20", "Количество")
        page.line.set_text_wl("amount", "100", "Сумма", order=2)
        page.line.set_text_wl("ndsPercent", "18", "Ставка НДС")
        assert page.checker.check_text_input("amountWithoutNds", "84,75")
        assert page.checker.check_text_input("ndsAmount", "15,25")
        page.line.set_select2_wl("departmentUnit", "ФАМИРТ", "Группа учета", order=2)
        page.line.set_select2_wl("recepient", "Зотова М.В.", "Получатель (МОЛ)")
        page.line.set_text_wl("comment", "Текст заполнения поля Комментарий", "Комментарий", order=2)
        page.line.set_select2_wl("act", "2008 - Договор", "Мероприятие")
        page.line.set_select_wl("CashTransactionCode", "53 Прочие выдачи", "Кассовый символ", order=2)
        sleep(2)
        page.line.click_by_text("Сохранить", 2)
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Приложение
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Приложение")
        page.click_by_text("Приложение")
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Проводки
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Проводки")
        page.click_by_text("Проводки")
        # ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Строки документа
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР \ блок Строки документа")
        page.click_by_text("Строки документа")
        # page.accounting.save_screenshot("test1", default_folder="C:\\Test\\")
        sleep(5)
        page.line.click_by_text("Сохранить", 1)
        assert page.wait.text_appear("Документ сохранен")
        print("ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР - ДОКУМЕНТ СОХРАНЕН")

    def test_zkr(self):
        # ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Информация о документе
        print("ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Информация о документе")
        page = ZKRPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Заявка на кассовый расход")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.set_select2_wl("documentKind", "Заявка на кассовый расход", "поле Вид документа")
        page.set_select2_wl("accountDetails", "14481000320 (Московская обл.)", exactly=False)
        page.set_select2_wl("counterparty", "МИФНС России № 46", "Наименование контрагента или ФИО", exactly=False)
        page.set_text_wl("documentNumber", "3")
        page.set_text_wl("ofkNumber", "77", "Номер УФК")
        assert page.checker.check_text_select("counterpartyAccountDetails", "40101810800000010041")
        sleep(5)
        page.set_date_wl("documentDate", "05.02.2018")
        page.set_date_wl("entryDate", "05.02.2018", "Дата проводки")
        page.set_date_wl("limitDate", "10.02.2018", "Предельная дата исполнения")
        page.set_select2_wl("operation", "(226) Оплата за прочие услуги", "Типовая операция")
        # ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Реквизиты документа
        print("ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Реквизиты документа")
        page.request.click_by_text("Реквизиты документа")
        page.request.set_select2_wl("currency", "Российский рубль", "Код валюты по ОКВ")
        page.request.set_select2_wl("departmentUnit", "ФАМИРТ", "Группа учета")
        page.request.set_select2_wl("faip", "Технопарк МФТИ, поселок Северный", "Код объекта по ФАИП")
        page.request.set_text_wl("priority", "1", "Приоритет исполнения")
        page.request.set_select_wl("paymentForm", "4 – срочно", "Вид платежа")
        page.request.set_text_wl("paymentPurpose", "Текст заполнения поля Назначение платежа", "Назначение платежа")
        # ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Документ-основание
        print("ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Документ-основание")
        page.doc.click_by_text("Документ-основание")
        page.doc.set_select2_wl("foundation", "", "Документ-основание")
        page.doc.set_text_wl("trackingNumber", "8", "Учетный номер обязательства")
        page.doc.set_select2_wl("documentFoundaiontKind", "Договор", "Вид документ-основания")
        page.doc.set_text_wl("documentFoundationNumber", "25", "Учетный номер обязательства")
        page.doc.set_date_wl("documentFoundationDate", "05.02.2018")
        page.doc.set_text_wl("documentFoundationSubject", "Текст заполнения поля Предмет", "Предмет")
        # ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Расшифровка заявки
        print("ЗАЯВКА НА КАССОВЫЙ РАСХОД \ Расшифровка заявки")
        page.click_by_text("Расшифровка заявки")
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.bid.set_select_wl("activityKind", "1 - Средства бюджета", "Вид стредств")
        page.bid.set_select2_wl("operation", "(226) Оплата за прочие услуги", "Типовая операция", order=2)
        page.bid.set_select2_wl("kbk", "(2016) 122 ЦА Командировки 212,222,226",
                                "КБК плательщика", exactly=False, order=2)
        page.bid.set_select_wl("drawee_kbk_type", "Группировочный КБК (гКБК)", "Тип КБК плательщика", order=2)
        page.bid.set_select2_wl("kosgu", "226", "КОСГУ", exactly=False)
        page.bid.set_select2_wl("costElement", "Прочие услуги", "Вид затрат")
        page.bid.set_text_wl("amountWithoutNds", "100", "Сумма без НДС", order=2)
        page.bid.set_text_wl("ndsPercent", "18", "Ставка НДС")
        page.bid.set_text_wl("ndsAmount", "15,25", "Сумма НДС", order=2)
        page.bid.set_text_wl("amount", "84,75", "Сумма в рублях", order=2)
        # assert page.checker.check_text_input("amountWithoutNds", "84,75")
        # assert page.checker.check_text_input("ndsAmount", "15,25")
        page.bid.set_select2_wl("recepientKbk", "РАГС", "КБК получателя")
        # page.set_text_wl("outstandingPaymentDocumentAmount", "100.00","поле Сумма в рублях")
        # page.set_text_wl("ndsPercent", "18","Ставка НДС")
        # assert page.check_text_input("ndsAmount", "15,25")

    def te1st_znv(self):
        # ЗАЯВКА НА ВОЗВРАТ \ шапка документа
        print("ЗАЯВКА НА ВОЗВРАТ \ шапка документа")
        page = ZNVPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Заявка на возврат")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.set_text_wl("documentNumber", "1", "Номер")
        page.set_date_wl("documentDate", "05.02.2018", "Дата")
        page.set_select2_wl("accountDetails", "14481000320 (Московская обл.)", "поле Лицевой счет", exactly=False)
        page.set_select2_wl("recepient", "", "Наименование получателя")
        # exactly=False исп. для точного совпадения
        page.set_text_wl("ofkRegistrationNumber", "05.02.2018", "Номер УФК")
        page.set_date_wl("entryDate", "05.02.2018", "Дата проводки")
        page.set_select2_wl("operation",
                            "Выбытие средств из временного распоряжения", "Типовая операция", exactly=False)
        page.set_select2_wl("recepientAccountDetails", "", "Банковский счет")
        page.set_select2_wl("documentKind", "Внебанковская заявка на возврат", "Вид документа")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки")
        page.click_by_text("Расшифровка заявки")
        page.request.set_text_wl("outstandingPaymentDocumentAmount", "100.00", "поле Сумма в рублях")
        page.set_text_wl("ndsPercent", "18", "Ставка НДС")
        page.request.set_text_wl("ndsAmount", "", "Сумма НДС")
        # расчетное значение
        page.request.set_select2_wl("kbk", "0410 9970092041 244", "КБК", exactly=False)
        page.request.set_select_wl("kbkType", "Группировочный КБК (гКБК)", "Тип КБК")
        page.request.set_select2_wl("kosgu", "290", "КОСГУ", exactly=False)
        page.request.set_select2_wl("costElement", "Прочие расходы", "Вид затрат")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Дополнительные реквизиты
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Дополнительные реквизиты")
        page.request.set_text_wl("goalCode", "32", "Код цели")
        page.request.set_select2_wl("investmentProgram", "Технопарк МФТИ, поселок Северный", "Код объекта по ФАИП")
        page.request.set_select2_wl("oktmo", "40 333 000", "Код по ОКТМО", exactly=False)
        page.request.set_select2_wl("expenditureGoalAct", "2008 - Договор", "Мероприятие")
        page.request.set_select2_wl("department", "Договор подряда", "Группа учета")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Информация о платеже
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Информация о платеже")
        page.request.set_text_wl("paymentPurpose", "Текст заполнения поля Назначения платежа", "Назначение платежа")
        page.request.set_select_wl("paymentForm", "4 – срочно", "Вид платежа")
        page.request.set_text_wl("paymentPriority", "1", "Очередность платежа")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Документ-основание
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Документ-основание")
        page.request.set_select2_wl("documentFoundationKind", "Акт выполненных работ", "Вид документа-основание")
        page.request.set_text_wl("documentFoundationNumber", "21", "Номер документа-основание")
        page.request.set_date_wl("documentFoundationDate", "05.02.2018", "Дата документа-основания")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Реквизиты получателя
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки \ блок Реквизиты получателя")
        page.request.set_select2_wl("recepientKbk", "РАГС", "КБК получателя")
        page.request.set_select2_wl("recepientOktmo", "город Москва", "Код по ОКТМО Получателя", exactly=False)
        # page.request.save_screenshot("test1", default_folder="C:\\Test\\")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Документ по зачислению невыясненного платежа
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Документ по зачислению невыясненного платежа")
        page.click_by_text("Документ по зачислению невыясненного платежа")
        page.doc.set_text_wl("outstandingPaymentDocumentNumber", "1", "Номер")
        page.doc.set_date_wl("outstandingPaymentDocumentDate", "05.02.2018", "Дата")
        page.doc.set_text_wl("amount", "100.00", "поле Сумма")
        page.doc.set_text_wl("outstandingPaymentDocumentInn", "111", "поле ИНН")
        page.doc.set_text_wl("outstandingPaymentDocumentKpp", "222", "поле КПП")
        # page.doc.save_screenshot("test1", default_folder="C:\\Test\\")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Уполномоченные сотрудники
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Уполномоченные сотрудники")
        page.click_by_text("Уполномоченные сотрудники")
        page.workers.set_select2_wl("chief", "Е.Ю.Петрова", "Руководитель (уполномоченное лицо)", exactly=False)
        page.workers.set_select2_wl("chiefAccountant", "С.В. Васина", "Код по ОКТМО Получателя", exactly=False)
        # page.workers.save_screenshot("test1", default_folder="C:\\Test\\")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Проводки
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Проводки")
        page.click_by_text("Проводки")
        # page.accounting.save_screenshot("test1", default_folder="C:\\Test\\")
        # ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки
        print("ЗАЯВКА НА ВОЗВРАТ \ закладка Расшифровка заявки")
        page.click_by_text("Расшифровка заявки")
        page.request.click_by_text("Сохранить")
        assert page.wait.text_appear("Документ сохранен")
        # assert "" in self.driver.page_source
        print("ЗАЯВКА НА ВОЗВРАТ - ДОКУМЕНТ СОХРАНЕН")
        sleep(10)