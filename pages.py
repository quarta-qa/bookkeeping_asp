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

    # Обработка выписки из л/с (НЕ РЕАЛИЗОВАН ФУНКЦИОНАЛ)
    def statement_processing(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.statement_processing)
        print("Обработка выписки из л/с")

    # Выгрузка Сведений о бюджетном обязательстве (загрузка) в формате СУФД ФК (или Электронного бюджета)
    def unloading_information_sufd(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.unloading_informationSUFD)
        print("Выгрузка Сведений о бюджетном обязательстве (загрузка) в формате СУФД ФК (или Электронного бюджета)")
        # sleep(1)
        # self.click(MenuLocators.calculation)
        # self.open()

    # Выгрузка Сведений о денежном обязательстве в Электронный бюджет (НЕ РЕАЛИЗОВАН ФУНКЦИОНАЛ)
    def unloading_information(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.unloading_information)
        print("Выгрузка Сведений о денежном обязательстве в Электронный бюджет")
        # sleep(1)
        # self.click(MenuLocators.calculation)
        # self.open()

    # Расчеты
    def calculation(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.calculation)
        sleep(1)
        self.click(MenuLocators.inner_calculation)
        print("Меню расчеты")
        # sleep(1)
        # self.click(MenuLocators.calculation)
        # self.open()

    # Журнал документов
    def document_journal(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.document_journal)
        print("Журнал документов")
        # self.open()

    # Корзина документов
    def recycle_bin(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.recycle_bin)
        print("Корзина документов")
        self.open()

    # Справочники
    def references(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.references)
        print("Меню - Справочники")
        # sleep(1)
        # self.open()

    # Отчет - Оборотная ведомость
    def turnover_statement(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.turnover_statement)
        print("Отчет - Оборотная ведомость")

    # Отчет - Сводная отчетность (НЕ РЕАЛИЗОВАН ФУНКЦИОНАЛ)
    def summary_reporting(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.summary_reporting)
        print("Отчет - Сводная отчетность")

    # Отчет - Печатные формы
    def printed_forms(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.printed_forms)
        print("Отчет - Печатные формы")
        # sleep(1)
        # self.click(MenuLocators.report)
        # self.open()

    # Отчет - Остатки НФА
    def remains_nfa(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.report)
        sleep(1)
        self.click(MenuLocators.remains_NFA)
        print("Отчет - Остатки НФА")

    # АИС «Зарплата.NET» (НЕ РЕАЛИЗОВАН ФУНКЦИОНАЛ)
    def salary(self):
        self.open()
        sleep(1)
        self.click(MenuLocators.salary)
        print("Меню - АИС «Зарплата.NET»")

    # Нажать на орла
    def click_to_eagle(self):
        sleep(1)
        self.click(MenuLocators.eagle, "Значок орла")


# Нажать на раздел из справочника
class ClickOnTheSectionFromTheDirectory(Browser):
    # Учет нефинансовых активов
    def objects_os_nma_npa(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.objects_os_nma_npa, "Нажать на Оъекты ОС,НМА,НПА")

    def group_os_nma_npa(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.group_os_nma_npa, "Нажать на Группы ОС, НМА, НПА")

    def objects_mz(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.objects_mz, "Нажать на Объекты МЗ")

    def group_mz(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.group_mz, "Нажать на Группы МЗ")

    def materially_responsible_person(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.materially_responsible_person,
                   "Нажать на Материально ответственные лица")

    def storage(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.storage, "Нажать на Места хранения")

    def okof(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.okof, "Нажать на ОКОФ")

    def ofof_2017(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.okof, "Нажать на ОКОФ (2017)")

    def templates_of_the_card_os_nma_npa(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.templates_of_the_card_os_nma_npa,
                   "Нажать на Шаблоны карточки ОС, НМА, НПА")

    def ifns(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.ifns, "Нажать на ИФНС")

    def commission_orders(self):
        self.click(ClickOnTheSectionFromTheDirectoryLocators.commission_orders,
                   "Нажать на Приказы о назначении комиссии")


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


# Журнал проводок
class PostingJournalPage(Browser):
    def date_from(self, value):
        self.set_date(PostingJournalLocators.date_from, value, "Дата проводки с")

    def date_by(self, value):
        self.set_date(PostingJournalLocators.date_by, value, "Дата проводки по")

    def balance_sheet_account(self, value):
        self.set_select2(PostingJournalLocators.balance_sheet_account, value, "Счет")

    def balance_sheet_account_group(self, value):
        self.set_select2(PostingJournalLocators.balance_sheet_account_group, value, "Группа счетов")


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


#  Основание для выдачи подотчетных сумм
class BasisForReportingAmountsPage(Browser):
    def number(self, value):
        self.set_text(BasisForReportingAmountsLocators.number, value, "Номер")

    def document_date(self, value):
        self.set_date(BasisForReportingAmountsLocators.document_date, value, "Дата")

    def document_kind(self, value):
        self.set_select2(BasisForReportingAmountsLocators.document_kind, value, "Вид документа")

    def employee(self, value):
        self.set_select2(BasisForReportingAmountsLocators.employee, value, "Сотрудник")

    def position(self, value):
        self.set_select2(BasisForReportingAmountsLocators.position, value, "Должность")

    def department(self, value):
        self.set_select2(BasisForReportingAmountsLocators.department, value, "Подразделение")

    def trip_start_date(self, value):
        self.set_date(BasisForReportingAmountsLocators.trip_start_date, value, "Дата начала")

    def trip_end_date(self, value):
        self.set_date(BasisForReportingAmountsLocators.trip_end_date, value, "Дата окончания")

    def comment(self, value):
        self.set_text(BasisForReportingAmountsLocators.comment, value, "Комментарий")

    def trip_route(self, value):
        self.set_text(BasisForReportingAmountsLocators.trip_route, value, "Маршрут")


