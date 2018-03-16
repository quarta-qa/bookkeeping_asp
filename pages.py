from locators import *


class LoginPage(Browser):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")


class MenuPage(Browser):

    # Выход в меню
    def open(self):
        sleep(1)
        self.click(MenuLocators.menu)

    # Расчеты
    def calculation(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.inner_calculation)
        print("Меню расчеты")
        self.open()

    # Обработка выписки из л/с
    def statement_processing(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.statement_processing)
        print("Обработка выписки из л/с")
        self.open()

    # Выгрузка Сведений о бюджетном обязательстве (загрузка) в формате СУФД ФК (или Электронного бюджета)
    def unloading_information_sufd(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.unloading_informationSUFD)
        print("Выгрузка Сведений о бюджетном обязательстве (загрузка) в формате СУФД ФК (или Электронного бюджета)")
        self.open()

    # Выгрузка Сведений о денежном обязательстве в Электронный бюджет
    def unloading_information(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.unloading_information)
        print("Выгрузка Сведений о денежном обязательстве в Электронный бюджет")
        self.open()

    # Справочники
    def references(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.references)
        print("Меню - Справочники")
        sleep(1)
        self.open()

    # Отчет - Оборотная ведомость
    def turnover_statement(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.turnover_statement)
        print("Отчет - Оборотная ведомость")
        self.open()

    # Отчет - Сводная отчетность
    def summary_reporting(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.summary_reporting)
        print("Отчет - Сводная отчетность")
        self.open()

    # Отчет - Печатные формы
    def printed_forms(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.printed_forms)
        print("Отчет - Печатные формы")
        self.open()

    # Отчет - Остатки НФА
    def remains_nfa(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.remainsNFA)
        print("Отчет - Остатки НФА")
        self.open()

    # АИС «Зарплата.NET»
    def salary(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.salary)
        print("Меню - АИС «Зарплата.NET»")
        self.open()

    # Журнал документов
    def document_journal(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.document_journal)
        print("Журнал документов")
        self.open()

    # Корзина документов
    def recycle_bin(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.recycle_bin)
        print("Корзина документов")
        self.open()

    # Нажать на орла
    def click_to_eagle(self):
        sleep(1)
        self.click(MenuLocators.eagle, "Значок орла")


