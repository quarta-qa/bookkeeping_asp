from locators import *


class LoginPage(Browser):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")


class MainPage(Browser):

    def click_button_menu(self):
        sleep(3)
        self.click(MainLocators.menu)

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

    # Документы
    def to_main(self):
        self.click(MenuLocators.eagle)
        print("Документы — Бухгалтерский учет")


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

        def document_kind(self,value):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.document_kind,value, "Вид документа")

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
            self.set_text(CashExpenseRequestLocators.DocumentHeader.tracking_number, value, "Учетный номер обязательства")

        def federal_targeted_investment_program(self):
            self.set_type(CashExpenseRequestLocators.DocumentHeader.federal_targeted_investment_program, "Код объекта по ФАИП")

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
            self.set_type(CashExpenseRequestLocators.DocumentHeader.chief_account, "Главный бухгалтер (уполномоченное лицо)")

        # Реквизиты документа-основания
        @property
        def requisites(self):
            return self.Requisites(self.driver)

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
            self.set_select(CashExpenseRequestLocators.Transcript.activity_kind, value, "Наименование вида средств для исполнения обязательства")

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
            self.set_type(CashExpenseRequestLocators.Transcript.document_foundation_counterparty, "Организация для Документа - основания")

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
            self.set_text(CashExpenseRequestLocators.Transcript.recepient_subsidy_code, value, "Код субсидии получателя")

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

    def document_number(self, value):
        self.set_text(ZNVLocators.document_number, value, "Номер")

    def document_date(self, value):
        self.set_date(ZNVLocators.document_date, value, "Дата документа")

    def personal_account(self, value):
        self.set_select2(ZNVLocators.personal_account, value, "Лицевой счет", exactly=False)

    def recipient_name(self, value):
        self.set_type(ZNVLocators.recipient_name, value, "Наименование получателя")

    def ofk_registration_number(self, value):
        self.set_text(ZNVLocators.ofk_registration_number, value, "Номер УФК")

    def entry_date(self, value):
        self.set_date(ZNVLocators.entry_date, value, "Дата проводки")

    def typical_operation(self, value):
        self.set_type(ZNVLocators.typical_operation, value, "Типовая операция")

    def recipient_account(self, value):
        self.set_type(ZNVLocators.recipient_account, value, "Расчетный счет получателя")

    def document_type(self, value):
        self.set_type(ZNVLocators.document_type, value, "Вид документа")

    class Request(Browser):

        def summa_rub(self, value):
            self.set_text(ZNVLocators.Request.summa_rub, value, "Сумма в рублях")

        def kbk(self, value):
            self.set_type(ZNVLocators.Request.kbk, value, "КБК")

        def kosgu(self, value):
            self.set_type(ZNVLocators.Request.kosgu, value, "КОСГУ")

        def stavka_nds(self, value):
            self.set_text(ZNVLocators.Request.stavka_nds, value, "Ставка НДС")

        def tip_kbk(self, value):
            self.set_select(ZNVLocators.Request.tip_kbk, value, "Тип КБК")

        def vid_zatrat(self, value):
            self.set_type(ZNVLocators.Request.vid_zatrat, value, "Вид затрат")

        def summa_nds(self, value):
            self.set_text(ZNVLocators.Request.summa_nds, value, "Сумма НДС")

        def oktmo(self, value):
            self.set_type(ZNVLocators.Request.oktmo, value, "Код по ОКТМО")

    class Doc(Browser):

        def number(self, value):
            self.set_text(ZNVLocators.Doc.number, value, "Номер")


# Договор с поставщиком
class ContractWithSupplierPage(Browser):

    def documen_type(self, value):
        self.set_select2(ContractWithSupplierLocators.documen_type, value, "Вид документа")

    def number(self, value):
        self.set_text(ContractWithSupplierLocators.number, value, "Номер документа")

    def date(self, value):
        self.set_date(ContractWithSupplierLocators.date, value, "Дата создания документа")

    def сounterparty(self, value):
        self.set_select2(ContractWithSupplierLocators.сounterparty, value, "Контрагент")

    def bank_account_number(self, value):
        self.set_select2(ContractWithSupplierLocators.bank_account_number, value, "Номер банковского счета", exactly=False)

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


# Справочники - Картотека ОС,НМА,НПА
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

    def serialNumber(self, value):
        self.set_text(CardIndexOSNMANPALocators.serialNumber, value, "Серийный №")
