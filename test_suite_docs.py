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


    def te1st_getting_cash_request(self):
        page = CashPullRequestPage(self.driver)
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

    def test_znv(self):
        #Документ Заявка на возврат \ шапка документа
        print("Документ Заявка на возврат \ шапка документа")
        page = ZNVPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Заявка на возврат")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        page.set_text_wl("documentNumber", "5", "Номер")
        page.set_date_wl("documentDate", "05.02.2018", "Дата")
        page.set_select2_wl("accountDetails", "14481000320 (Московская обл.)","поле Лицевой счет", exactly=False)
        page.set_select2_wl("recepient", "","Наименование получателя") #exactly=False исп. для точного совпадения
        page.set_text_wl("ofkRegistrationNumber", "05.02.2018", "Номер УФК")
        page.set_date_wl("entryDate", "05.02.2018", "Дата проводки")
        page.set_select2_wl("operation", "Выбытие средств из временного распоряжения","Типовая операция", exactly=False)
        page.set_select2_wl("recepientAccountDetails", "","Банковский счет")
        page.set_select2_wl("documentKind", "Внебанковская заявка на возврат","Вид документа")

        #Документ Заявка на возврат \ закладка Расшифровка заявки
        print("Документ Заявка на возврат \ закладка Расшифровка заявки")
        page.set_text_wl("outstandingPaymentDocumentAmount", "100.00","поле Первоначальная стоимость")
        #page.set_text_wl("ndsPercent", "18","Ставка НДС")
        page.set_text_wl("ndsAmount", "18","Сумма НДС")
        page.set_select2_wl("kbk", "0410 9970092041 244", "КБК", exactly=False)
        page.set_select_wl("kbkType", "Группировочный КБК (гКБК)", "Тип КБК")
        page.set_select2_wl("kosgu", "290", "КОСГУ", exactly=False)
        page.set_select2_wl("costElement", "Прочие расходы", "Вид затрат")

        #Документ Заявка на возврат \ закладка Расшифровка заявки \ Дополнительные реквизиты
        print("Документ Заявка на возврат \ закладка Расшифровка заявки \ Дополнительные реквизиты")
        page.set_text_wl("goalCode", "32", "Код цели")
        page.set_select2_wl("investmentProgram", "Технопарк МФТИ, поселок Северный", "Код объекта по ФАИП")
        page.set_select2_wl("oktmo", "40 333 000", "Код по ОКТМО", exactly=False)
        page.set_select2_wl("expenditureGoalAct", "2008 - Договор", "Мероприятие")
        page.set_select2_wl("department", "Договор подряда", "Группа учета")

        #Документ Заявка на возврат \ закладка Расшифровка заявки \ Информация о платеже
        print("Документ Заявка на возврат \ закладка Расшифровка заявки \ Информация о платеже")

        sleep(20)

        #page.save_screenshot("test1", default_folder="C:\\Test\\")
        #page.click_by_text("Документ по зачислению невыясненного платежа")
        #page.doc.number("55")
        #sleep(1)