class CashExpenseRequestPage(Browser):
    # Шапка документа
    @property
    def document_header(self):
        return self.DocumentHeader(self.driver)

    class DocumentHeader(Browser):

        def document_number(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.document_number, value, "Номер документа")

        def document_date(self, value):
            self.set_date(CashExpenseRequestLocators.DocumentHeader.document_date, value, "Дата документа")

        def document_kind(self, value):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.document_kind, value, "Вид документа")

        def ofk_number(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.ofk_number, value, "Номер ОФК")

        def entry_date(self, value):
            self.set_date(CashExpenseRequestLocators.DocumentHeader.entry_date, value, "Дата проводки")

        def operation(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.operation, "Операция")

        def current_organization_account(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.current_organization_account, "Лицевой счет")

        def short(self, value):
            self.set_checkbox(CashExpenseRequestLocators.DocumentHeader.short, value, "Сокращенная")

        def limit_date(self, value):
            self.set_date(CashExpenseRequestLocators.DocumentHeader.limit_date, value, "Предельная дата исполнения")

        def tracking_number(self, value):
            self.set_text(
                CashExpenseRequestLocators.DocumentHeader.tracking_number, value, "Учетный номер обязательства")

        def federal_targeted_investment_program(self):
            self.set_type(
                CashExpenseRequestLocators.DocumentHeader.federal_targeted_investment_program, "Код объекта по ФАИП")

        def priority(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.ofk_number, value, "Приоритет исполнения")

        def currency_amount(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.document_number, value, "Сумма в валюте выплаты")

        def currency_nds_amount(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.document_date, value, "Сумма НДС в валюте")

        def currency_classifier(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.currency_classifier, "Код валюты по ОКВ")

        def amount(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.amount, value, "Сумма в рублях")

        def nds_amount(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.nds_amount, value, "Сумма НДС")

        def amount_without_nds(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.amount_without_nds, value, "Сумма без НДС")

        def is_advance(self, value):
            self.set_checkbox(CashExpenseRequestLocators.DocumentHeader.is_advance, value, "Признак авансового платежа")

        def payment_priority(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.payment_priority, value, "Очередность платежа")

        def payment_form(self):
            self.set_select(CashExpenseRequestLocators.DocumentHeader.payment_form, "Вид платежа")

        def payment_purpose(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.payment_purpose, value, "Назначение платежа")

        def document_foundation(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.document_foundation, "Документ-основание")

        def document_foundation_kind(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.document_foundation_kind, "Вид")

        def document_foundation_number(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.document_foundation_number, value, "Номер")

        def document_foundation_date(self, value):
            self.set_date(CashExpenseRequestLocators.DocumentHeader.document_foundation_date, value, "Дата")

        def document_foundation_subject(self, value):
            self.set_text(CashExpenseRequestLocators.DocumentHeader.document_foundation_subject, value, "Предмет")

        def counterparty(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.counterparty, "Наименование / ФИО")

        def counterparty_account_details(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.counterparty_account_details, "Банковский счет")

        def is_employee(self, value):
            self.set_checkbox(CashExpenseRequestLocators.DocumentHeader.is_employee, value, "Сотрудник")

        def is_tax(self, value):
            self.set_checkbox(CashExpenseRequestLocators.DocumentHeader.is_tax, value, "Налоговый платеж")

        def chief(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.chief, "Руководитель (уполномоченное лицо)")

        def chief_account(self):
            self.set_type(
                CashExpenseRequestLocators.DocumentHeader.chief_account, "Главный бухгалтер (уполномоченное лицо)")

        # Реквизиты документа-основания
        # @property
        # def requisites(self):
        #     return self.Requisites(self.driver)

    # Реквизиты документа-основания
    @property
    def requisites(self):
        return self.Requisites(self.driver)

    class Requisites(Browser):

        def document(self):
            self.set_type(CashExpenseRequestLocators.Requisites.document, "Документ")

        def document_type(self):
            self.set_type(CashExpenseRequestLocators.Requisites.document_type, "Вид")

        def document_number(self):
            self.set_text(CashExpenseRequestLocators.Requisites.document_number, "Номер")

        def document_date(self, value):
            self.set_date(CashExpenseRequestLocators.Requisites.document_date, value, "Дата")

        def subject(self, value):
            self.set_text(CashExpenseRequestLocators.Requisites.subject, value, "Предмет")

    # Расшифровка заявки на кассовый расход
    @property
    def transcript(self):
        return self.Transcript(self.driver)

    class Transcript(Browser):

        def activity_kind(self, value):
            self.set_select(
                CashExpenseRequestLocators.Transcript.activity_kind,
                value, "Наименование вида средств для исполнения обязательства")

        def kbk(self):
            self.set_type(CashExpenseRequestLocators.Transcript.kbk, "Код по БК плательщика")

        def drawee_kbk_type(self, value):
            self.set_select(CashExpenseRequestLocators.Transcript.drawee_kbk_type, value, "Тип КБК плательщика")

        def kosgu(self):
            self.set_type(CashExpenseRequestLocators.Transcript.kosgu, "КОСГУ")

        def cost_element(self):
            self.set_type(CashExpenseRequestLocators.Transcript.cost_element, "Вид затрат")

        def recepient_kbk(self):
            self.set_type(CashExpenseRequestLocators.Transcript.recepient_kbk, "Код по БК получателя")

        def recepient_kbk_type(self):
            self.set_select(CashExpenseRequestLocators.Transcript.recepient_kbk_type, "Тип КБК Получателя")

        def goal_code(self):
            self.set_type(CashExpenseRequestLocators.Transcript.goal_code, "Код цели (аналитический код)")

        def department(self):
            self.set_type(CashExpenseRequestLocators.Transcript.department, "Подразделение")

        def expenditure_goal_act(self):
            self.set_type(CashExpenseRequestLocators.Transcript.expenditure_goal_act, "Мероприятие")

        def document_foundation_counterparty(self):
            self.set_type(
                CashExpenseRequestLocators.Transcript.document_foundation_counterparty,
                "Организация для Документа - основания")

        def foundation(self):
            self.set_type(CashExpenseRequestLocators.Transcript.foundation, "Документ основания")

        def report_code(self):
            self.set_type(CashExpenseRequestLocators.Transcript.report_code, "Код для отчетности")

        def operation(self):
            self.set_type(CashExpenseRequestLocators.Transcript.operation, "Операция")

        def currency_amount(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.currency_amount, value, "Сумма в валюте заявки")

        def currency_nds_amount(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.currency_nds_amount, value, "Сумма НДС в валюте")

        def amount(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.amount, value, "Сумма в рублях")

        def nds_amount(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.nds_amount, value, "Сумма НДС")

        def amount_without_nds(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.amount_without_nds, value, "Сумма без НДС")

        def nds_percent(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.nds_percent, value, "% НДС")

        def payment_purpose(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.payment_purpose, value, "Назначение платежа")

        def comment(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.comment, value, "Примечание")

        def drawee_subsidy_code(self, value):
            self.set_text(CashExpenseRequestLocators.Transcript.drawee_subsidy_code, value, "Код субсидии плательщика")

        def recepient_subsidy_code(self, value):
            self.set_text(
                CashExpenseRequestLocators.Transcript.recepient_subsidy_code, value, "Код субсидии получателя")

        def act(self):
            self.set_type(CashExpenseRequestLocators.Transcript.act, "Мероприятие по БР")


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