#  Основание для выдачи подотчетных сумм добавление строк
class BasisForReportingAmountsAddLinePage(Browser):
    def kbk(self, value):
        self.set_select2(BasisForReportingAmountsAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(BasisForReportingAmountsAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(BasisForReportingAmountsAddLineLocators.cost_element, value, "Вид затрат")

    def employee(self, value):
        self.set_select2(BasisForReportingAmountsAddLineLocators.employee, value, "Сотрудник")

    def position(self, value):
        self.set_select2(BasisForReportingAmountsAddLineLocators.position, value, "Должность" )

    def amount(self, value):
        self.set_text(BasisForReportingAmountsAddLineLocators.amount, value, "Сумма")

    def comment(self, value):
        self.set_text(BasisForReportingAmountsAddLineLocators.comment, value, "Комментарий")


# Приходный кассовый ордер
class IncomingOrderPage(Browser):
    def document_kind(self, value):
        self.set_select2(IncomingOrderLocators.document_kind, value, "Вид документа")

    def document_number(self, value):
        self.set_text(IncomingOrderLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(IncomingOrderLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(IncomingOrderLocators.entry_date, value, "entryDate")

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


# Добавление строки в Приходный кассовый ордер
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


# Добавление приложения в Приходный кассовый ордер
class IncomeCashOrderPlusPage(Browser):
    def document_foundation(self, value):
        self.set_select2(IncomeCashOrderPlusLocators.document_foundation, value, "documentFoundation")

    def advance_report(self, value):
        self.set_select2(IncomeCashOrderPlusLocators.advance_report, value, "advanceReport")

    def comment(self, value):
        self.set_text(IncomeCashOrderPlusLocators.comment, value, "comment")

    def chief_accountant(self, value):
        self.set_select2(IncomeCashOrderPlusLocators.chief_accountant, value, "chiefAccountant")

    def cashier(self, value):
        self.set_select2(IncomeCashOrderPlusLocators.cashier, value, "cashier")


# Авансовый отчет
class AvansReportPage(Browser):
    def document_kind(self, value):
        self.set_select2(AvansReportLocators.document_kind, value, "Вид документа")

    def document_number(self, value):
        self.set_text(AvansReportLocators.document_number, value, "Номер документа")

    def document_date(self, value):
        self.set_date(AvansReportLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(AvansReportLocators.entry_date, value, "Дата проводки")

    def employee(self, value):
        self.set_select2(AvansReportLocators.employee, value, "Сотрудник")

    def position(self, value):
        self.set_select2(AvansReportLocators.position, value, "Должность")

    def department(self, value):
        self.set_select2(AvansReportLocators.department, value, "Подразделение")

    def employee_full_name(self, value):
        self.set_text(AvansReportLocators.employee_full_name, value, "ФИО")

    def document_foundation(self, value):
        self.set_select2(AvansReportLocators.document_foundation, value, "Основание")

    def purpose(self, value):
        self.set_text(AvansReportLocators.purpose, value, "Назначение аванса")

    def comment(self, value):
        self.set_text(AvansReportLocators.comment, value, "Комментарий")


# Авансовый отчет добавление строки
class AvansReportAddLinePage(Browser):
    def operation_master(self, value):
        self.set_select2(AvansReportAddLineLocators.operation_master, value, "Типовая операция")

    def kbk(self, value):
        self.set_select2(AvansReportAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(AvansReportAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(AvansReportAddLineLocators.cost_element, value, "Вид затрат")

    def document_date(self, value):
        self.set_date(AvansReportAddLineLocators.document_date, value, "Дата")

    def document_number(self, value):
        self.set_text(AvansReportAddLineLocators.document_number, value, "Номер")

    def amount(self, value):
        self.set_text(AvansReportAddLineLocators.amount, value, "Сумма")

    def comment(self, value):
        self.set_text(AvansReportAddLineLocators.comment, value, "Комментарий")


# Заявка на кассовый расход
class ApplicationCashFlowPage(Browser):

    def documen_type(self, value):
        self.set_select2(ApplicationCashFlowLocators.documen_type, value, "Вид документа")

    def number(self, value):
        self.set_text(ApplicationCashFlowLocators.number, value, "Номер")

    def date(self, value):
        self.set_date(ApplicationCashFlowLocators.date, value, "Дата")

    def entry_date(self, value):
        self.set_date(ApplicationCashFlowLocators.entry_date, value, "Дата проводки")

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

    def is_employee(self, value):
        self.set_checkbox(ApplicationCashFlowLocators.is_employee, value, "Сотрудник чек-бокс")

    def employee(self, value):
        self.set_select2(ApplicationCashFlowLocators.employee, value, "Сотрудник")

    def imprest_foundation(self, value):
        self.set_select2(ApplicationCashFlowLocators.imprest_foundation, value, "Основание для выдачи в подотчет")

    def advance_report(self, value):
        self.set_select2(ApplicationCashFlowLocators.advance_report, value, "Авансовый отчет")

    def foundation(self, value):
        self.set_select2(ApplicationCashFlowLocators.foundation, value, "Документ-основание", exactly=False)

    def tracking_number(self, value):
        self.set_text(ApplicationCashFlowLocators.tracking_number, value, "Учетный номер обязательства")

    def document_foundaiont_kind(self, value):
        self.set_select2(ApplicationCashFlowLocators.document_foundaiont_kind, value, "Вид документа-основания")

    def document_foundation_number(self, value):
        self.set_text(ApplicationCashFlowLocators.document_foundation_number, value, "Номер")

    def document_foundation_date(self, value):
        self.set_date(ApplicationCashFlowLocators.document_foundation_date, value, "Дата")

    def document_foundation_subject(self, value):
        self.set_text(ApplicationCashFlowLocators.document_foundation_subject, value, "Предмет")

    def operation(self, value):
        self.set_select2(ApplicationCashFlowLocators.operation, value, "Типовая операция", exactly=False)

    def currency(self, value):
        self.set_select2(ApplicationCashFlowLocators.currency, value, "Код валюты по ОКВ")

    def department_unit(self, value):
        self.set_select2(ApplicationCashFlowLocators.department_unit, value, "Группа учета")

    def investment_program(self, value):
        self.set_select2(ApplicationCashFlowLocators.investment_program, value, "Код объекта по ФАИП")

    def priority(self, value):
        self.set_text(ApplicationCashFlowLocators.priority, value, "Приоритет исполнения")

    def is_advance(self, value):
        self.set_checkbox(ApplicationCashFlowLocators.is_advance, value, "Авансовый платеж")

    def priority_of_payment(self, value):
        self.set_text(ApplicationCashFlowLocators.priority_of_payment, value, "Очередность платежа")

    def payment_type(self, value):
        self.set_select(ApplicationCashFlowLocators.payment_type, value, "Вид платежа")

    def payment_purpose(self, value):
        self.set_text(ApplicationCashFlowLocators.payment_purpose, value, "Назначение платежа")

    def chief(self, value):
        self.set_select2(ApplicationCashFlowLocators.chief, value, "Руководитель")

    def accountant_general(self, value):
        self.set_select2(ApplicationCashFlowLocators.accountant_general, value, "Главный бухгалтер")


# Заявка на кассовый расход добавление строки
class DecodingOfTheApplicationPage(Browser):
    def activity_kind(self, value):
        self.set_select(DecodingOfTheApplicationLocators.activity_kind, value, "Вид средств")

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

    def recepient_kbk(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.recepient_kbk, value, "КБК получателя")

    def recepient_kbk_type(self, value):
        self.set_select(DecodingOfTheApplicationLocators.recepient_kbk_type, value, "Тип КБК Получателя")

    def department(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.department, value, "Группа учета")

    def expenditure_goal_act(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.expenditure_goal_act, value, "Мероприятие")

    def document_foundation_counterparty(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.document_foundation_counterparty, value,
                         "Организация для документа-основания")

    def foundation(self, value):
        self.set_select2(DecodingOfTheApplicationLocators.foundation, value, "Документ-основание", exactly=False)

    def payment_purpose(self, value):
        self.set_text(DecodingOfTheApplicationLocators.payment_purpose, value, "Назначение платежа")

    def comment(self, value):
        self.set_text(DecodingOfTheApplicationLocators.comment, value, "Примечание")

    def drawee_kbk_type(self, value):
        self.set_select(DecodingOfTheApplicationLocators.draweeKbkType, value, "Тип КБК плательщика")

    def type_of_funds(self, value):
        self.set_select(DecodingOfTheApplicationLocators.typeOfFunds, value, "Тип КБК плательщика")


# Заявка на кассовый расход - реквизиты документа основания
class ApplicationCashFlowRequisitesPage(Browser):
    def document(self, value):
        self.set_select2(ApplicationCashFlowRequisitesLocators.document, value, "Документ-основание")

    def document_type(self, value):
        self.set_select2(ApplicationCashFlowRequisitesLocators.document_type, value, "Вид")

    def document_number(self, value):
        self.set_text(ApplicationCashFlowRequisitesLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(ApplicationCashFlowRequisitesLocators.document_date, value, "Дата")

    def subject(self, value):
        self.set_text(ApplicationCashFlowRequisitesLocators.subject, value, "Предмет")


# Заявка на кассовый расход - Реквизиты налоговых платежей
class ApplicationCashFlowRequisitesTaxPaymentsPage(Browser):
    def taxpayer_status(self, value):
        self.set_select(
            ApplicationCashFlowRequisitesTaxPaymentsLocators.taxpayer_status, value, "Статус налогоплательщика")

    def tax_period(self, value):
        self.set_text(ApplicationCashFlowRequisitesTaxPaymentsLocators.tax_period, value, "Налоговый период")

    def is_tax(self, value):
        self.set_checkbox(ApplicationCashFlowRequisitesTaxPaymentsLocators.is_tax, value, "Налоговый платеж")

    def kbk(self, value):
        self.set_select2(ApplicationCashFlowRequisitesTaxPaymentsLocators.kbk, value, "КБК")

    def tax_bill_number(self, value):
        self.set_text(
            ApplicationCashFlowRequisitesTaxPaymentsLocators.tax_bill_number, value, "Номер документа-основания")

    def oktmo(self, value):
        self.set_select2(ApplicationCashFlowRequisitesTaxPaymentsLocators.oktmo, value, "Код по ОКТМО")

    def tax_bill_date(self, value):
        self.set_date(ApplicationCashFlowRequisitesTaxPaymentsLocators.tax_bill_date, value, "Дата документа-основания")

    def reason_for_payment(self, value):
        self.set_select(ApplicationCashFlowRequisitesTaxPaymentsLocators.reason_for_payment, value, "Основание платежа")


# Платежное поручение (приход средств)
class PaymentOrderArrivalPage(Browser):
    def document_number(self, value):
        self.set_text(PaymentOrderArrivalLocators.document_number, value, "Номер")

    def recipient_account_details(self, value):
        self.set_select2(PaymentOrderArrivalLocators.recipient_account_details, value, "Лицевой счет", exactly=False)

    def operation(self, value):
        self.set_select2(PaymentOrderArrivalLocators.operation, value, "Типовая операция")

    def entry_date(self, value):
        self.set_date(PaymentOrderArrivalLocators.entry_date, value, "Дата проводки")

    def drawee(self, value):
        self.set_select2(PaymentOrderArrivalLocators.drawee, value, "Плательщик")

    def drawee_account_details(self, value):
        self.set_select2(PaymentOrderArrivalLocators.drawee_account_details, value, "Расчетный счет плательщика")

    def tracking_number(self, value):
        self.set_text(PaymentOrderArrivalLocators.tracking_number, value, "Бюджетное обязательство")

    def currency(self, value):
        self.set_select2(PaymentOrderArrivalLocators.currency, value, "Код валюты по ОКВ")

    def document_kind(self, value):
        self.set_select2(PaymentOrderArrivalLocators.document_kind, value, "Вид документа")

    def act(self, value):
        self.set_select2(PaymentOrderArrivalLocators.act, value, "Мероприятие по бюджетной росписи")

    def payment_purpose(self, value):
        self.set_text(PaymentOrderArrivalLocators.payment_purpose, value, "Назначение платежа")

    def is_employee(self, value):
        self.set_checkbox(PaymentOrderArrivalLocators.is_employee, value, "Сотрудник")

    def department_unit(self, value):
        self.set_select2(PaymentOrderArrivalLocators.department_unit, value, "Группа учета")

    def purchasing_notice(self, value):
        self.set_select2(PaymentOrderArrivalLocators.purchasing_notice, value, "Извещения о закупке")

    def notification_number(self, value):
        self.set_text(PaymentOrderArrivalLocators.notification_number, value, "Номер уведомления")

    def payment_form(self, value):
        self.set_select(PaymentOrderArrivalLocators.payment_form, value, "Вид платежа")


# Платежное поручение (приход средств) бланк
class PaymentOrderArrivalBlankPage(Browser):
    def kbk(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.kbk, value, "КБК")

    def operation(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.operation, value, "Типовая операция")

    def kosgu(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.kosgu, value, "КОСГУ")

    def cost_element(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.cost_element, value, "Вид затрат")

    def department_unit(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.department_unit, value, "Группа учета")

    def act(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.act, value, "Мероприятие")

    def imprest_foundation(self, value):
        self.set_select2(PaymentOrderArrivalBlankLocators.imprest_foundation, value, "Документ - основание")

    def vat_percent(self, value):
        self.set_text(PaymentOrderArrivalBlankLocators.vat_percent, value, "Ставка НДС")

    def amount(self, value):
        self.set_text(PaymentOrderArrivalBlankLocators.amount, value, "Сумма в рублях")

    def comment(self, value):
        self.set_text(PaymentOrderArrivalBlankLocators.comment, value, "Комментарий")


# Платежное поручение (приход средств) реквизиты
class PaymentOrderArrivalRequisitesPage(Browser):
    def taxpayer_status(self, value):
        self.set_select(PaymentOrderArrivalRequisitesLocators.taxpayer_status, value, "Статус налогоплательщика")

    def kbk(self, value):
        self.set_select2(PaymentOrderArrivalRequisitesLocators.kbk, value, "КБК")

    def oktmo(self, value):
        self.set_select2(PaymentOrderArrivalRequisitesLocators.oktmo, value, "Код по ОКТМО")

    def tax_period(self, value):
        self.set_text(PaymentOrderArrivalRequisitesLocators.tax_period, value, "Налоговый период")

    def tax_bill_number(self, value):
        self.set_text(PaymentOrderArrivalRequisitesLocators.tax_bill_number, value, "Номер документа-основания")

    def tax_bill_date(self, value):
        self.set_date(PaymentOrderArrivalRequisitesLocators.tax_bill_date, value, "Дата документа-основания")

    def reason_for_payment(self, value):
        self.set_select(PaymentOrderArrivalRequisitesLocators.reason_for_payment, value, "Основание платежа")


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

    def document_kind(self, value):
        self.set_select2(ReturnRequestLocators.document_kind, value, "Вид документа")

    def kbk(self, value):
        self.set_select2(ReturnRequestLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ReturnRequestLocators.kosgu, value, "КОСГУ", exactly=False)

    def kbk_type(self, value):
        self.set_select2(ReturnRequestLocators.kbk_type, value, "Тип КБК")

    def cost_element(self, value):
        self.set_select2(ReturnRequestLocators.cost_element, value, "Вид затрат")

    def goal_code(self, value):
        self.set_text(ReturnRequestLocators.goal_code, value, "Код цели")

    def oktmo(self, value):
        self.set_select2(ReturnRequestLocators.oktmo, value, "Код по ОКТМО")

    def department(self, value):
        self.set_select2(ReturnRequestLocators.department, value, "Группа учета")

    def investment_program(self, value):
        self.set_select2(ReturnRequestLocators.investment_program, value, "Код объекта по ФАИП")

    def expenditure_goal_act(self, value):
        self.set_select2(ReturnRequestLocators.expenditure_goal_act, value, "Мероприятие")

    def amount(self, value):
        self.set_text(ReturnRequestLocators.amount, value, "Сумма в рублях")

    def nds_percent(self, value):
        self.set_text(ReturnRequestLocators.nds_percent, value, "Ставка НДС")

    def nds_amount(self, value):
        self.set_text(ReturnRequestLocators.nds_amount, value, "ndsAmount")

    def document_foundation_kind(self, value):
        self.set_select2(ReturnRequestLocators.document_foundation_kind, value, "Вид документа-основания")

    def document_foundation_number(self, value):
        self.set_text(ReturnRequestLocators.document_foundation_number, value, "Номер документа-основания")

    def document_foundation_date(self, value):
        self.set_date(ReturnRequestLocators.document_foundation_date, value, "Дата документа-основания")

    def recepient_kbk(self, value):
        self.set_select2(ReturnRequestLocators.recepient_kbk, value, "КБК получателя")

    def recepient_oktmo(self, value):
        self.set_select2(ReturnRequestLocators.recepient_oktmo, value, "Код по ОКТМО Получателя")

    def chief(self, value):
        self.set_select2(ReturnRequestLocators.chief, value, "Руководитель (уполномоченное лицо)", exactly=False)

    def chief_accountant(self, value):
        self.set_select2(
            ReturnRequestLocators.chief_accountant, value, "Главный бухгалтер (уполномоченное лицо)", exactly=False)

    def priority_of_payment(self, value):
        self.set_text(ReturnRequestLocators.priority_of_payment, value, "Очередность платежа")

    def payment_purpose(self, value):
        self.set_text(ReturnRequestLocators.payment_purpose, value, "Назначение платежа")

    def payment_type(self, value):
        self.set_select(ReturnRequestLocators.payment_type, value, "Вид платежа")

    def type_funds_for_return(self, value):
        self.set_select(ReturnRequestLocators.type_funds_for_return, value, "Вид средств для возврата")

    def outstanding_payment_document_number(self, value):
        self.set_text(
            ReturnRequestLocators.outstanding_payment_document_number, value, "Документ по зачислению  - Номер")

    def outstanding_payment_document_date(self, value):
        self.set_date(
            ReturnRequestLocators.outstanding_payment_document_date, value, "Документ по зачислению  - Дата")

    def outstanding_payment_document_amount(self, value):
        self.set_text(
            ReturnRequestLocators.outstanding_payment_document_amount, value, "Документ по зачислению  - Сумма")

    def outstanding_payment_document_inn(self, value):
        self.set_text(ReturnRequestLocators.outstanding_payment_document_inn, value, "ИНН")

    def outstanding_payment_document_kpp(self, value):
        self.set_text(ReturnRequestLocators.outstanding_payment_document_kpp, value, "КПП")


# Уведомления об уточнении вида и принадлежности платежа
class NotificationTypeAndPaymentTypePage(Browser):
    def document_number(self, value):
        self.set_text(NotificationTypeAndPaymentTypeLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(NotificationTypeAndPaymentTypeLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(NotificationTypeAndPaymentTypeLocators.entry_date, value, "Дата проводки")

    def account_details(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.account_details, value, "Лицевой счет", exactly=False)

    def activity_kind(self, value):
        self.set_select(NotificationTypeAndPaymentTypeLocators.activity_kind, value, "Вид деятельности")

    def budget_commitment_info_number(self, value):
        self.set_text(
            NotificationTypeAndPaymentTypeLocators.budget_commitment_info_number, value,
            "Номер бюджетного обязательства")

    def notification_kind(self, value):
        self.set_select(NotificationTypeAndPaymentTypeLocators.notification_kind, value, "Вид уведомления")

    def unit(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.unit, value, "Группа учета")

    def counterparty(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.counterparty, value, "Плательщик")

    def counterparty_account_details(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeLocators.counterparty_account_details, value,
            "Номер банковского счета плательщика")

    def federal_treasury_request_number(self, value):
        self.set_text(
            NotificationTypeAndPaymentTypeLocators.federal_treasury_request_number, value, "Номер запроса УФК")

    def federal_treasury_request_date(self, value):
        self.set_date(NotificationTypeAndPaymentTypeLocators.federal_treasury_request_date, value, "Дата запроса УФК")

    def region(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.region, value, "Регион")

    def is_employee(self, value):
        self.set_checkbox(NotificationTypeAndPaymentTypeLocators.is_employee, value, "Сотрудник - чекбокс")

    def employee(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.employee, value, "Сотрудник")

    def passport(self, value):
        self.set_text(NotificationTypeAndPaymentTypeLocators.passport, value, "Паспортные данные плательщика")

    def chief(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.chief, value, "Руководитель")

    def contractor(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeLocators.contractor, value, "Ответственный исполнитель")

    def contractor_phone(self, value):
        self.set_text(NotificationTypeAndPaymentTypeLocators.contractor_phone, value, "Телефон исполнителя")


# Уведомления об уточнении вида и принадлежности платежа - добавление уведомления
class NotificationTypeAndPaymentTypeNotificationPage(Browser):
    def order_number(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.order_number, value, "№ п/п")

    def amount(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.amount, value, "Сумма")

    def operation(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.operation, value, "Типовая операция")

    def document_type(self, value):
        self.set_select(NotificationTypeAndPaymentTypeNotificationLocators.document_type, value, "Тип документа")

    def document_number(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(NotificationTypeAndPaymentTypeNotificationLocators.document_date, value, "Дата")

    def billing_document(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.billing_document, value,
                         "Платежный документ")

    def document_foundation(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeNotificationLocators.document_foundation, value, "Документ–основание")

    def recepient(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.recepient, value, "Получатель")

    def recepient_name(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.recepient_name, value, "Получатель-имя")

    def recepient_account_details(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeNotificationLocators.recepient_account_details, value,
            "Расчетный счет получателя")

    def inn(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.inn, value, "ИНН")

    def kpp(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.kpp, value, "КПП")

    def oktmo(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.oktmo, value, "ОКТМО")

    def kbk(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.kbk, value, "КБК")

    def kosgu(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.kosgu, value, "КОСГУ")

    def cost_element(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeNotificationLocators.cost_element, value, "Вид затрат")

    def statement_analysis_code(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeNotificationLocators.statement_analysis_code, value, "Код для отчетности")

    def purpose_code(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.purpose_code, value, "Код цели")

    def purpose_payment(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.purpose_payment, value, "Назначение платежа")

    def comment(self, value):
        self.set_text(NotificationTypeAndPaymentTypeNotificationLocators.comment, value, "Примечание")


# Уведомления об уточнении вида и принадлежности платежа - добавление уведомления + Изменение реквизитов
class NotificationTypeAndPaymentTypeImagePage(Browser):
    def amount(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.amount, value, "Сумма")

    def recepient(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeImageLocators.recepient, value, "Получатель")

    def recepient_account_details(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeImageLocators.recepient_account_details, value, "Расчетный счет получателя")

    def inn(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.inn, value, "ИНН")

    def kpp(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.kpp, value, "КПП")

    def oktmo(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.oktmo, value, "ОКТМО")

    def recepient_personal_account(self, value):
        self.set_text(
            NotificationTypeAndPaymentTypeImageLocators.recepient_personal_account, value, "Лицевой счет получателя")

    def is_taxes(self, value):
        self.set_checkbox(NotificationTypeAndPaymentTypeImageLocators.is_taxes, value, "Налог - чек бокс")

    def kbk(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeImageLocators.kbk, value, "КБК")

    def kosgu(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeImageLocators.kosgu, value, "КОСГУ")

    def cost_element(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeImageLocators.cost_element, value, "Вид затрат")

    def recepient_kbk(self, value):
        self.set_select2(NotificationTypeAndPaymentTypeImageLocators.recepient_kbk, value, "КБК поступлений")

    def activity_kind(self, value):
        self.set_select(NotificationTypeAndPaymentTypeImageLocators.activity_kind, value, "Вид средств")

    def purpose_code(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.purpose_code, value, "Код цели")

    def statement_analysis_code(self, value):
        self.set_select2(
            NotificationTypeAndPaymentTypeImageLocators.statement_analysis_code, value, "Код для отчетности")

    def purpose_payment(self, value):
        self.set_text(NotificationTypeAndPaymentTypeImageLocators.purpose_payment, value, "Назначение платежа")


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
    def operation_master(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.operation_master, value, "Типовая операция")

    def kbk_type(self, value):
        self.set_select(ApplicationForCashWithdrawalAddLineLocators.kbk_type, value, "Тип БК")

    def kbk(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.cost_element, value, "Вид затрат")

    def department_unit(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.department_unit, value, "Группа учета")

    def act(self, value):
        self.set_select2(ApplicationForCashWithdrawalAddLineLocators.act, value, "Мероприятие")

    def code_goal(self, value):
        self.set_text(ApplicationForCashWithdrawalAddLineLocators.code_goal, value, "Код цели")

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


# Заявка на получение денежных средств, перечисляемых на карту
class ApplyingForCardPage(Browser):
    def document_number(self, value):
        self.set_text(ApplyingForCardLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(ApplyingForCardLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(ApplyingForCardLocators.entry_date, value, "Дата проводки")

    def operation_master(self, value):
        self.set_select2(ApplyingForCardLocators.operation_master, value, "Типовая операция")

    def account_details(self, value):
        self.set_select2(ApplyingForCardLocators.account_details, value, "Лицевой счет", exactly=False)

    def tracking_number(self, value):
        self.set_text(ApplyingForCardLocators.tracking_number, value, "Учетный номер обязательства")

    def activity_kind(self, value):
        self.set_select(ApplyingForCardLocators.activity_kind, value, "Вид средств")

    def card_number(self, value):
        self.set_text(ApplyingForCardLocators.card_number, value, "Номер карты")

    def trustee(self, value):
        self.set_select2(ApplyingForCardLocators.trustee, value, "Сотрудник")

    def employee_position(self, value):
        self.set_select2(ApplyingForCardLocators.employee_position, value, "Должность")

    def investment_program(self, value):
        self.set_select2(ApplyingForCardLocators.investment_program, value, "Код объекта ФАИП")

    def employee_name_in_ablative_case(self, value):
        self.set_text(
            ApplyingForCardLocators.employee_name_in_ablative_case, value, "ФИО сотрудника в творительном падеже")

    def employee_position_in_ablative_case(self, value):
        self.set_text(
            ApplyingForCardLocators.employee_position_in_ablative_case, value, "Должность в творительном падеже")

    def foundation(self, value):
        self.set_text(ApplyingForCardLocators.foundation, value, "Основание")

    def chief(self, value):
        self.set_select2(ApplyingForCardLocators.chief, value, "Руководитель")

    def accountant_general(self, value):
        self.set_select2(ApplyingForCardLocators.accountant_general, value, "Главный бухгалтер")


# Заявка на получение денежных средств, перечисляемых на карту добавление строк
class ApplyingForCardAddLinePage(Browser):
    def operation_master(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.operation_master, value, "Типовая операция")

    def kbk(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.kbk, value, "КБК", exactly=False)

    def kbk_type(self, value):
        self.set_select(ApplyingForCardAddLineLocators.kbk_type, value, "Тип КБК")

    def kosgu(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.cost_element, value, "Вид затрат")

    def amount(self, value):
        self.set_text(ApplyingForCardAddLineLocators.amount, value, "Сумма")

    def goal_code(self, value):
        self.set_text(ApplyingForCardAddLineLocators.goal_code, value, "Код цели")

    def department_unit(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.department_unit, value, "Группа учета")

    def act(self, value):
        self.set_select2(ApplyingForCardAddLineLocators.act, value, "Мероприятие")

    def payment_purpose(self, value):
        self.set_text(ApplyingForCardAddLineLocators.payment_purpose, value, "Назначение платежа")

    def comment(self, value):
        self.set_text(ApplyingForCardAddLineLocators.comment, value, "Примечание")


# Расшифровка сумм неиспользованных средств
class DecodingAmountsUnusedFundsPage(Browser):
    def document_number(self, value):
        self.set_text(DecodingAmountsUnusedFundsLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(DecodingAmountsUnusedFundsLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(DecodingAmountsUnusedFundsLocators.entry_date, value, "Дата проводки")

    def card_number(self, value):
        self.set_text(DecodingAmountsUnusedFundsLocators.card_number, value, "Номер карты")

    def operation_type(self, value):
        self.set_select(DecodingAmountsUnusedFundsLocators.operation_type, value, "Вид операции")

    def personal_account(self, value):
        self.set_select2(DecodingAmountsUnusedFundsLocators.personal_account, value, "Лицевой счет", exactly=False)

    def operation_master(self, value):
        self.set_select2(DecodingAmountsUnusedFundsLocators.operation_master, value, "Типовая операция")

    def tracking_number(self, value):
        self.set_text(DecodingAmountsUnusedFundsLocators.tracking_number, value, "Учетный номер обязательства")

    def investment_program(self, value):
        self.set_select2(DecodingAmountsUnusedFundsLocators.investment_program, value, "Код объекта ФАИП")

    def chief(self, value):
        self.set_select2(DecodingAmountsUnusedFundsLocators.chief, value, "Руководитель")

    def accountant_general(self, value):
        self.set_select2(DecodingAmountsUnusedFundsLocators.accountant_general, value, "Главный бухгалтер")


# Расшифровка сумм неиспользованных средств добавление строки
class DecodingAmountsUnusedFundsAddLinePage(Browser):
    def operation_master(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.operation_master, value, "Типовая операция")

    def kosgu(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.cost_element, value, "Вид затрат")

    def kbk(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.kbk, value, "КБК", exactly=False)

    def kbk_type(self, value):
        self.set_select(DecodingAmountsUnusedFundsAddLineLocators.kbk_type, value, "Тип КБК")

    def activity_kind(self, value):
        self.set_select(DecodingAmountsUnusedFundsAddLineLocators.activity_kind, value, "Вид средств")

    def amount(self, value):
        self.set_text(DecodingAmountsUnusedFundsAddLineLocators.amount, value, "Сумма")

    def goal_code(self, value):
        self.set_text(DecodingAmountsUnusedFundsAddLineLocators.goal_code, value, "Код цели")

    def department_unit(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.department_unit, value, "Группа учета")

    def act(self, value):
        self.set_select2(DecodingAmountsUnusedFundsAddLineLocators.act, value, "Мероприятие")

    def comment(self, value):
        self.set_text(DecodingAmountsUnusedFundsAddLineLocators.comment, value, "Примечание")


# Договор с поставщиком
class ContractWithSupplierPage(Browser):
    def document_type(self, value):
        self.set_select2(ContractWithSupplierLocators.documen_type, value, "Вид документа")

    def number(self, value):
        self.set_text(ContractWithSupplierLocators.number, value, "Номер документа")

    def date(self, value):
        self.set_date(ContractWithSupplierLocators.date, value, "Дата создания документа")

    def counter_party(self, value):
        self.set_select2(ContractWithSupplierLocators.counter_party, value, "Контрагент")

    def bank_account_number(self, value):
        self.set_select2(
            ContractWithSupplierLocators.bank_account_number, value, "Номер банковского счета", exactly=False)

    def uin(self, value):
        self.set_text(ContractWithSupplierLocators.uin, value, "УИН")

    def currency(self, value):
        self.set_select2(ContractWithSupplierLocators.currency, value, "Валюта")

    def personal_account(self, value):
        self.set_select2(ContractWithSupplierLocators.personal_account, value, "Лицевой счет", exactly=False)

    def budget_commitment(self, value):
        self.set_select2(ContractWithSupplierLocators.budget_commitment, value, "Номер бюджетного обязательства")

    def payment_against_invoice(self, value):
        self.set_checkbox(ContractWithSupplierLocators.payment_against_invoice, value, "Оплата по счетам -чекбокс")

    def payment_type(self, value):
        self.set_select(ContractWithSupplierLocators.payment_type, value, "Вид оплаты")

    def date_begin(self, value):
        self.set_date(ContractWithSupplierLocators.date_begin, value, "Дата начала")

    def date_end(self, value):
        self.set_date(ContractWithSupplierLocators.date_end, value, "Дата окончания")

    def security_type(self, value):
        self.set_select(ContractWithSupplierLocators.security_type, value, "Тип")

    def security_amount(self, value):
        self.set_text(ContractWithSupplierLocators.security_amount, value, "Сумма")

    def security_period(self, value):
        self.set_date(ContractWithSupplierLocators.security_period, value, " Срок действия ")

    def sending_letter_number(self, value):
        self.set_text(ContractWithSupplierLocators.sending_letter_number, value, "Номер письма об отправке")

    def assurance_register_record_number(self, value):
        self.set_text(ContractWithSupplierLocators.assurance_register_record_number, value,
                      "Номер записи в реестре гарантий")

    def letter_date(self, value):
        self.set_date(ContractWithSupplierLocators.letter_date, value, "Дата письма")

    def note(self, value):
        self.set_text(ContractWithSupplierLocators.note, value, "Примечание")

    def responsible(self, value):
        self.set_select2(ContractWithSupplierLocators.responsible, value, "Ответственный")

    def department_unit(self, value):
        self.set_select2(ContractWithSupplierLocators.department_unit, value, "Группа учета")

    def penalty_period_count(self, value):
        self.set_select(ContractWithSupplierLocators.penalty_period_count, value, "Количество")

    def penalty_period(self, value):
        self.set_select(ContractWithSupplierLocators.penalty_period, value, "дней/часов")

    def penalty_percent(self, value):
        self.set_text(ContractWithSupplierLocators.penalty_percent, value, "%")

    def penalty_amount(self, value):
        self.set_text(ContractWithSupplierLocators.penalty_amount, value, "Сумма")

    def prolongation_term(self, value):
        self.set_text(ContractWithSupplierLocators.prolongation_term, value, "Условие пролонгации")

    def subject_contract(self, value):
        self.set_text(ContractWithSupplierLocators.subject_contract, value, "Предмет договора")

    def payment_terms(self, value):
        self.set_text(ContractWithSupplierLocators.payment_terms, value, "Условие оплаты")


# Договор с Поставщиком - вкладка Детализация по КБК
class ContractWithSupplierDetailKBKPage(Browser):

    def financial_year(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.financial_year, value, "Финансовый год")

    def entry_date(self, value):
        self.set_date(ContractWithSupplierDetailKBKPageLocators.entry_date, value, "Дата проводки")

    def operation(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.operation, value, "Типовая операция")

    def changed(self, value):
        self.set_checkbox(ContractWithSupplierDetailKBKPageLocators.changed, value, "Изменение чекбокс")

    def kbk(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.cost_Element, value, "Вид затрат")

    def contract_subject(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.contract_subject, value, "Предмет договора")

    def department(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.department, value, "Департамент")

    def budgetary_plan_act(self, value):
        self.set_select2(
            ContractWithSupplierDetailKBKPageLocators.budgetary_plan_act, value, "Мероприятие по бюджетной росписи")

    def investment_program(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.investment_program, value, "ФАИП")

    def department_unit(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.department_unit, value, "Группа учета")

    def work(self, value):
        self.set_select2(ContractWithSupplierDetailKBKPageLocators.work, value, "Работа")

    def amounts_amount(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.amounts_amount, value, "Сумма по договору с НДС")

    def amounts_nds_percent(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.amounts_nds_percent, value, "% НДС")

    def advance(self, value):
        self.set_text(ContractWithSupplierDetailKBKPageLocators.advance, value, "Сумма аванса")


# Договор с Поставщиком - вкладка  Детализация по ОКПД
class ContractWithSupplierDetailOKPDPage(Browser):
    def order_number(self, value):
        self.set_text(ContractWithSupplierDetailOKPDLocators.order_number, value, " № п/п ")

    def okpd2(self, value):
        self.set_select2(ContractWithSupplierDetailOKPDLocators.okpd2, value, "ОКПД2")

    def unit_of_measure(self, value):
        self.set_select2(ContractWithSupplierDetailOKPDLocators.unit_of_measure, value, "Единица измерения по ОКЕИ")

    def unit_price(self, value):
        self.set_text(ContractWithSupplierDetailOKPDLocators.unit_price, value, "Цена за единицу")

    def quantity(self, value):
        self.set_text(ContractWithSupplierDetailOKPDLocators.quantity, value, " Количество ")

    def amount(self, value):
        self.set_text(ContractWithSupplierDetailOKPDLocators.amount, value, "Сумма")

    def purchase_object_type(self, value):
        self.set_select2(ContractWithSupplierDetailOKPDLocators.purchase_object_type, value, "Вид объекта закупки")


# Договор с Поставщиком - Вкладка Сведения о госконтракте
class InformationAboutContractPage(Browser):
    def aviso(self, value):
        self.set_select2(InformationAboutContractLocators.aviso, value, "Номер извещения о проведении закупки")

    def purchase_identity(self, value):
        self.set_text(InformationAboutContractLocators.purchase_identity, value, "Идентификационный код закупки")

    def register_record_number(self, value):
        self.set_text(InformationAboutContractLocators.register_record_number, value, "Номер реестровой записи")

    def registration_date(self, value):
        self.set_date(InformationAboutContractLocators.registration_date, value, "Дата регистрации госконтракта")

    def privacy(self, value):
        self.set_select(InformationAboutContractLocators.privacy, value, "Признак секретности")

    def confirm_document_number(self, value):
        self.set_text(InformationAboutContractLocators.confirm_document_number, value, "Номер")

    def confirm_document_date(self, value):
        self.set_date(InformationAboutContractLocators.confirm_document_date, value, "Дата")

    def confirm_document_kind(self, value):
        self.set_select2(InformationAboutContractLocators.confirm_document_kind, value, "Вид документа")

    def comment(self, value):
        self.set_text(InformationAboutContractLocators.comment, value, "Дополнительная информация")

    def department(self, value):
        self.set_select2(InformationAboutContractLocators.department, value, "Способ размещения заказа")

    def auction_date(self, value):
        self.set_date(InformationAboutContractLocators.auction_date, value, "Дата торгов")

    def declared_value(self, value):
        self.set_text(InformationAboutContractLocators.declared_value, value, "Объявленная стоимость госконтракта")

    def change_foundation(self, value):
        self.set_text(InformationAboutContractLocators.change_foundation, value, "Основание для внесения изменений")

    def for_small_entrepreneur(self, value):
        self.set_checkbox(InformationAboutContractLocators.for_small_entrepreneur, value,
                          "Для размещения среди субъектов малого предпринимательства")

    def domestic_goods_preference(self, value):
        self.set_checkbox(InformationAboutContractLocators.domestic_goods_preference, value,
                          "С предоставлением преференций отечественным и белорусским товарам")

    def perfomance_document_number(self, value):
        self.set_text(InformationAboutContractLocators.perfomance_document_number, value,
                      "Номер документа об исполнении или расторжении")

    def contract_performance_date(self, value):
        self.set_date(InformationAboutContractLocators.contract_performance_date, value,
                      "Дата исполнения или расторжения госконтракта")

    def terminated_by(self, value):
        self.set_select(InformationAboutContractLocators.terminated_by, value, "Причина расторжения")

    def contract_cancellation_record_number(self, value):
        self.set_text(
            InformationAboutContractLocators.contract_cancellation_record_number, value,
            "Номер реестровой записи ранее расторгнутого госконтракта")

    def contract_perfomance_foundation(self, value):
        self.set_text(
            InformationAboutContractLocators.contract_perfomance_foundation, value,
            "Основание исполнения или расторжения госконтракта")


# Договор с Поставщиком - История
class HistoryPage(Browser):
    def change_date(self, value):
        self.set_date(HistoryLocators.change_date, value, "Дата изменения")

    def change_number(self, value):
        self.set_text(HistoryLocators.change_number, value, "Номер изменения")

    def change_type(self, value):
        self.set_select(HistoryLocators.change_type, value, "Тип изменения")

    def comment(self, value):
        self.set_text(HistoryLocators.comment, value, "comment")


# Договор с Поставщиком - Календарный план
class CalendarPlanPage(Browser):
    def financial_year(self, value):
        self.set_text(CalendarPlanLocators.financial_year, value, "Финансовый год")

    def work_name(self, value):
        self.set_text(CalendarPlanLocators.work_name, value, "Наименование этапа")

    def result(self, value):
        self.set_text(CalendarPlanLocators.result, value, "Результат")

    def comment(self, value):
        self.set_text(CalendarPlanLocators.comment, value, "Комментарий")

    def start_date(self, value):
        self.set_date(CalendarPlanLocators.start_date, value, "Дата начала этапа")

    def end_date(self, value):
        self.set_date(CalendarPlanLocators.end_date, value, "Дата окончания этапа")

    def amount(self, value):
        self.set_text(CalendarPlanLocators.amount, value, "Сумма по этапу")

    # Договор с Поставщиком - Дополнительные контрагенты
    def counterparty(self, value):
        self.set_select2(CalendarPlanLocators.counterparty, value, "counterparty")

    def account_details(self, value):
        self.set_select2(CalendarPlanLocators.account_details, value, "accountDetails")


# Обеспечение исполнения обязательств
class EnsuringFulfillmentOfObligationsPage(Browser):
    def document_number(self, value):
        self.set_text(EnsuringFulfillmentOfObligationsLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(EnsuringFulfillmentOfObligationsLocators.document_date, value, "Дата")

    def operation(self, value):
        self.set_select2(EnsuringFulfillmentOfObligationsLocators.operation, value, "Типовая операция")

    def counterparty(self, value):
        self.set_select2(EnsuringFulfillmentOfObligationsLocators.counterparty, value, "Принципал / Должник")

    def entry_date(self, value):
        self.set_date(EnsuringFulfillmentOfObligationsLocators.entry_date, value, "Дата проводки / постановки на учет")

    def retirement_date(self, value):
        self.set_date(EnsuringFulfillmentOfObligationsLocators.retirement_date, value, "Дата списания")

    def amount(self, value):
        self.set_text(EnsuringFulfillmentOfObligationsLocators.amount, value, "Сумма обеспечения")

    def guarantor(self, value):
        self.set_select2(EnsuringFulfillmentOfObligationsLocators.guarantor, value, "Гарант / Поручитель")

    def assurance_starts(self, value):
        self.set_date(EnsuringFulfillmentOfObligationsLocators.assurance_starts, value, "Срок действия обеспечения с")

    def assurance_ends(self, value):
        self.set_date(EnsuringFulfillmentOfObligationsLocators.assurance_ends, value, "Срок действия обеспечения по")


# Сведения о бюджетном обязательстве
class InformationAboutBudgetObligationPage(Browser):
    def document_number(self, value):
        self.set_text(InformationAboutBudgetObligationLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(InformationAboutBudgetObligationLocators.document_date, value, "Дата")

    def financial_year(self, value):
        self.set_text(InformationAboutBudgetObligationLocators.financial_year, value, "Финансовый год")

    def liability(self, value):
        self.set_select(InformationAboutBudgetObligationLocators.liability, value, "Тип бюджетного обязательства")

    def tracking_number(self, value):
        self.set_text(InformationAboutBudgetObligationLocators.tracking_number, value, "Учетный номер БО")

    def registration_date(self, value):
        self.set_date(InformationAboutBudgetObligationLocators.registration_date, value, "Дата регистрации в ФК")

    def account_details(self, value):
        self.set_select2(InformationAboutBudgetObligationLocators.account_details, value, "Лицевой счет")

    def guid(self, value):
        self.set_text(InformationAboutBudgetObligationLocators.guid, value, "GUID")

    def counterparty(self, value):
        self.set_select2(InformationAboutBudgetObligationLocators.counterparty, value, "Контрагент")

    def transaction_account(self, value):
        self.set_select2(InformationAboutBudgetObligationLocators.transaction_account, value, "Номер банковского счета")

    def chief(self, value):
        self.set_select2(InformationAboutBudgetObligationLocators.chief, value, "Руководитель")

    def prepared_by(self, value):
        self.set_select2(InformationAboutBudgetObligationLocators.prepared_by, value, "Исполнитель")


# Сведения о бюджетном обязательстве  - Дополнительные контрагенты
class InformationAboutBudgetObligationDopPage(Browser):
    def counterparty(self, value):
        self.set_text(InformationAboutBudgetObligationDopLocators.counterparty, value, "Наименование")

    def account_details(self, value):
        self.set_text(InformationAboutBudgetObligationDopLocators.account_details, value, "Номер банковского счета")


# Сведения о бюджетном обязательстве строки
class InformationAboutBudgetObligationAddLinePage(Browser):
    def financial_year(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.financial_year, value, "Финансовый год")

    def kbk(self, value):
        self.set_select2(InformationAboutBudgetObligationAddLineLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(InformationAboutBudgetObligationAddLineLocators.kosgu, value, "КОСГУ", exactly=False)

    def activity_kind(self, value):
        self.set_select(InformationAboutBudgetObligationAddLineLocators.activity_kind, value, "Вид средств")

    def kbk_type(self, value):
        self.set_select(InformationAboutBudgetObligationAddLineLocators.kbk_type, value, "Тип КБК")

    def comment(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.comment, value, "Примечание")

    def investment_program(self, value):
        self.set_select2(InformationAboutBudgetObligationAddLineLocators.investment_program, value, "ФАИП")

    # Суммы на текущий год
    def current_year_amounts(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.current_year_amounts, value, "Январь")

    def february(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.february, value, "february")

    def march(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.march, value, "march")

    def april(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.april, value, "april")

    def may(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.may, value, "may")

    def june(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.june, value, "june")

    def july(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.july, value, "july")

    def august(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.august, value, "august")

    def september(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.september, value, "september")

    def october(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.october, value, "october")

    def november(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.november, value, "november")

    def december(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.december, value, "december")

    # Суммы на плановый период
    def first_year_amount(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.first_year_amount, value, "Первый год")

    def second_year_amount(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.second_year_amount, value, "Второй год")

    def third_year_amount(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.third_year_amount, value, "Третий год")

    def other_years_amount(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.other_years_amount, value, "Последующие")

    def completed_amout(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.completed_amout, value, "Исполненные")

    def not_completed_amount(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.not_completed_amount, value, "Неисполненные")

    def conditional_payment(self, value):
        self.set_checkbox(
            InformationAboutBudgetObligationAddLineLocators.conditional_payment, value, "Условный платеж - чек бокс")

    def analytical_code(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.analytical_code, value, "Аналитический код")

    def act(self, value):
        self.set_select2(InformationAboutBudgetObligationAddLineLocators.act, value, "Мероприятие по бюджетной росписи")

    def payment_day(self, value):
        self.set_text(InformationAboutBudgetObligationAddLineLocators.payment_day, value,
                      "День выплаты по исполнительному документу")


# Сведения о бюджетном обязательстве - история
class InformationAboutBudgetObligationHistoryPage(Browser):
    def change_number(self, value):
        self.set_text(InformationAboutBudgetObligationHistoryLocators.change_number, value, "Номер изменения")

    def change_date(self, value):
        self.set_date(InformationAboutBudgetObligationHistoryLocators.change_date, value, "Дата изменения")

    def comment(self, value):
        self.set_text(InformationAboutBudgetObligationHistoryLocators.comment, value, "Примечание")


# Сведения о бюджетном обязательстве -  Реквизиты документа-основания
class InformationAboutBudgetObligationRequisitesPage(Browser):
    def document_foundation_kind(self, value):
        self.set_select(InformationAboutBudgetObligationRequisitesLocators.document_foundation_kind, value,
                        "Вид")

    def document_foundation_number(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.document_foundation_number, value,
                      "Номер")

    def document_foundation_date(self, value):
        self.set_date(InformationAboutBudgetObligationRequisitesLocators.document_foundation_date, value,
                      "Дата")

    def document_fondation_currency(self, value):
        self.set_select2(InformationAboutBudgetObligationRequisitesLocators.document_fondation_currency, value,
                         "Код валюты по ОКВ")

    def amount(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.amount, value, "Сумма в рублях")

    def currency_amount(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.currency_amount, value, "Сумма в валюте")

    def advance_percent(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.advance_percent, value, "%")

    def advance_amount(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.advance_amount, value, "Сумма аванса")

    def register_record_number(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.register_record_number, value,
                      "Реестровый номер")

    def document_foundation_subject(self, value):
        self.set_text(InformationAboutBudgetObligationRequisitesLocators.document_foundation_subject, value,
                      "Предмет по документу-основанию")


# Справочники - Картотека ОС,НМА,НПА - добавление документа
class CardIndexOSNMANPAPage(Browser):

    def tag_no_first_part(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no_first_part, value, "Первая часть инвентарного номера")

    def tag_no_second_part(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no_second_part, value, "Вторая часть инвентарного номера")

    def tag_no(self, value):
        self.set_text(CardIndexOSNMANPALocators.tag_no, value, ">>>")

    def template(self, value):
        self.set_select2(CardIndexOSNMANPALocators.template, value, "Шаблон карточки")

    def full_name(self, value):
        self.set_text(CardIndexOSNMANPALocators.full_name, value, "Полное наименование")

    def property_designation(self, value):
        self.set_text(CardIndexOSNMANPALocators.property_designation, value, "Назначение объекта")

    def supplier(self, value):
        self.set_select2(CardIndexOSNMANPALocators.supplier, value, "Поставщик")

    def issue_date(self, value):
        self.set_date(CardIndexOSNMANPALocators.issue_date, value, "Дата выпуска")

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


# Справочники - Материально - ответственные лица
class MateriallyResponsiblePersonPage(Browser):

    def employee(self, value):
        self.set_select2(MateriallyResponsiblePersonLocators.employee, value, "Ссылка на сотрудника")

    def name(self, value):
        self.set_text(MateriallyResponsiblePersonLocators.name, value, "Краткое наименование")

    def full_name(self, value):
        self.set_text(MateriallyResponsiblePersonLocators.full_name, value, "Полное наименование")

    def position(self, value):
        self.set_select2(MateriallyResponsiblePersonLocators.position, value, "Должность")

    def valid_till(self, value):
        self.set_date(MateriallyResponsiblePersonLocators.valid_till, value, "Дата актуальности")


# Учет нефинансовых активов - Поступление НФА - шапка документа
class ReceiptOfNonFinancialAssetsCapPage(Browser):

    def document_number(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsCapLocators.document_number, value, "Номер")

    def document_kind(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsCapLocators.document_kind, value, "Вид документа", exactly=False)

    def document_date(self, value):
        self.set_date(ReceiptOfNonFinancialAssetsCapLocators.document_date, value, "Дата")

    def entry_date(self, value):
        self.set_date(ReceiptOfNonFinancialAssetsCapLocators.entry_date, value, "Дата проводки")

    def materially_responsible_person(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsCapLocators.materially_responsible_person, value,
                         "МОЛ")

    def sender_sender_type(self, value):
        self.set_select(ReceiptOfNonFinancialAssetsCapLocators.sender_sender_type, value, "Вид отправителя")

    def organization(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsCapLocators.organization, value, "Наименование отправителя")

    def comment(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsCapLocators.comment, value, "Комментарий")


# Учет нефинансовых активов - Поступление НФА - строка документа
class ReceiptOfNonFinancialAssetsRowPage(Browser):

    def operation(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsRowLocators.operation, value, "Типовая операция")

    def tag_no(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsRowLocators.tag_no, value, "Инвентарный №")

    def amount(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsRowLocators.amount, value, "Сумма по документу")

    def amortization(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsRowLocators.amortization, value, "Амортизация")

    def comment(self, value):
        self.set_text(ReceiptOfNonFinancialAssetsRowLocators.comment, value, "Комментарий")

    def kbk(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsRowLocators.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(ReceiptOfNonFinancialAssetsRowLocators.kosgu, value, "КОСГУ", exactly=False)


# Шаблона карточки ОС, НМА, НПА
class CreateATemplateForTheCardOSNMANPA(Browser):

    def name(self, value):
        self.set_text(CreateATemplateForTheCardOSNMANPALocators.name, value, "Наименование объекта")

    def unit_of_measure(self, value):
        self.set_select2(CreateATemplateForTheCardOSNMANPALocators.unit_of_measure, value, "Единица измерения")

    def group(self, value):
        self.set_select2(CreateATemplateForTheCardOSNMANPALocators.group, value, "Группа ОС, НМА, НПА")

    def okof(self, value):
        self.set_select2(CreateATemplateForTheCardOSNMANPALocators.okof, value, "ОКОФ")

    def amortization_group(self, value):
        self.set_select2(CreateATemplateForTheCardOSNMANPALocators.amortization_group, value, "Амортизационная группа")


# Массовое заполнение параметров ОС
class MassFillingOfOsParametersPage(Browser):
    def unit_of_measure(self, value):
        self.set_select2(MassFillingOfOsParametersLocators.unit_of_measure, value, "Еденица измерения")

    def property_designation(self, value):
        self.set_text(MassFillingOfOsParametersLocators.property_designation, value, "Назначение объекта")

    def start_up_date(self, value):
        self.set_date(MassFillingOfOsParametersLocators.start_up_date, value, "Дата ввода в эксплуатацию")

    def issue_date(self, value):
        self.set_date(MassFillingOfOsParametersLocators.issue_date, value, "Дата выпуска")


# Справочник - «Группы МЗ»
class CreationOfANewEntryInTheDirectoryGroupMzPage(Browser):
    def order_number(self, value):
        self.set_text(CreationOfANewEntryInTheDirectoryGroupMzLocators.order_number, value, "N п/п")

    def full_name(self, value):
        self.set_text(CreationOfANewEntryInTheDirectoryGroupMzLocators.full_name, value, "Полное наименование")

    def name(self, value):
        self.set_text(CreationOfANewEntryInTheDirectoryGroupMzLocators.name, value, "Краткое наименование")


# Справочник «Объекты МЗ» - шапка
class CreationOfAnEntryInTheDirectoryObjectsOfOzCapPage(Browser):
    def tag_no(self, value):
        self.set_text(CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators.tag_no, value, "Шифр")

    def name(self, value):
        self.set_text(CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators.name, value, "Наименование")

    def unit_of_measure(self, value):
        self.set_select2(CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators.unit_of_measure, value,
                         "Единица измерения")

    def group(self, value):
        self.set_select2(CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators.group, value,
                         "Группа материальных запасов")

    def valid_till(self, value):
        self.set_date(CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators.valid_till, value, "Дата актуальности")


# Справочник «Объекты МЗ» - строки
class CreationOfAnEntryInTheDirectoryObjectsOfOzRowPage(Browser):
    def open(self):
        self.click(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.open, "Открыть")

    def add(self):
        self.click(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.add, "Добавить")

    def delete(self):
        self.click(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.delete, "Удалить")

    def name(self, value):
        self.set_text(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.name, value, "Характеристика объекта")

    def price(self, value):
        self.set_text(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.price, value, "Сумма")

    def acquisition_date(self, value):
        self.set_date(CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators.acquisition_date, value,
                      "Дата поступления")


# Справочник - «Приказы о назначении комиссии» - шапка
class CreationOfACommissionOrderCapPage(Browser):
    def order_number(self, value):
        self.set_text(CreationOfACommissionOrderCapLocators.order_number, value, "№")

    def order_date(self, value):
        self.set_date(CreationOfACommissionOrderCapLocators.order_date, value, "Дата приказа")

    def comment(self, value):
        self.set_text(CreationOfACommissionOrderCapLocators.comment, value, "Комментарий")

    def valid_till(self, value):
        self.set_date(CreationOfACommissionOrderCapLocators.valid_till, value, "Дата актуальности")


# Справочник - «Приказы о назначении комиссии» - строки
class CreationOfACommissionOrderRowPage(Browser):

    def order(self, value):
        self.set_text(CreationOfACommissionOrderRowLocators.order, value, "№ п/п")

    def employee(self, value):
        self.set_select2(CreationOfACommissionOrderRowLocators.employee, value, "Расшифровка подписи")

    def position(self, value):
        self.set_select2(CreationOfACommissionOrderRowLocators.position, value, "Должность")


# Модальное окно - Печать - «Акт о приеме-передаче объектов нефинансовых активов»
class ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsPage(Browser):
    def committee(self, value):
        self.set_select2(ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.committee,
                         value, "Приказ о назначении комиссии")

    def foundation_document(self, value):
        self.set_text(
            ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.foundation_document, value,
            "Основание")

    def foundation_number(self, value):
        self.set_text(ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.foundation_number,
                      value, "Номер")

    def foundation_date(self, value):
        self.set_date(ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.foundation_date,
                      value, "Дата")

    def sender_chief_position(self, value):
        self.set_text(
            ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.sender_chief_position, value,
            "Руководитель сдатчика - должность")

    def sender_chief_name(self, value):
        self.set_text(ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.sender_chief_name,
                      value, "Руководитель сдатчика - ФИО")

    def recipient_chief_position(self, value):
        self.set_text(
            ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.recipient_chief_position,
            value, "Руководитель получателя - должность")

    def recipient_chief_name(self, value):
        self.set_text(
            ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators.recipient_chief_name, value,
            "Руководитель получателя - ФИО")


# Модальное окно - Печать - «Акт о приеме-сдаче отремонтированных,
# реконструированных и модернизированных объектов основных средств»
class ModalWindowOfTheActOnAcceptanceAndTransferOfObjectsOfNonFinancialAssetsPage(Browser):
    def committee(self, value):
        self.set_select2(ModalWindowOfTheActOnAcceptanceAndTransferOfObjectsOfNonFinancialAssetsLocators.committee,
                         value, "Приказ о назначении комиссии")

    def inventory_date_from(self, value):
        self.set_date(
            ModalWindowOfTheActOnAcceptanceAndTransferOfObjectsOfNonFinancialAssetsLocators.inventory_date_from,
            value, "Срок инвентаризации с")

    def inventory_date_to(self, value):
        self.set_date(
            ModalWindowOfTheActOnAcceptanceAndTransferOfObjectsOfNonFinancialAssetsLocators.inventory_date_to,
            value, "по")


# Модальное окно - Изменение параметоров в отмеченных записях
class ModalWindowChangingParametersInMarkedRecordsPage(Browser):
    def operation(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.operation, value, "Типовая операция")

    def kosgu(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.cost_element, value, "Вид затрат")

    def department_unit(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.department_unit, value, "Группа учета")

    def kbk(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.kbk, value, "КБК", exactly=False)

    def storage(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.storage, value, "Место хранения")

    def counterparty(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.counterparty, value,
                         "Организация-контрагент")

    def foundation(self, value):
        self.set_select2(ModalWindowChangingParametersInMarkedRecordsLocators.foundation, value, "Документ-основание")

    def comment(self, value):
        self.set_text(ModalWindowChangingParametersInMarkedRecordsLocators.comment, value, "Комментарий")


# Модальное окно - Расчет по бухгалтерским данным
class AccountingCalculationPage(Browser):
    def balances_collection_date(self, value):
        self.set_date(AccountingCalculationLocators.balances_collection_date, value, "Дата сбора остатков")

    def operation_date(self, value):
        self.set_date(AccountingCalculationLocators.operation_date, value, "Дата формирования операции")

    def balance_sheet_account(self, value):
        self.set_select2(AccountingCalculationLocators.balance_sheet_account, value, "Счет учета ОС, НМА")

    def balance_sheet_account_group(self, value):
        self.set_select2(AccountingCalculationLocators.balance_sheet_account_group, value,
                         "Группа счетов учета ОС, НМА")


# Модальное окно - Параметры вывода остатков НФА
class ViewingOfAccountBalancesPage(Browser):
    def clear_field_account(self):
        self.click(ViewingOfAccountBalancesLocators.clear_field_account, "Очистка поля Счет")

    def date(self, value):
        self.set_date(ViewingOfAccountBalancesLocators.date, value,
                      "Дата, на которую формируются остатки")

    def balance_sheet_account(self, value):
        self.set_select2(ViewingOfAccountBalancesLocators.balance_sheet_account, value,
                         "Счет")

    def balance_sheet_account_group(self, value):
        self.set_select2(ViewingOfAccountBalancesLocators.balance_sheet_account_group, value,
                         "Группа счетов")

    def materially_responsible_person(self, value):
        self.set_select2(ViewingOfAccountBalancesLocators.materially_responsible_person, value,
                         "Материально-ответственные лица")

    def kbk(self, value):
        self.set_select2(ViewingOfAccountBalancesLocators.kbk, value, "КБК")

    def basic_facilities(self, value):
        self.set_select2(ViewingOfAccountBalancesLocators.basic_facilities, value,
                         "Картотека ОС, НМА, НПА")

    def price_from(self, value):
        self.set_text(ViewingOfAccountBalancesLocators.price_from, value, "Цена от")

    def price_to(self, value):
        self.set_text(ViewingOfAccountBalancesLocators.price_to, value, "Цена до")

    def name_query(self, value):
        self.set_text(ViewingOfAccountBalancesLocators.name_query, value, "Контекст наименования")


# Cчет от Поставщика
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


# Cчет от поставщика - добавление строки
class InvoiceFromTheSupplierAddLinePage(Browser):
    def add(self):
        self.click(InvoiceFromTheSupplierAddLineLocators.add, "add")

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


# Расходный кассовый ордер
class AccountCashWarrantPage(Browser):
    def document_kind(self, value):
        self.set_select2(AccountCashWarrantLocators.document_kind, value, "Вид документа")

    def document_number(self, value):
        self.set_text(AccountCashWarrantLocators.document_number, value, "Номер")

    def entry_date(self, value):
        self.set_date(AccountCashWarrantLocators.entry_date, value, "Дата проводки")

    def document_date(self, value):
        self.set_date(AccountCashWarrantLocators.document_date, value, "Дата")

    def department_unit(self, value):
        self.set_select2(AccountCashWarrantLocators.department_unit, value, "Группа учета")

    def operation_master(self, value):
        self.set_select2(AccountCashWarrantLocators.operation_master, value, "Типовая операция")

    def employee(self, value):
        self.set_select2(AccountCashWarrantLocators.employee, value, "Сотрудник")

    def issue(self, value):
        self.set_text(AccountCashWarrantLocators.issue, value, "Выдать")

    def foundation(self, value):
        self.set_text(AccountCashWarrantLocators.foundation, value, "Основание")

    def cash_report_number(self, value):
        self.set_text(AccountCashWarrantLocators.cash_report_number, value, "Номер кассового отчета")


# Расходный кассовый ордер добавление строки
class AccountCashWarrantPageAddLine(Browser):
    def operation(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.operation, value, "Типовая операция", exactly=False)

    def kbk(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.kbk, value, "КБК", exactly=False)

    def kosgu(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.kosgu, value, "КОСГУ", exactly=False)

    def cost_element(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.cost_element, value, "Вид затрат")

    def department_unit(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.department_unit, value, "Группа учета")

    def sender(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.sender, value, "Отправитель (МОЛ)")

    def material_inventory(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.material_inventory, value, "Номенклатура")

    def quantity(self, value):
        self.set_text(AccountCashWarrantPageAddLine.quantity, value, "Количество")

    def amount(self, value):
        self.set_text(AccountCashWarrantLocatorsAddLine.amount, value, "Сумма")

    def comment(self, value):
        self.set_text(AccountCashWarrantLocatorsAddLine.comment, value, "Комментарий")

    def act(self, value):
        self.set_select2(AccountCashWarrantLocatorsAddLine.act, value, "Мероприятие")


# Расходный кассовый ордер приложение
class AccountCashWarrantPagePlusPage(Browser):
    def document_foundation(self, value):
        self.set_select2(
            AccountCashWarrantPagePlusLocators.document_foundation, value, "Основание для выдачи в подотчет")

    def advance_report(self, value):
        self.set_select2(AccountCashWarrantPagePlusLocators.advance_report, value, "Авансовый отчет")

    def supplement(self, value):
        self.set_text(AccountCashWarrantPagePlusLocators.supplement, value, "Приложение")

    def accountant(self, value):
        self.set_select2(AccountCashWarrantPagePlusLocators.accountant, value, "Главный бухгалтер")

    def chief(self, value):
        self.set_select2(AccountCashWarrantPagePlusLocators.chief, value, "Руководитель организации")

    def cashier(self, value):
        self.set_select2(AccountCashWarrantPagePlusLocators.cashier, value, "Выдал кассир")




# # Справочники - Шаблоны карточки ОС, НМА, НПА - добавление документа
# class TemplatesofthecardOSNMANPA(Browser):
#         print("Templates_of_the_card_OSNMANPA")
#
# # Массовое заполнение параметров ОС
# class Mass_filling_of_OS_parameters(Browser):
#     print("Mass_filling_of_OS_parameters")
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
