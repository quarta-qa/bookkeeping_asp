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
        page = ZNVPage(self.driver)
        page.scroll_to_bottom()
        page.click_by_text("Заявка на возврат")
        page.click_by_text("Добавить")
        page.click_by_text("Новый документ")
        #page.document_number("5")
        page.set_text_wl("documentNumber", "5", "Номер")
        #page.document_date("05.02.2018")
        page.set_date_wl("documentDate", "05.02.2018", "Дата")
     #   page.personal_account("14481000320 (Московская обл.)")
        page.set_select2_wl("accountDetails", "14481000320 (Московская обл.)","поле Лицевой счет", exactly=False)
        ## page.recipient_name("")
     #   page.ofk_registration_number("2")
     #   page.entry_date("05.09.2017")
     #   page.typical_operation("Выбытие средств из временного распоряжения")
        ## page.recipient_account("")
     #   page.document_type("Внебанковская заявка на возврат")
        sleep(20)
        #page.request.summa_rub("100.00")
        #page.request.kbk("0410 9970092041 244")
        #page.request.kosgu("290")
        #page.request.stavka_nds("13")
        #page.request.tip_kbk("Группировочный КБК (гКБК)")
        #page.request.vid_zatrat("Прочие расходы")
        #page.request.summa_nds("113.00")
        #page.request.oktmo("80 606 416")
        #page.save_screenshot("test1", default_folder="C:\\Test\\")
        #page.click_by_text("Документ по зачислению невыясненного платежа")
        #page.doc.number("55")
        #sleep(1)
        #page.save_screenshot("test2", default_folder="C:\\Test\\")