class ZNVPage(Browser):
    @property
    def request(self):
        return self.Request(self.driver)

    @property
    def doc(self):
        return self.Doc(self.driver)

    @property
    def workers(self):
        return self.Workers(self.driver)

    @property
    def accounting(self):
        return self.Accounting(self.driver)

    class Request(Browser):
        pass

    class Doc(Browser):
        pass

    class Workers(Browser):
        pass

    class Accounting(Browser):
        pass


class PKOPage(Browser):
    @property
    def line(self):
        return self.Line(self.driver)

    class Line(Browser):
        pass


class ZKRPage(Browser):
    @property
    def request(self):
        return self.Request(self.driver)

    class Request(Browser):
        pass

    @property
    def doc(self):
        return self.Doc(self.driver)

    class Doc(Browser):
        pass

    @property
    def bid(self):
        return self.Bid(self.driver)

    class Bid(Browser):
        pass


# Проведение документов
class CarryingOutOfDocumentsPage(Browser):
    def lddate_prov(self, value):
        self.set_date(CarryingOutOfDocumentsLocators.lddate_prov, value, "Дата проводки")

    def operation_master(self, value):
        self.set_select2(CarryingOutOfDocumentsLocators.operation_master, value, "Типовая операция")


# Экспорт в УФК
class ExportUFKPage(Browser):
    def account_details(self, value):
        self.set_select2(ExportUFKLocators.account_details, value, "Банк", exactly=False)

    def file_number(self, value):
        self.set_text(ExportUFKLocators.file_number, value, "Порядковый № файла")


# оборотная ведомость
class TurnoverStatementPage(Browser):
    def date_from(self, value):
        self.set_date(TurnoverStatementLocators.date_from, value, "Период с")

    def date_to(self, value):
        self.set_date(TurnoverStatementLocators.date_to, value, "по")

    def balance_sheet_account(self, value):
        self.set_select2(TurnoverStatementLocators.balance_sheet_account, value, "Счет")

    def balance_sheet_account_group(self, value):
        self.set_select2(TurnoverStatementLocators.balance_sheet_account_group, value, "Группа счетов")

    def account_unit(self, value):
        self.set_select(TurnoverStatementLocators.account_unit, value, "Единица измерения")

    def is_only_out_balance(self, value):
        self.set_checkbox(TurnoverStatementLocators.is_only_out_balance, value, "По забалансовым счетам")


# Приходно кассовый ордер
class IncomingOrderPage(Browser):
    def document_kind(self, value):
        self.set_select2(IncomingOrderLocators.document_kind, value, "Вид документа")

    def document_number(self, value):
        self.set_text(IncomingOrderLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(IncomingOrderLocators.document_date, value, "Дата")

    def employee(self, value):
        self.set_select2(IncomingOrderLocators.employee, value, "Сотрудник")

    def organization(self, value):
        self.set_select2(IncomingOrderLocators.organization, value, "Организация")

    def received_from(self, value):
        self.set_text(IncomingOrderLocators.received_from, value, "Принято от")

    def department_unit(self, value):
        self.set_select2(IncomingOrderLocators.department_unit, value, "Группа учета")

    def cash_report_number(self, value):
        self.set_text(IncomingOrderLocators.cash_report_number, value, "Номер кассового отчета")

    def foundation(self, value):
        self.set_text(IncomingOrderLocators.foundation, value, "Основание")

    def operation(self, value):
        self.set_select2(IncomingOrderLocators.operation, value, "Типовая операция")


# Добавление строки в ПКО
class IncomingOrderAddLinePage(Browser):
    def operation(self, value):
        self.set_select2(IncomingOrderAddLineLocators.operation, value, "Типовая операция")

    def kbk(self, value):
        self.set_select2(IncomingOrderAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(IncomingOrderAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def expense_type(self, value):
        self.set_select2(IncomingOrderAddLineLocators.expense_type, value, "Вид затрат")

    def inventory(self, value):
        self.set_select2(IncomingOrderAddLineLocators.inventory, value, "Номенклатура")

    def quantity(self, value):
        self.set_text(IncomingOrderAddLineLocators.quantity, value, "Количество")

    def amount(self, value):
        self.set_text(IncomingOrderAddLineLocators.amount, value, "Сумма")

    def amount_without_nds(self, value):
        self.set_text(IncomingOrderAddLineLocators.amount_without_nds, value, "Сумма без НДС")

    def nds_percent(self, value):
        self.set_text(IncomingOrderAddLineLocators.nds_percent, value, "Ставка НДС")

    def nds_amount(self, value):
        self.set_text(IncomingOrderAddLineLocators.nds_amount, value, "Сумма НДС")

    def department_unit(self, value):
        self.set_select2(IncomingOrderAddLineLocators.department_unit, value, "Группа учета")

    def recepient(self, value):
        self.set_select2(IncomingOrderAddLineLocators.recepient, value, "Получатель (МОЛ)")

    def comment(self, value):
        self.set_text(IncomingOrderAddLineLocators.comment, value, "Комментарий")

    def act(self, value):
        self.set_select2(IncomingOrderAddLineLocators.act, value, "Мероприятие")

    def cash_transaction_code(self, value):
        self.set_select(IncomingOrderAddLineLocators.cash_transaction_code, value, "Кассовый символ")


# Заявка на кассовый расход
class ApplicationCashFlowPage(Browser):

    def documen_type(self, value):
        self.set_select2(ApplicationCashFlowLocators.documen_type, value, "Вид документа")

    def number(self, value):
        self.set_text(ApplicationCashFlowLocators.number, value, "Номер")

    def date(self, value):
        self.set_date(ApplicationCashFlowLocators.date, value, "Дата")

    def personal_account(self, value):
        self.set_select2(ApplicationCashFlowLocators.personal_account, value, "Лицевой счет", exactly=False)

    def bank_account_number(self, value):
        self.set_select2(ApplicationCashFlowLocators.bank_account_number, value, "Банковский счет", exactly=False)

    def recipient(self, value):
        self.set_select2(ApplicationCashFlowLocators.recipient, value, "Наименование контрагента или ФИО")

    def number_ufk(self, value):
        self.set_text(ApplicationCashFlowLocators.number_ufk, value, "Номер УФК")

    def limit_date(self, value):
        self.set_date(ApplicationCashFlowLocators.limit_date, value, "Предельная дата исполнения")

    def foundation(self, value):
        self.set_select2(ApplicationCashFlowLocators.foundation, value, "Документ-основание", exactly=False)

    def operation(self, value):
        self.set_select2(ApplicationCashFlowLocators.operation, value, "Типовая операция", exactly=False)


# Заявка на кассовый расход добавление строки
class DecodingOfTheApplicationPage(Browser):
    def operation(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.operation, value, "Типовая операция")

    def kbk(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.cost_element, value, "Вид затрат")

    def amount(self, value):
        self.set_text(DecodingOfTheApplicationLocators.amount, value, "Сумма в рублях")

    def nds_percent(self, value):
        self.set_text(DecodingOfTheApplicationLocators.nds_percent, value, "Ставка НДС")

    def document_foundation_counterparty(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.document_foundation_counterparty, value,
                         "Организация для документа-основания")

    def foundation(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.foundation, value, "Документ-основание", exactly=False)

    def comment(self, value):
        self.set_text(DecodingOfTheApplicationLocators.comment, value, "Примечание")

    def drawee_kbk_type(self, value):
        self.set_select(DecodingOfTheApplicationLocators.draweeKbkType, value, "Тип КБК плательщика")


#  Заявка на возврат
class ReturnRequestPage(Browser):
    def document_number(self, value):
        self.set_text(ReturnRequestLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(ReturnRequestLocators.document_date, value, "Дата")

    def account_details(self, value):
        self.set_select2(ReturnRequestLocators.account_details, value, "Лицевой счет", exactly=False)

    def recepient(self, value):
        self.set_select2(ReturnRequestLocators.recepient, value, "Наименование получателя")

    def ofk_registration_number(self, value):
        self.set_text(ReturnRequestLocators.ofk_registration_number, value, "Номер УФК")

    def entry_date(self, value):
        self.set_date(ReturnRequestLocators.entry_date, value, "Дата проводки")

    def operation(self, value):
        self.set_select2(ReturnRequestLocators.operation, value, "Типовая операция")

    def recepient_account_details(self, value):
        self.set_select2(ReturnRequestLocators.recepient_account_details, value, "Банковский счет", exactly=False)

    def kbk(self, value):
        self.set_select2(ReturnRequestLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ReturnRequestLocators.kosgu, value, "КОСГУ", exactly=False)

    def kbk_type(self, value):
        self.set_select2(ReturnRequestLocators.kbk_type, value, "Тип КБК")

    def cost_element(self, value):
        self.set_select2(ReturnRequestLocators.cost_element, value, "Вид затрат")

    def outstanding_payment_document_amount(self, value):
        self.set_text(ReturnRequestLocators.outstanding_payment_document_amount, value,
                      "Сумма в рублях")

    def nds_percent(self, value):
        self.set_text(ReturnRequestLocators.nds_percent, value, "Ставка НДС")

    def nds_amount(self, value):
        self.set_text(ReturnRequestLocators.nds_amount, value, "ndsAmount")

    def chief(self, value):
        self.set_select2(ReturnRequestLocators.chief, value, "Руководитель (уполномоченное лицо)", exactly=False)

    def chief_accountant(self, value):
        self.set_select2(
            ReturnRequestLocators.chief_accountant, value, "Главный бухгалтер (уполномоченное лицо)", exactly=False)


# Заявка на получение наличных денег
class ApplicationForCashWithdrawalPage(Browser):
    def document_number(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(ApplicationForCashWithdrawalLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(ApplicationForCashWithdrawalLocators.entry_date, value, "Дата проводки")

    def deadline(self, value):
        self.set_date(ApplicationForCashWithdrawalLocators.deadline, value, "Предельная дата исполнения")

    def account_details(self, value):
        self.set_select2(ApplicationForCashWithdrawalLocators.account_details, value, "Лицевой счет", exactly=False)

    def tracking_number(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.tracking_number, value, "Учетный номер обязательства")

    def operation_master(self, value):
        self.set_select2(
            ApplicationForCashWithdrawalLocators.operation_master, value, "Типовая операция", exactly=False)

    def trustee(self, value):
        self.set_select2(ApplicationForCashWithdrawalLocators.trustee, value, "Доверенное лицо")

    def trustee_name_dative_case(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.trustee_name_dative_case, value, "ФИО в дательном падеже")

    def trustee_position(self, value):
        self.set_select2(ApplicationForCashWithdrawalLocators.trustee_position, value, "Должность")

    def trustee_position_dative_case(self, value):
        self.set_text(
            ApplicationForCashWithdrawalLocators.trustee_position_dative_case, value, "Должность в дательном падеже")

    def chief(self, value):
        self.set_select2(ApplicationForCashWithdrawalLocators.chief, value, "Руководитель", exactly=False)

    def accountant_general(self, value):
        self.set_select2(
            ApplicationForCashWithdrawalLocators.accountant_general, value, "Главный бухгалтер", exactly=False)

    def foundation(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.foundation, value, "Основание")

    def check_series(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.check_series, value, "Серия чека")

    def check_number(self, value):
        self.set_text(ApplicationForCashWithdrawalLocators.check_number, value, "Номер чека")

    def check_date(self, value):
        self.set_date(ApplicationForCashWithdrawalLocators.check_date, value, "Дата чека")

    def check_valid_till(self, value):
        self.set_date(ApplicationForCashWithdrawalLocators.check_valid_till, value, "Срок действия чека")


# Заявка на получение наличных денег добавление строки
class ApplicationForCashWithdrawalAddLinePage(Browser):
    def kbk(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.cost_element, value, "Вид затрат")

    def cash_transaction_code(self, value):
        self.set_select(ApplicationForCashWithdrawalAddLineLocators.cash_transaction_code, value,
                        "Вид средств для исполнения обязательств")

    def funds_source(self, value):
        self.set_select(ApplicationForCashWithdrawalAddLineLocators.funds_source, value, "Кассовый символ")

    def amount(self, value):
        self.set_text(ApplicationForCashWithdrawalAddLineLocators.amount, value, "Сумма")

    def payment_purpose(self, value):
        self.set_text(ApplicationForCashWithdrawalAddLineLocators.payment_purpose, value, "Назначение платежа")

    def comment(self, value):
        self.set_text(ApplicationForCashWithdrawalAddLineLocators.comment, value, "Примечание")


# Договор с поставщиком
class ContractWithSupplierPage(Browser):
    def document_type(self, value):
        self.set_select2(ContractWithSupplierLocators.documen_type, value, "Вид документа")

    def number(self, value):
        self.set_text(ContractWithSupplierLocators.number, value, "Номер документа")

    def date(self, value):
        self.set_date(ContractWithSupplierLocators.date, value, "Дата создания документа")

    def сounterparty(self, value):
        self.set_select2(ContractWithSupplierLocators.сounterparty, value, "Контрагент")

    def bank_account_number(self, value):
        self.set_select2(
            ContractWithSupplierLocators.bank_account_number, value, "Номер банковского счета", exactly=False)

    def uin(self, value):
        self.set_text(ContractWithSupplierLocators.uin, value, "УИН")

    def currency(self, value):
        self.set_select2(ContractWithSupplierLocators.currency, value, "Валюта")

    def date_begin(self, value):
        self.set_date(ContractWithSupplierLocators.date_begin, value, "Дата начала")

    def date_end(self, value):
        self.set_date(ContractWithSupplierLocators.date_end, value, "Дата окончания")

    def payment_type(self, value):
        self.set_select(ContractWithSupplierLocators.payment_type, value, "Вид оплаты")

    def subject_contract(self, value):
        self.set_text(ContractWithSupplierLocators.subject_contract, value, "Предмет договора")

    def payment_terms(self, value):
        self.set_text(ContractWithSupplierLocators.payment_terms, value, "Условие оплаты")

    def note(self, value):
        self.set_text(ContractWithSupplierLocators.note, value, "Примечание")


# Договор с Поставщиком - добавление строки
class ContractWithSupplierPageDetailKBK(Browser):

    def financial_year(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.financial_year, value, "Финансовый год")

    def entry_date(self, value):
        self.set_date(ContractWithSupplierDetailKBKPageLocators.entry_date, value, "Дата проводки")

    def operation(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.operation, value, "Типовая операция")

    def kbk(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.kosgu, value, "КОСГУ", exactly=False)

    def contract_subject(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.contract_subject, value, "Предмет договора")

    def amounts_amount(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.amounts_amount, value, "Сумма по договору с НДС")

    def amounts_nds_percent(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.amounts_nds_percent, value, "% НДС")

    def advance(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.advance, value, "Сумма аванса")

    def cost_element(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.cost_Element, value, "Вид затрат")


# Справочники - Картотека ОС,НМА,НПА - добавление документа
class CardIndexOSNMANPAPage(Browser):

    def tag_no_first_part(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no_first_part, value, "Первая часть инвентарного номера")

    def tag_no_second_part(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no_second_part, value, "Вторая часть инвентарного номера")

    def tag_no(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no, value, ">>>")

    def full_name(self, value):
        self.set_text(CardIndexOSNMANPALocators.full_name, value, "Полное наименование")

    def property_designation(self, value):
        self.set_text(CardIndexOSNMANPALocators.property_designation, value, "Назначение объекта")

    def start_up_date(self, value):
        self.set_date(CardIndexOSNMANPALocators.start_up_date, value, "Дата ввода в эксплуатацию")

    def unit_of_measure(self, value):
        self.set_select2(CardIndexOSNMANPALocators.unit_of_measure, value, "Единица измерения")

    # Согласно сценарию на портале должно быть поле - Pull Down - "Папка"

    def cost(self, value):
        self.set_text(CardIndexOSNMANPALocators.cost, value, "Первоначальная стоимость")

    def value_added_used(self, value):
        self.set_text(CardIndexOSNMANPALocators.value_added_used, value, "Срок полезного использования (месяцев)")

    def okof(self, value):
        self.set_select2(CardIndexOSNMANPALocators.okof, value, "ОКОФ")

    def amortization_group(self, value):
        self.set_select2(CardIndexOSNMANPALocators.amortization_group, value, "Амортизационная группа")

    def serial_number(self, value):
        self.set_text(CardIndexOSNMANPALocators.serialNumber, value, "Серийный №")

    def group(self, value):
        self.set_select2(CardIndexOSNMANPALocators.group, value, "Группа ОС, НМА, НПА")


# счет от поставщика
class InvoiceFromTheSupplierPage(Browser):
    def document_number(self, value):
        self.set_text(InvoiceFromTheSupplierLocators.document_number, value, "Номер документа")

    def document_date(self, value):
        self.set_date(InvoiceFromTheSupplierLocators.document_date, value, "Дата")

    def supplier(self, value):
        self.set_select2(InvoiceFromTheSupplierLocators.supplier, value, "Постащик")

    def supplier_account_detail(self, value):
        self.set_select2(
            InvoiceFromTheSupplierLocators.supplier_account_detail, value, "Номер банковского счета", exactly=False)

    def account_details(self, value):
        self.set_select2(InvoiceFromTheSupplierLocators.account_details, value, "Заказчик Лицевой счет", exactly=False)

    def department(self, value):
        self.set_select2(InvoiceFromTheSupplierLocators.department, value, "Подразделение")

    def note(self, value):
        self.set_text(InvoiceFromTheSupplierLocators.note, value, "Примечание")


# счет от поставщика добавление строки
class InvoiceFromTheSupplierAddLinePage(Browser):
    def add(self):
        self.click(InvoiceFromTheSupplierAddLineLocators.add,  "add")

    def add_new(self):
        self.click(InvoiceFromTheSupplierAddLineLocators.add_new, "addNew")

    def kbk(self, value):
        self.set_select2(InvoiceFromTheSupplierAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(InvoiceFromTheSupplierAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(InvoiceFromTheSupplierAddLineLocators.cost_element, value, "Вид затрат")

    def comment(self, value):
        self.set_text(InvoiceFromTheSupplierAddLineLocators.comment, value, "Примечание")

    def amount(self, value):
        self.set_text(InvoiceFromTheSupplierAddLineLocators.amount, value, "Сумма к оплате")

    def vat_percent(self, value):
        self.set_text(InvoiceFromTheSupplierAddLineLocators.vat_percent, value, "Ставка НДС")


# Справочники - Шаблоны карточки ОС, НМА, НПА - добавление документа
class TemplatesofthecardOSNMANPA(Browser):
        print("Templates_of_the_card_OSNMANPA")


# Справочники - Материально - ответственные лица
class MateriallyResponsiblePerson(Browser):
        print("Materially_responsible_person")


# Учет нефинансовых активов - Поступление НФА - шапка документа
class ReceiptOfNonFinancialAssets(Browser):
    print("Receipt_of_non_financial_assets")


# Учет нефинансовых активов - Поступление НФА - строка документа
class ReceiptOfNonFinancialAssetsLine(Browser):
    print("Receipt_of_non_financial_assets_line")


# Массовое заполнение параметров ОС
class MassFillingOfOSParameters(Browser):
    print("Mass_filling_of_OS_parameters")
