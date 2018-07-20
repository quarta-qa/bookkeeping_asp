from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='username']")
    password = (By.XPATH, "//input[@id='password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")
    # menu_close = (By.XPATH, "//button[@class='left-menu-toggle active']")

"""
class MenuLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")
    eagle = (By.XPATH, "//*[@class='qa-header-icon-logo']")
    calculation = (By.XPATH, "//a[contains(.,'Расчеты')]")
    inner_calculation = (By.XPATH, "//*[@href='#/common/calculation']")
    statement_processing = (By.XPATH, "//a[contains(.,'Обработка выписки из л/с')]")
    unloading_informationSUFD = (By.XPATH, "//div[@id='collapseMenu1']//*[@href='#/reports']")
    unloading_information = (By.XPATH, "(//*[@href='#'])[3]")
    references = (By.XPATH, "//a[contains(.,'Справочники')]")
    report = (By.XPATH, "//a[contains(.,'Отчет')]")
    turnover_statement = (By.XPATH, "//*[@href='#/reports/turnover-balance-sheet']")
    summary_reporting = (By.XPATH, "//a[contains(.,'Сводная отчетность')]")
    printed_forms = (By.XPATH, "//div[@id='collapseMenu2']//*[@href='#/reports']")
    remains_NFA = (By.XPATH, "//*[@href='#/report/non-financial-assets/balances-gathering']")
    salary = (By.XPATH, "(//a[contains(.,'АИС «Зарплата.NET»')]")
    document_journal = (By.XPATH, "//a[contains(.,'Журнал документов')]")
    recycle_bin = (By.XPATH, "//*[@href='#/common/documents/deleted-document']")

"""

class MenuLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")
    eagle = (By.XPATH, "//*[@class='qa-header-icon-logo']")
    calculation = (By.XPATH, "//a[contains(.,'Расчеты')]")
    inner_calculation = (By.XPATH, "(//a[contains(.,'Расчеты')])[2]")
    statement_processing = (By.XPATH, "//a[contains(.,'Обработка выписки из л/с')]")
    unloading_informationSUFD = (
        By.XPATH, "//a[contains(.,'Выгрузка Сведений о бюджетном обязательстве (загрузка)"
                  " в формате СУФД ФК (или Электронного бюджета)')]")
    unloading_information = (
        By.XPATH, "//a[contains(.,'Выгрузка Сведений о денежном обязательстве в Электронный бюджет')]")
    references = (By.XPATH, "//*[@href='#/classifiers']")
    report = (By.XPATH, "//a[contains(.,'Отчет')]")
    turnover_statement = (By.XPATH, "//a[contains(.,'Оборотная ведомость')]")
    summary_reporting = (By.XPATH, "//a[contains(.,'Сводная отчетность')]")
    printed_forms = (By.XPATH, "//a[contains(.,'Печатные формы')]")
    remains_NFA = (By.XPATH, "//*[@href='#/report/non-financial-assets/balances-gathering']")
    salary = (By.XPATH, "//*[@href='http://qtestzrpasp5.office.quarta-vk.ru:1100']")
    document_journal = (By.XPATH, "//a[contains(.,'Журнал документов')]")
    recycle_bin = (By.XPATH, "//*[@href='#/common/documents/deleted-document']")


# Нажать на раздел из справочника
class ClickOnTheSectionFromTheDirectoryLocators(object):
    # Учет нефинансовых активов
    objects_os_nma_npa = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/basic-facilities']")
    group_os_nma_npa = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/material-inventory-group']")
    objects_mz = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/material-inventory']")
    group_mz = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/material-inventory-group']")
    materially_responsible_person = (By.XPATH,
                                     "//*[@href='#/non-financial-assets/classifiers/materially-responsible-person']")
    storage = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/storage']")
    okof = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/okof']")
    ofof_2017 = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/okof2017']")
    templates_of_the_card_os_nma_npa = (By.XPATH,
                                        "//*[@href='#/non-financial-assets/classifiers/basic-facilities-template']")
    ifns = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/ifns']")
    commission_orders = (By.XPATH, "//*[@href='#/non-financial-assets/classifiers/committee']")


# оборотная ведомость
class TurnoverStatementLocators(object):
    date_from = (By.XPATH, "//date-input[@name='dateFrom']//input")
    date_to = (By.XPATH, "//date-input[@name='dateTo']//input")
    balance_sheet_account = (By.XPATH, "//balance-sheet-account-classifier[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH, "//*[@name='balanceSheetAccountGroup']")
    account_unit = (By.XPATH, "//account-units-dropdown-input[@name='accountUnits']//select")
    is_only_out_balance = (By.XPATH, "//check-input[@name='isOnlyOutBalance']//input")


class CashExpenseRequestLocators(object):

    class DocumentHeader(object):
        document_number = (By.XPATH, "//input[@id='documentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        document_kind = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        ofk_number = (By.XPATH, "//input[@id='ofkNumber']")
        entry_date = (By.XPATH, "//input[@id='EntryDate']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")
        current_organization_account = (By.XPATH, "(//button[@title='Выбрать'])[3]")
        short = (By.XPATH, "//input[@id='short']")
        limit_date = (By.XPATH, "//input[@id='limitDate']")
        tracking_number = (By.XPATH, "//input[@id='trackingNumber']")
        federal_targeted_investment_program = (By.XPATH, "(//button[@title='Выбрать'])[4]")
        priority = (By.XPATH, "//input[@id='priority']")
        currency_amount = (By.XPATH, "//input[@id='currencyAmount']")
        currency_nds_amount = (By.XPATH, "//input[@id='currencyNdsAmount']")
        currency_classifier = (By.XPATH, "(//button[@title='Выбрать'])[5]")
        amount = (By.XPATH, "//input[@id='amount']")
        nds_amount = (By.XPATH, "//input[@id='ndsAmount']")
        amount_without_nds = (By.XPATH, "//input[@id='amountWithoutNds']")
        is_advance = (By.XPATH, "//input[@id='isAdvance']")
        payment_priority = (By.XPATH, "//input[@id='paymentPriority']")
        payment_form = (By.XPATH, "//select[@name='paymentForm']")
        payment_purpose = (By.XPATH, "//input[@id='paymentPurpose']")
        document_foundation = (By.XPATH, "(//button[@title='Выбрать'])[6]")
        document_foundation_kind = (By.XPATH, "(//button[@title='Выбрать'])[7]")
        document_foundation_number = (By.XPATH, "//input[@id='documentFoundationNumber']")
        document_foundation_date = (By.XPATH, "//input[@id='documentFoundationDate']")
        document_foundation_subject = (By.XPATH, "//input[@id='documentFoundationSubject']")
        counterparty = (By.XPATH, "(//button[@title='Выбрать'])[8]")
        counterparty_account_details = (By.XPATH, "(//button[@title='Выбрать'])[9]")
        is_employee = (By.XPATH, "//input[@id='isEmployee']")
        is_tax = (By.XPATH, "//input[@id='isTax']")
        chief = (By.XPATH, "(//button[@title='Выбрать'])[10]")
        chief_account = (By.XPATH, "(//button[@title='Выбрать'])[11]")

    class Requisites(object):

        document = (By.XPATH, "(//button[@title='Выбрать'])[12]")
        document_type = (By.XPATH, "(//button[@title='Выбрать'])[13]")
        document_number = (By.XPATH, "//input[@id='documentNumber']")
        document_date = (By.XPATH, "//input[@id='documentDate']")
        subject = (By.XPATH, "//input[@id='subject']")

    class Transcript(object):
        activity_kind = (By.XPATH, "//select[@name='activityKind']")
        kbk = (By.XPATH, "(//button[@title='Выбрать'])[12]")
        drawee_kbk_type = (By.XPATH, "//select[@name='drawee_kbk_type']")
        kosgu = (By.XPATH, "(//button[@title='Выбрать'])[13]")
        cost_element = (By.XPATH, "(//button[@title='Выбрать'])[14]")
        recepient_kbk = (By.XPATH, "(//button[@title='Выбрать'])[15]")
        recepient_kbk_type = (By.XPATH, "//select[@name='recepientKbkType']")
        goal_code = (By.XPATH, "(//button[@title='Выбрать'])[16]")
        department = (By.XPATH, "(//button[@title='Выбрать'])[17]")
        expenditure_goal_act = (By.XPATH, "(//button[@title='Выбрать'])[18]")
        document_foundation_counterparty = (By.XPATH, "(//button[@title='Выбрать'])[19]")
        foundation = (By.XPATH, "(//button[@title='Выбрать'])[20]")
        report_code = (By.XPATH, "(//button[@title='Выбрать'])[21]")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[22]")
        currency_amount = (By.XPATH, "//input[@id='currencyAmount']")
        currency_nds_amount = (By.XPATH, "//input[@id='currencyNdsAmount']")
        amount = (By.XPATH, "//input[@id='amount']")
        nds_amount = (By.XPATH, "//input[@id='ndsAmount']")
        amount_without_nds = (By.XPATH, "//input[@id='amountWithoutNds']")
        nds_percent = (By.XPATH, "//input[@id='ndsPercent']")
        payment_purpose = (By.XPATH, "//input[@id='paymentPurpose']")
        comment = (By.XPATH, "//input[@id='comment']")
        drawee_subsidy_code = (By.XPATH, "//input[@id='draweeSubsidyCode']")
        recepient_subsidy_code = (By.XPATH, "//input[@id='recepientSubsidyCode']")
        act = (By.XPATH, "(//button[@title='Выбрать'])[23]")


class CashPullRequestLocators(object):
    filter = (By.XPATH, "//input[@placeholder='Все поля']")

    class HoldingRequest(object):
        lddate_prov = (By.XPATH, "//input[@id='lddate_prov']")
        typical_operation = (By.XPATH, "//button[@title='Выбрать']")
        submit = (By.XPATH, "//button[.='Провести']")

    class NewDocument(object):
        # Реквизиты документа
        account_number = (By.XPATH, "(//button[@title='Выбрать'])[1]")
        tracking_number = (By.XPATH, "//input[@id='TrackingNumber']")
        operation = (By.XPATH, "(//button[@title='Выбрать'])[2]")
        # Информация о документе
        document_number = (By.XPATH, "//input[@id='DocumentNumber']")
        document_date = (By.XPATH, "//input[@id='date1']")
        entry_date = (By.XPATH, "//input[@id='date2']")
        deadline = (By.XPATH, "//input[@id='date3']")
        # Дополнительно - Доверенность
        trustee = (By.XPATH, "(//button[@title='Выбрать'])[3]")
        trustee_name_dative_case = (By.XPATH, "//input[@id='TrusteeNameDativeCase']")
        trustee_position = (By.XPATH, "(//button[@title='Выбрать'])[4]")
        trustee_position_dative_case = (By.XPATH, "//input[@id='TrusteePositionDativeCase']")
        foundation = (By.XPATH, "//input[@id='Foundation']")
        # Дополнительно - Чек
        check_series = (By.XPATH, "//input[@id='CheckSeries']")
        check_number = (By.XPATH, "//input[@id='CheckNumber']")
        check_date = (By.XPATH, "//input[@id='CheckDate']")
        check_valid_till = (By.XPATH, "//input[@id='CheckValidTill']")
        # Дополнительно - Подписывающие лица
        manager = (By.XPATH, "(//button[@title='Выбрать'])[5]")
        chief_accountant = (By.XPATH, "(//button[@title='Выбрать'])[6]")

        class NewLine(object):
            kbk = (By.XPATH, "(//button[@title='Выбрать'])[7]")
            kbk_type = (By.XPATH, "//select[@name='kbkType']")
            kosgu = (By.XPATH, "(//button[@title='Выбрать'])[8]")
            costs_type = (By.XPATH, "(//button[@title='Выбрать'])[9]")
            operation = (By.XPATH, "(//button[@title='Выбрать'])[10]")
            funds_source = (By.XPATH, "//select[@name='fundsSource']")
            cash_transaction_code = (By.XPATH, "//select[@name='CashTransactionCode']")
            code_goal = (By.XPATH, "//input[@id='CodeGoal']")
            payment_purpose = (By.XPATH, "//input[@id='PaymentPurpose']")
            amount = (By.XPATH, "//input[@id='amount']")
            comment = (By.XPATH, "//input[@id='Comment']")


class ZNVLocators(object):
    document_number = (By.XPATH, "//*[@name='documentNumber']//input")
    document_date = (By.XPATH, "//*[@name='documentDate']//input")
    personal_account = (By.XPATH, "//*[@name='accountDetails']")

    recipient_name = (By.XPATH, "(//button[@title='Выбрать'])[2]")
    ofk_registration_number = (By.XPATH, "//input[@id='ofkRegistrationNumber']")
    entry_date = (By.XPATH, "//input[@id='entryDate']")
    typical_operation = (By.XPATH, "(//button[@title='Выбрать'])[3]")
    recipient_account = (By.XPATH, "(//button[@title='Выбрать'])[4]")
    document_type = (By.XPATH, "(//button[@title='Выбрать'])[5]")

    class Request(object):
        # Закладка Расшифровка заявки
        summa_rub = (By.XPATH, "//input[@id='outstandingPaymentDocumentAmount']")
        kbk = (By.XPATH, "(//button[@title='Выбрать'])[6]")
        kosgu = (By.XPATH, "(//button[@title='Выбрать'])[7]")
        stavka_nds = (By.XPATH, "//input[@id='ndsPercent']")
        tip_kbk = (By.XPATH, "//select[@name='kbkType']")
        vid_zatrat = (By.XPATH, "(//button[@title='Выбрать'])[8]")
        summa_nds = (By.XPATH, "//input[@id='ndsAmount']")
        # Фрэйм Дополнительные реквизиты
        kod_cely = (By.XPATH, "//select[@name='goalCode']")
        oktmo = (By.XPATH, "(//button[@title='Выбрать'])[10]")

    class Doc(object):
        # Закладка Документы по зачислению невыясненного платежа
        number = (By.XPATH, "//input[@id='outstandingPaymentDocumentNumber']")


#   Приходный кассовый ордер
class IncomingOrderLocators(object):
    document_kind = (By.XPATH, "//*[@name='documentKind']")
    document_number = (By.XPATH, "//*[@name='documentNumber']//input")
    document_date = (By.XPATH, "//*[@name='documentDate']//input")
    entry_date = (By.XPATH, "//*[@name='entryDate']//input")
    employee = (By.XPATH, "//*[@name='employee']")
    organization = (By.XPATH, "//*[@name='organization']")
    received_from = (By.XPATH, "//*[@name='receivedFrom']//input")
    department_unit = (By.XPATH, "//*[@name='departmentUnit']")
    cash_report_number = (By.XPATH, "//*[@name='cashReportNumber']//input")
    foundation = (By.XPATH, "//*[@name='foundation']//textarea")
    operation = (By.XPATH, "//*[@name='operation']")


# Добавление  строки в Приходный кассовый ордер
class IncomingOrderAddLineLocators(object):
    operation = (By.XPATH, "//div[@class='modal in']//*[@name='operation']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    expense_type = (By.XPATH, "//cost-elements-classifier[@name='expenseType']")
    inventory = (By.XPATH, "//material-inventory-classifier[@name='inventory']")
    quantity = (By.XPATH, "//number-input[@name='quantity']//input")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    amount_without_nds = (By.XPATH, "//currency-input[@name='amountWithoutNds']//input")
    nds_percent = (By.XPATH, "//nds-percent-input[@name='ndsPercent']//input")
    nds_amount = (By.XPATH, "//currency-input[@name='ndsAmount']//input")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    recepient = (By.XPATH, "//materially-responsible-person-classifier[@name='recepient']")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    act = (By.XPATH, "//expenditure-goal-act-classifier[@name='act']")
    cash_transaction_code = (By.XPATH, "//cash-transaction-code-dropdown-input[@name='CashTransactionCode']//select")


# Добавление приложения в Приходный кассовый ордер
class IncomeCashOrderPlusLocators(object):
    document_foundation = (
        By.XPATH, "//div[@class='tab-content']//imprest-foundation-classifier[@name='documentFoundation']")
    advance_report = (By.XPATH, "//div[@class='tab-content']//advance-report-classifier[@name='advanceReport']")
    comment = (By.XPATH, "//div[@class='tab-content']//text-input[@name='comment']//input")
    chief_accountant = (By.XPATH, "//div[@class='tab-content']//signatory-classifier[@name='chiefAccountant']")
    cashier = (By.XPATH, "//div[@class='tab-content']//signatory-classifier[@name='cashier']")


# Локаторы для экспорта в УФК
class ExportUFKLocators(object):
    account_details = (By.XPATH, "//*[@name='accountDetails']")
    file_number = (By.XPATH, "//*[@name='fileNumber']//input")


# Локаторы для проведения документа
class CarryingOutOfDocumentsLocators(object):
    lddate_prov = (By.XPATH, "//*[@name='lddate_prov']//input")
    operation_master = (By.XPATH, "//*[@name='OperationMaster']")


class ContractWithSupplierLocators(object):
    documen_type = (By.XPATH, "//*[@name='documentKind']")
    number = (By.XPATH, "//*[@name='documentNumber']//input")
    date = (By.XPATH, "//*[@name='documentDate']//input")
    counter_party = (By.XPATH, "//*[@name='counterparty']")
    bank_account_number = (By.XPATH, "//*[@name='transactionAccount']")
    uin = (By.XPATH, "//*[@name='chargeUniqueIdentifier']//input")
    currency = (By.XPATH, "//*[@name='currency']")
    personal_account = (By.XPATH, "//current-organization-account-details-classifier[@name='personalAccount']")
    budget_commitment = (By.XPATH, "//budget-commitment-classifier[@name='budgetCommitment']")
    payment_against_invoice = (By.XPATH, "//check-input[@name='paymentAgainstInvoice']//input")
    payment_type = (By.XPATH, "//*[@name='considerationPeriod']//select")
    date_begin = (By.XPATH, "//*[@name='startDate']//input")
    date_end = (By.XPATH, "//*[@name='endDate']//input")
    security_type = (By.XPATH, "//security-type-dropdown-input[@name='securityType']//select")
    security_amount = (By.XPATH, "//currency-input[@name='securityAmount']//input")
    security_period = (By.XPATH, "//date-input[@name='securityPeriod']//input")
    sending_letter_number = (By.XPATH, "//text-input[@name='sendingLetterNumber']//input")
    assurance_register_record_number = (By.XPATH, "//text-input[@name='assuranceRegisterRecordNumber']//input")
    letter_date = (By.XPATH, "//date-input[@name='letterDate']//input")
    note = (By.XPATH, "//*[@name='comment']//textarea")
    responsible = (By.XPATH, "//employee-classifier[@name='responsible']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    penalty_period = (By.XPATH, "//penalty-period-dropdown[@name='penaltyPeriod']//select")
    penalty_percent = (By.XPATH, "//decimal-input[@name='penaltyPercent']//input")
    penalty_amount = (By.XPATH, "//currency-input[@name='penaltyAmount']//input")
    penalty_period_count = (By.XPATH, "//number-input[@name='penaltyPeriodCount']//select")
    subject_contract = (By.XPATH, "//*[@name='subject']//textarea")
    payment_terms = (By.XPATH, "//*[@name='paymentTerm']//textarea")
    prolongation_term = (By.XPATH, "//text-area-input[@name='prolongationTerm']//textarea")


# Договор с Поставщиком - вкладка Детализация по КБК
class ContractWithSupplierDetailKBKPageLocators(object):
    financial_year = (By.XPATH, "//*[@name='financialYear']//input")
    entry_date = (By.XPATH, "//*[@name='entryDate']//input")
    changed = (By.XPATH, "//*[@name='changed']//input")
    operation = (By.XPATH, "//*[@name='operation']")
    kbk = (By.XPATH, "//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    cost_Element = (By.XPATH, "//*[@name='costElement']")
    contract_subject = (By.XPATH, "//*[@name='contractSubject']//textarea")
    department = (By.XPATH, "//department-classifier[@name='Department']")
    budgetary_plan_act = (By.XPATH, "//act-classifier[@name='budgetaryPlanAct']")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    work = (By.XPATH, "//work-classifier[@name='work']")
    amounts_amount = (By.XPATH, "//*[@name='amountsAmount']//input")
    amounts_nds_percent = (By.XPATH, "//*[@name='amountsNdsPercent']//input")
    advance = (By.XPATH, "//*[@name='advance']//input")


# Договор с Поставщиком - вкладка  Детализация по ОКПД
class ContractWithSupplierDetailOKPDLocators(object):
    order_number = (By.XPATH, "//number-input[@name='orderNumber']//input")
    okpd2 = (By.XPATH, "//okpd2-classifier[@name='okpd2']")
    unit_of_measure = (By.XPATH, "//okei-classifier[@name='unitOfMeasure']")
    unit_price = (By.XPATH, "//currency-input[@name='unitPrice']//input")
    quantity = (By.XPATH, "//decimal-input[@name='quantity']//input")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    purchase_object_type = (By.XPATH, "//purchase-object-type-dropdown-input[@name='purchaseObjectType']")


# Договор с Поставщиком - Вкладка Сведения о госконтракте
class InformationAboutContractLocators(object):
    aviso = (By.XPATH, "//purchasing-notice-classifier[@name='aviso']")
    purchase_identity = (By.XPATH, "//text-input[@name='purchaseIdentity']//input")
    register_record_number = (By.XPATH, "//text-input[@name='registerRecordNumber']//input")
    registration_date = (By.XPATH, "//date-input[@name='registrationDate']//input")
    privacy = (By.XPATH, "//privacy-dropdown-input[@name='privacy']//select")
    confirm_document_number = (By.XPATH, "//number-input[@name='confirmDocumentNumber']//input")
    confirm_document_date = (By.XPATH, "//date-input[@name='confirmDocumentDate']//input")
    confirm_document_kind = (By.XPATH, "//contract-award-foundation-classifier[@name='confirmDocumentKind']")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    department = (By.XPATH, "//order-placement-classifier[@name='department']")
    auction_date = (By.XPATH, "//date-input[@name='auctionDate']//input")
    declared_value = (By.XPATH, "//currency-input[@name='declaredValue']//input")
    change_foundation = (By.XPATH, "//text-input[@name='changeFoundation']//input")
    for_small_entrepreneur = (By.XPATH, "//check-input[@name='forSmallEntrepreneur']//input")
    domestic_goods_preference = (By.XPATH, "//check-input[@name='domesticGoodsPreference']//input")
    perfomance_document_number = (By.XPATH, "//text-input[@name='perfomanceDocumentNumber']//input")
    contract_performance_date = (By.XPATH, "//date-input[@name='contractPerformanceDate']//input")
    terminated_by = (By.XPATH, "//termination-reason-dropdown-input[@name='terminatedBy']//select")
    contract_cancellation_record_number = (By.XPATH, "//text-input[@name='contractCancellationRecordNumber']//input")
    contract_perfomance_foundation = (By.XPATH, "//text-area-input[@name='contractPerfomanceFoundation']//textarea")


# Договор с Поставщиком - История
class HistoryLocators(object):
    change_date = (By.XPATH, "//date-input[@name='changeDate']//input")
    change_number = (By.XPATH, "//number-input[@name='changeNumber']//input")
    change_type = (By.XPATH, "//contract-with-supplier-change-type-dropdown-input[@name='changeType']//select")
    comment = (By.XPATH, "//text-area-input[@name='comment']//input")


# Договор с Поставщиком - Календарный план
class CalendarPlanLocators(object):
    financial_year = (By.XPATH, "//number-input[@name='financialYear']//input")
    work_name = (By.XPATH, "//text-area-input[@name='workName']//textarea")
    result = (By.XPATH, "//text-area-input[@name='result']//textarea")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    start_date = (By.XPATH, "//date-input[@name='startDate']//input")
    end_date = (By.XPATH, "//date-input[@name='endDate']//input")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    account_details = (By.XPATH, "//counterparty-account-details-classifier[@name='accountDetails']")


# Обеспечение исполнения обязательств
class EnsuringFulfillmentOfObligationsLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    retirement_date = (By.XPATH, "//date-input[@name='retirementDate']//input")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    guarantor = (By.XPATH, "(//counterparty-classifier[@name='counterparty'])[2]")
    assurance_starts = (By.XPATH, "//date-input[@name='assuranceStarts']//input")
    assurance_ends = (By.XPATH, "//date-input[@name='assuranceEnds']//input")


# Сведения о бюджетном обязательстве
class InformationAboutBudgetObligationLocators(object):
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    financial_year = (By.XPATH, "//number-input[@name='financialYear']//input")
    liability = (By.XPATH, "//liability-dropdown-input[@name='liability']//select")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    registration_date = (By.XPATH, "//date-input[@name='registrationDate']//input")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    guid = (By.XPATH, "//text-input[@name='guid']//input")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    transaction_account = (By.XPATH, "//counterparty-account-details-classifier[@name='transactionAccount']")
    chief = (By.XPATH, "//signatory-classifier[@name='Chief']")
    prepared_by = (By.XPATH, "//signatory-classifier[@name='PreparedBy']")


# Сведения о бюджетном обязательстве
class InformationAboutBudgetObligationDopLocators(object):
    counterparty = (By.XPATH, "//div[@class='modal-content']//*[@id='counterparty']//input")
    account_details = (By.XPATH, "//div[@class='modal-content']//*[@id='accountDetails']//input")


# Сведения о бюджетном обязательстве строки
class InformationAboutBudgetObligationAddLineLocators(object):
    financial_year = (By.XPATH, "//text-input[@name='financialYear']//input")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    activity_kind = (By.XPATH, "//activity-kind-dropdown-input[@name='activityKind']//select")
    kbk_type = (By.XPATH, "//kbk-type-dropdown-input[@name='kbkType']//select")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    current_year_amounts = (By.XPATH, "//currency-input[@name='currentYearAmounts']//input")
    february = (By.XPATH, "//currency-input[@name='february']//input")
    march = (By.XPATH, "//currency-input[@name='march']//input")
    april = (By.XPATH, "//currency-input[@name='april']//input")
    may = (By.XPATH, "//currency-input[@name='may']//input")
    june = (By.XPATH, "//currency-input[@name='june']//input")
    july = (By.XPATH, "//currency-input[@name='july']//input")
    august = (By.XPATH, "//currency-input[@name='august']//input")
    september = (By.XPATH, "//currency-input[@name='september']//input")
    october = (By.XPATH, "//currency-input[@name='october']//input")
    november = (By.XPATH, "//currency-input[@name='november']//input")
    december = (By.XPATH, "//currency-input[@name='december']//input")
    first_year_amount = (By.XPATH, "//currency-input[@name='firstYearAmount']//input")
    second_year_amount = (By.XPATH, "//currency-input[@name='secondYearAmount']//input")
    third_year_amount = (By.XPATH, "//currency-input[@name='thirdYearAmount']//input")
    other_years_amount = (By.XPATH, "//currency-input[@name='otherYearsAmount']//input")
    completed_amout = (By.XPATH, "//currency-input[@name='completedAmout']//input")
    not_completed_amount = (By.XPATH, "//currency-input[@name='notCompletedAmount']//input")
    conditional_payment = (By.XPATH, "//check-input[@name='conditionalPayment']//input")
    analytical_code = (By.XPATH, "//text-input[@name='analyticalCode']//input")
    act = (By.XPATH, "//act-classifier[@name='act']")
    payment_day = (By.XPATH, "//number-input[@name='paymentDay']//input")


# Сведения о бюджетном обязательстве - история
class InformationAboutBudgetObligationHistoryLocators(object):
    change_number = (By.XPATH, "//text-input[@name='changeNumber']//input")
    change_date = (By.XPATH, "//date-input[@name='changeDate']//input")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# Сведения о бюджетном обязательстве -  Реквизиты документа-основания
class InformationAboutBudgetObligationRequisitesLocators(object):
    document_foundation_kind = (
        By.XPATH, "//budget-commitment-info-kind-dropdown-input[@name='documentFoundationKind']//select")
    document_foundation_number = (By.XPATH, "//text-input[@name='documentFoundationNumber']//input")
    document_foundation_date = (By.XPATH, "//date-input[@name='documentFoundationDate']//input")
    document_fondation_currency = (By.XPATH, "//currency-classifier[@name='documentFondationCurrency']")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    currency_amount = (By.XPATH, "//currency-input[@name='currencyAmount']//input")
    advance_percent = (By.XPATH, "//decimal-input[@name='advancePercent']//input")
    advance_amount = (By.XPATH, "//currency-input[@name='advanceAmount']//input")
    register_record_number = (By.XPATH, "//number-input[@name='registerRecordNumber']//input")
    document_foundation_subject = (By.XPATH, "//text-input[@name='documentFoundationSubject']//input")


# Локаторы для Справочника «ОС,НМА,НПА»
class CardIndexOSNMANPALocators(object):
    tag_no_first_part = (By.XPATH, "//*[@name='tagNoFirstPart']//input")
    tag_no_second_part = (By.XPATH, "//*[@name='tagNoSecondPart']//input")
    tag_no = (By.XPATH, "//*[@name='tagNo']//input")
    template = (By.XPATH, "//*[@name='template']")
    full_name = (By.XPATH, "//*[@name='fullName']//input")
    supplier = (By.XPATH, "//*[@name='supplier']")
    property_designation = (By.XPATH, "//*[@name='propertyDesignation']//input")
    issue_date = (By.XPATH, "//*[@name='issueDate']//input")
    start_up_date = (By.XPATH, "//*[@name='startUpDate']//input")
    serialNumber = (By.XPATH, "//*[@name='serialNumber']//input")
    # group = (By.XPATH, "//li[contains(.,'С/блоки')]")
    group = (By.XPATH, "//*[@name='group']")
    unit_of_measure = (By.XPATH, "//*[@name='unitOfMeasure']")
    cost = (By.XPATH, "//*[@name='cost']//input")
    exclude_from_depreciation_accrual = (By.XPATH, "//*[@name='exludeFromDepreciationAccrual']//input")
    value_added_used = (By.XPATH, "//*[@name='valueAddedUsed']//input")
    amortization_group = (By.XPATH, "//*[@name='amortizationGroup']")
    okof = (By.XPATH, "//*[@name='okof']")


# Локаторы для Справочника «Материально ответственные лица»
class MateriallyResponsiblePersonLocators(object):
    employee = (By.XPATH, "//*[@name='employee']")
    name = (By.XPATH, "//*[@name='name']//input")
    full_name = (By.XPATH, "//*[@name='fullName']//input")
    position = (By.XPATH, "//*[@name='position']")
    valid_till = (By.XPATH, "//*[@name='validTill']//input")


# Локаторы для Справочника «Поступление НФА - шапка»
class ReceiptOfNonFinancialAssetsCapLocators(object):
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    materially_responsible_person = \
        (By.XPATH, "//materially-responsible-person-classifier[@name='materiallyResponsiblePerson']")
    sender_sender_type = (By.XPATH, "//income-sender-type-enum[@name='senderSenderType']//select")
    organization = (By.XPATH, "//counterparty-classifier[@name='organization']")
    storage = (By.XPATH, "//storage-classifier[@name='storage']")
    advance_report = (By.XPATH, "//advance-report-classifier[@name='advanceReport']")
    sender_foundation = (By.XPATH, "//*[@name='senderFoundation']")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")



# Локаторы для Справочника «Поступление НФА - строки»
class ReceiptOfNonFinancialAssetsRowLocators(object):
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    tag_no = (By.XPATH, "//number-input[@name='tagNo']//input")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    amortization = (By.XPATH, "//currency-input[@name='amortization']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//*[@name='comment']//textarea")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")


# Локаторы для Справочника «Шаблоны карточки ОС, НМА, НПА»
class CreateATemplateForTheCardOSNMANPALocators(object):
    name = (By.XPATH, "//text-input[@name='name']//input")
    unit_of_measure = (By.XPATH, "//okei-classifier[@name='unitOfMeasure']")
    group = (By.XPATH, "//basic-facilities-group-classifier[@name='group']")
    okof = (By.XPATH, "//okof-hierarchy-classifier[@name='okof']")
    amortization_group = (By.XPATH, "//amortization-group-classifier[@name='amortizationGroup']")


# Локаторы для Массового заполнения параметров объектов
class MassFillingOfOsParametersLocators(object):
    unit_of_measure = (By.XPATH, "//okei-classifier[@name='unitOfMeasure']")
    property_designation = (By.XPATH, "//text-input[@name='propertyDesignation']//input")
    start_up_date = (By.XPATH, "//date-input[@name='startUpDate']//input")
    issue_date = (By.XPATH, "//date-input[@name='issueDate']//input")


# Локаторы для Справочника «Группы МЗ»
class CreationOfANewEntryInTheDirectoryGroupMzLocators(object):
    order_number = (By.XPATH, "//number-input[@name='orderNumber']//input")
    full_name = (By.XPATH, "//text-input[@name='fullName']//input")
    name = (By.XPATH, "//text-input[@name='name']//input")


# Локаторы для Справочника «Объекты МЗ» - шапка
class CreationOfAnEntryInTheDirectoryObjectsOfOzCapLocators(object):
    tag_no = (By.XPATH, "//number-input[@name='tagNo']//input")
    name = (By.XPATH, "//text-input[@name='name']//input")
    unit_of_measure = (By.XPATH, "//okei-classifier[@name='unitOfMeasure']")
    group = (By.XPATH, "//material-inventory-group-classifier[@name='group']")
    valid_till = (By.XPATH, "//date-input[@name='validTill']//input")


# Локаторы для Справочника «Объекты МЗ» - строки
class CreationOfAnEntryInTheDirectoryObjectsOfOzRowLocators(object):
    open = (By.XPATH, "(//button[contains(.,'Открыть')])")
    add = (By.XPATH, "(//button[contains(.,'Добавить')])")
    delete = (By.XPATH, "(//button[contains(.,'Добавить')])")
    name = (By.XPATH, "(//text-input[@name='name']//input)[2]")
    price = (By.XPATH, "//currency-input[@name='price']//input")
    acquisition_date = (By.XPATH, "//date-input[@name='acquisitionDate']//input")


# Локаторы для справочника «Приказы о назначении комиссии» - шапка
class CreationOfACommissionOrderCapLocators(object):
    order_number = (By.XPATH, "//text-input[@name='orderNumber']//input")
    order_date = (By.XPATH, "//date-input[@name='orderDate']//input")
    comment = (By.XPATH, "//text-input[@name='comment']//input")
    valid_till = (By.XPATH, "//date-input[@name='validTill']//input")


# Локаторы для справочника «Приказы о назначении комиссии» - строки
class CreationOfACommissionOrderRowLocators(object):
    order = (By.XPATH, "//text-input[@name='order']//input")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    position = (By.XPATH, "//position-classifier[@name='position']")


# Локаторы для модального окна - Печать - «Акт о приеме-передаче объектов нефинансовых активов»
class ModalWindowTheActOfAcceptanceTransferOfObjectsOfNonFinancialAssetsLocators(object):
    committee = (By.XPATH, "//committee-classifier[@name='committee']")
    foundation_document = (By.XPATH, "//text-input[@name='foundationDocument']//input")
    foundation_number = (By.XPATH, "//text-input[@name='foundationNumber']//input")
    foundation_date = (By.XPATH, "//date-input[@name='foundationDate']//input")
    sender_chief_position = (By.XPATH, "//text-input[@name='senderChiefPosition']//input")
    sender_chief_name = (By.XPATH, "//text-input[@name='senderChiefName']//input")
    recipient_chief_position = (By.XPATH, "//text-input[@name='recipientChiefPosition']//input")
    recipient_chief_name = (By.XPATH, "//text-input[@name='recipientChiefName']//input")


# Локаторы для модального окна - Печать - «Акт о приеме-сдаче отремонтированных,
# реконструированных и модернизированных объектов основных средств»
class ModalWindowOfTheActOnAcceptanceAndTransferOfObjectsOfNonFinancialAssetsLocators(object):
    committee = (By.XPATH, "//committee-classifier[@name='committee']")
    inventory_date_from = (By.XPATH, "//date-input[@name='inventoryDateFrom']//input")
    inventory_date_to = (By.XPATH, "//date-input[@name='inventoryDateTo']//input")


# Локаторы для модального окна - «Изменение параметров в отмеченных записях»
class ModalWindowChangingParametersInMarkedRecordsLocators(object):
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    storage = (By.XPATH, "//storage-classifier[@name='storage']")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    foundation = (By.XPATH, "//income-from-organization-document-foundation-classifier[@name='foundation']")
    comment = (By.XPATH, "//text-input[@name='comment']")


# Локаторы для модального окна - «Расчет по бухгалтерским данным»
class AccountingCalculationLocators(object):
    balances_collection_date = (By.XPATH, "//date-input[@name='balancesCollectionDate']//input")
    operation_date = (By.XPATH, "//date-input[@name='operationDate']//input")
    balance_sheet_account = (By.XPATH, "//balance-sheet-account-classifier[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH,
                                   "//balance-sheet-account-group-classifier[@name='balanceSheetAccountGroup']")


# Локаторы для модальное окна - Просмотр остатков по счету
class ViewingOfAccountBalancesLocators(object):
    clear_field_account = (By.XPATH, "//button[@class='btn btn-clear']")
    date = (By.XPATH, "//date-input[@name='date']//input")
    balance_sheet_account = (By.XPATH, "//balance-sheet-account-classifier[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH,
                                   "//balance-sheet-account-group-classifier[@name='balanceSheetAccountGroup']")
    materially_responsible_person = (By.XPATH,
                                     "//materially-responsible-person-classifier[@name='materiallyResponsiblePerson']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    basic_facilities = (By.XPATH, "//basic-facilities-classifier[@name='basicFacilities']")
    price_from = (By.XPATH, "//currency-input[@name='priceFrom']//input")
    price_to = (By.XPATH, "//currency-input[@name='priceTo']//input")
    name_query = (By.XPATH, "//text-input[@name='nameQuery']//input")


# Локаторы для модального окна - Массовое заполнение параметров объектов - остатки НФА
class BulkFillingOfObjectParametersOfRemnantsNfaLocators(object):
    date = (By.XPATH, "//date-input[@name='date']//input")
    balance_sheet_account = (By.XPATH, "//balance-sheet-account-classifier[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH,
                                   "//balance-sheet-account-group-classifier[@name='balanceSheetAccountGroup']")
    materially_responsible_person = (By.XPATH,
                                     "//materially-responsible-person-classifier[@name='materiallyResponsiblePerson']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    basic_facilities = (By.XPATH, "//basic-facilities-classifier[@name='basicFacilities']")
    price_from = (By.XPATH, "//currency-input[@name='priceFrom']//input")
    price_to = (By.XPATH, "//currency-input[@name='priceTo']//input")
    name_query = (By.XPATH, "//text-input[@name='nameQuery']//input")


class ApplicationCashFlowLocators(object):
    documen_type = (By.XPATH, "//*[@name='documentKind']")
    number = (By.XPATH, "//*[@name='documentNumber']//input")
    date = (By.XPATH, "//*[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    personal_account = (By.XPATH, "//*[@name='accountDetails']")
    bank_account_number = (By.XPATH, "//*[@name='counterpartyAccountDetails']")
    recipient = (By.XPATH, "//*[@name='counterparty']")
    number_ufk = (By.XPATH, "//*[@name='ofkNumber']//input")
    limit_date = (By.XPATH, "//*[@name='limitDate']//input")
    is_employee = (By.XPATH, "//check-input[@name='isEmployee']//input")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    imprest_foundation = (By.XPATH, "//imprest-foundation-classifier[@name='imprestFoundation']")
    advance_report = (By.XPATH, "//advance-report-classifier[@name='advanceReport']")
    foundation = (By.XPATH, "//div[@class='tab-content']//*[@name='foundation']")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    document_foundaiont_kind = (By.XPATH, "//document-foundation-kind-autocomplete[@name='documentFoundaiontKind']")
    document_foundation_number = (By.XPATH, "//text-input[@name='documentFoundationNumber']//input")
    document_foundation_date = (By.XPATH, "//date-input[@name='documentFoundationDate']//input")
    document_foundation_subject = (By.XPATH, "//text-area-input[@name='documentFoundationSubject']//textarea")
    operation = (By.XPATH, "//*[@name='operation']")
    currency = (By.XPATH, "//currency-classifier[@name='currency']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    priority = (By.XPATH, "//text-input[@name='priority']//input")
    is_advance = (By.XPATH, "//check-input[@name='isAdvance']//input")
    priority_of_payment = (By.XPATH, "//*[@name='paymentPriority']//input")
    payment_type = (By.XPATH, "//*[@name='paymentForm']//select")
    payment_purpose = (By.XPATH, "//text-area-input[@name='paymentPurpose']//textarea")
    chief = (By.XPATH, "//signatory-classifier[@name='chief']")
    accountant_general = (By.XPATH, "//signatory-classifier[@name='accountantGeneral']")


# Заявка на кассовый расход добавление строки
class DecodingOfTheApplicationLocators(object):
    activity_kind = (
        By.XPATH, "//div[@class='modal-content']//activity-kind-dropdown-input[@name='activityKind']//select")
    operation = (By.XPATH, "//div[@class='modal-content']//*[@name='operation']")
    kbk = (By.XPATH, "//div[@class='modal-content']//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    cost_element = (By.XPATH, "//*[@name='costElement']")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    nds_percent = (By.XPATH, "//*[@name='ndsPercent']//input")
    recepient_kbk = (By.XPATH, "//div[@class='modal-content']//recepient-kbk-autocomplete[@name='recepientKbk']")
    recepient_kbk_type = (
        By.XPATH, "//div[@class='modal-content']//kbk-type-dropdown-input[@name='recepientKbkType']//select")
    expenditure_goal_act = (
        By.XPATH, "//div[@class='modal-content']//expenditure-goal-act-classifier[@name='expenditureGoalAct']")
    department = (By.XPATH, "//div[@class='modal-content']//department-classifier[@name='department']")
    document_foundation_counterparty = (By.XPATH, "//*[@name='documentFoundationCounterparty']")
    foundation = (By.XPATH, "//div[@class='modal-content']//*[@name='foundation']")
    payment_purpose = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='paymentPurpose']//textarea")
    comment = (By.XPATH, "//*[@name='comment']//textarea")
    draweeKbkType = (By.XPATH, "//*[@name='draweeKbkType']//select")
    typeOfFunds = (By.XPATH, "//*[@name='activityKind']//select")


# Заявка на кассовый расход  реквизиты документа основания
class ApplicationCashFlowRequisitesLocators(object):
    document = (By.XPATH, "//div[@class='modal-content']//payment-basis-classifier[@name='document']")
    document_type = (
        By.XPATH, "//div[@class='modal-content']//document-foundation-kind-autocomplete[@name='documentType']")
    document_number = (By.XPATH, "//div[@class='modal-content']//text-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//div[@class='modal-content']//date-input[@name='documentDate']//input")
    subject = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='subject']//textarea")


# Заявка на кассовый расход - Реквизиты налоговых платежей
class ApplicationCashFlowRequisitesTaxPaymentsLocators(object):
    taxpayer_status = (By.XPATH, "//taxpayer-status-dropdown-input[@name='taxpayerStatus']//select")
    tax_period = (By.XPATH, "//field107-input[@name='taxPeriod']//input")
    is_tax = (By.XPATH, "//check-input[@name='isTax']//input")
    kbk = (By.XPATH, "//kbk-tax-autocomplete[@name='kbk']")
    tax_bill_number = (By.XPATH, "//text-input[@name='taxBillNumber']//input")
    oktmo = (By.XPATH, "//oktmo-autocomplete[@name='oktmo']")
    tax_bill_date = (By.XPATH, "//date-input[@name='taxBillDate']//input")
    reason_for_payment = (By.XPATH, "//reason-for-payment-dropdown-input[@name='reasonForPayment']//select")


# Платежное поручение (приход средств)
class PaymentOrderArrivalLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    recipient_account_details = (
        By.XPATH, "//current-organization-account-details-classifier[@name='recipientAccountDetails']")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    drawee = (By.XPATH, "//counterparty-classifier[@name='drawee']")
    drawee_account_details = (By.XPATH, "//counterparty-account-details-classifier[@name='draweeAccountDetails']")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    currency = (By.XPATH, "//currency-classifier[@name='currency']")
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    act = (By.XPATH, "//act-classifier[@name='act']")
    payment_purpose = (By.XPATH, "//text-area-input[@name='paymentPurpose']//textarea")
    is_employee = (By.XPATH, "//check-input[@name='isEmployee']//input")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    purchasing_notice = (By.XPATH, "//purchasing-notice-classifier[@name='purchasingNotice']")
    notification_number = (By.XPATH, "//text-input[@name='notificationNumber']//input")
    payment_form = (By.XPATH, "//facilitiesoutflow-payment-form-dropdown-input[@name='paymentForm']//select")


# Платежное поручение (приход средств) бланк
class PaymentOrderArrivalBlankLocators(object):
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='kbk']")
    operation = (By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='operation']")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//cost-elements-classifier[@name='costElement']")
    department_unit = (By.XPATH, "//div[@class='modal-content']//department-unit-classifier[@name='departmentUnit']")
    act = (By.XPATH, "//div[@class='modal-content']//act-classifier[@name='act']")
    imprest_foundation = (
        By.XPATH, "//div[@class='modal-content']//imprest-foundation-classifier[@name='imprestFoundation']")
    vat_percent = (By.XPATH, "//div[@class='modal-content']//nds-percent-input[@name='vatPercent']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//amount-input[@name='amount']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")


# Платежное поручение (приход средств) реквизиты
class PaymentOrderArrivalRequisitesLocators(object):
    taxpayer_status = (By.XPATH, "//taxpayer-status-dropdown-input[@name='taxpayerStatus']//select")
    kbk = (By.XPATH, "//kbk-tax-autocomplete[@name='kbk']")
    oktmo = (By.XPATH, "//oktmo-autocomplete[@name='oktmo']")
    tax_period = (By.XPATH, "//field107-input[@name='taxPeriod']//input")
    tax_bill_number = (By.XPATH, "//text-input[@name='taxBillNumber']//input")
    tax_bill_date = (By.XPATH, "//date-input[@name='taxBillDate']//input")
    reason_for_payment = (By.XPATH, "//reason-for-payment-dropdown-input[@name='reasonForPayment']//select")


class InvoiceFromTheSupplierLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    supplier = (By.XPATH, "//counterparty-classifier[@name='supplier']")
    paid_date = (By.XPATH, "//date-input[@name='paidDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='DepartmentUnit']")
    supplier_account_detail = (By.XPATH, "//counterparty-account-details-classifier[@name='supplierAccountDetail']")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    department = (By.XPATH, "//department-classifier[@name='Department']")
    note = (By.XPATH, "//text-area-input[@name='comment']//textarea")


class InvoiceFromTheSupplierAddLineLocators(object):
    add = (By.XPATH, "//button[contains(.,'Добавить')]")
    add_new = (By.XPATH, "//a[.='Новую строку']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    act = (By.XPATH, "//act-classifier[@name='act']//input")
    okpd2 = (By.XPATH, "//okpd2-classifier[@id='okpd2']//input")
    comment = (By.XPATH, "//div[@class='modal in']//*[@name='comment']//textarea")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    vat_percent = (By.XPATH, "//nds-percent-input[@name='vatPercent']//input")
    paid_date = (By.XPATH, "//date-input[@name='paidDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='DepartmentUnit']")


# Cчет фактура от поставщика
class InvoiceFromVendorLocators(object):
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    received_date = (By.XPATH, "//date-input[@name='receivedDate']//input")
    correction_number = (By.XPATH, "//number-input[@name='correctionNumber']//input")
    correction_date = (By.XPATH, "//date-input[@name='correctionDate']//input")
    editable = (By.XPATH, "//tax-invoice-from-supplier-classifier[@name='editable']")
    vendor = (By.XPATH, "//counterparty-classifier[@name='vendor']")
    billing_type = (By.XPATH, "//billing-type-dropdown-input[@name='billingType']//select")
    nds_operation_code = (By.XPATH, "//nds-operation-code-classifier[@name='ndsOperationCode']")
    public_contract_identifier = (By.XPATH, "//text-input[@name='publicContractIdentifier']//input")
    mercantile_agent = (By.XPATH, "//counterparty-classifier[@name='mercantileAgent']")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='DepartmentUnit']")
    trip = (By.XPATH, "//imprest-foundation-classifier[@name='Trip']")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    capitalization_date = (By.XPATH, "//date-input[@name='capitalizationDate']//input")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# Cчет фактура от поставщика - добавление строки
class InvoiceFromVendorAddLineLocators(object):
    goods_name = (By.XPATH, "//text-input[@name='goodsName']//input")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_elements = (By.XPATH, "//cost-elements-classifier[@name='costElements']")
    act = (By.XPATH, "//act-classifier[@name='act']")
    unit_of_measure = (By.XPATH, "//okei-classifier[@name='unitOfMeasure']")
    quantity = (By.XPATH, "//decimal-input[@name='quantity']//input")
    price = (By.XPATH, "//currency-input[@name='price']//input")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    excise_duty = (By.XPATH, "//currency-input[@name='exciseDuty']//input")
    nds_amount = (By.XPATH, "//currency-input[@name='ndsAmount']//input")
    cargo_custom_declaration = (By.XPATH, "//text-input[@name='cargoCustomDeclaration']//input")
    origin_country = (By.XPATH, "//country-classifier[@name='originCountry']")
    nds_percent = (By.XPATH, "//nds-percent-input[@name='ndsPercent']//input")


# Акт входящий
class IncomingActLocators(object):
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    contractor = (By.XPATH, "//counterparty-classifier[@name='contractor']")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='DepartmentUnit']")
    Appointment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_elements = (By.XPATH, "//cost-elements-classifier[@name='costElements']")
    nds_percent = (By.XPATH, "//nds-percent-input[@name='ndsPercent']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//amount-input[@name='amount']//input")
    advance_offset = (By.XPATH, "//currency-input[@name='advanceOffset']//input")
    under_repair = (By.XPATH, "//basic-facilities-classifier[@name='underRepair']")
    comment = (By.XPATH, "//div[@class='modal-content']//*[@name='comment']//textarea")


# Сведения о денежном обязательстве
class InformationAboutTheMonetaryObligationLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    financial_year = (By.XPATH, "//number-input[@name='financialYear']//input")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    currency = (By.XPATH, "//currency-classifier[@name='currency']")
    is_advance = (By.XPATH, "//check-input[@name='isAdvance']//input")
    registration_date = (By.XPATH, "//date-input[@name='registrationDate']//input")
    personal_account = (By.XPATH, "//current-organization-account-details-classifier[@name='personalAccount']")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    counterparty_account_detail = (By.XPATH, "//*[@name='counterpartyAccountDetail']")
    guid = (By.XPATH, "//text-input[@name='guid']//input")
    chief = (By.XPATH, "//signatory-classifier[@name='chief']")
    accountant_general = (By.XPATH, "//signatory-classifier[@name='accountantGeneral']")
    document_foundation_kind = (By.XPATH, "//*[@name='documentFoundationKind']//select")
    foundation_number = (By.XPATH, "//text-input[@name='foundationNumber']//input")
    foundation_date = (By.XPATH, "//date-input[@name='foundationDate']//input")
    foundation_amount = (By.XPATH, "//currency-input[@name='foundationAmount']//input")
    foundation_subject = (By.XPATH, "//text-area-input[@name='foundationSubject']//textarea")


# Сведения о денежном обязательстве добавление строк
class InformationAboutTheMonetaryObligationAddLineLocators(object):
    financial_year = (By.XPATH, "//div[@class='modal-content']//number-input[@name='financialYear']//input")
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='kbk']")
    kbk_type = (By.XPATH, "//div[@class='modal-content']//kbk-type-dropdown-input[@name='kbkType']//select")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    activity_kind = (
        By.XPATH, "//div[@class='modal-content']//*[@name='activityKind']//select")
    investment_program = (By.XPATH,
                          "//div[@class='modal-content']//*[@name='investmentProgram']")
    analytical_code = (By.XPATH, "//div[@class='modal-content']//text-input[@name='analyticalCode']//input")
    advance_transfered = (
        By.XPATH, "//div[@class='modal-content']//currency-input[@name='advanceTransfered']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='amount']//input")
    currency_amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='currencyAmount']//input")


# Сведения о денежном обязательстве - История изменений
class InformationAboutTheMonetaryObligationHistoryLocators(object):
    change_number = (By.XPATH, "//div[@class='modal-content']//text-input[@name='changeNumber']//input")
    change_date = (By.XPATH, "//div[@class='modal-content']//date-input[@name='changeDate']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")


# Заявка на возврат
class ReturnRequestLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    recepient = (By.XPATH, "//counterparty-classifier[@name='recepient']")
    ofk_registration_number = (By.XPATH, "//text-input[@name='ofkRegistrationNumber']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    recepient_account_details = (By.XPATH, "//*[@name='recepientAccountDetails']")
    document_kind = (By.XPATH, "//*[@name='documentKind']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    kbk_type = (By.XPATH, "//kbk-type-dropdown-input[@name='kbkType']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    amount = (By.XPATH, "//*[@name='amount']//input")
    nds_percent = (By.XPATH, "//nds-percent-input[@name='ndsPercent']//input")
    nds_amount = (By.XPATH, "//currency-input[@name='ndsAmount']//input")
    activity_kind = (By.XPATH, "//activity-kind-dropdown-input[@name='activityKind']//select")
    goal_code = (By.XPATH, "//text-input[@name='goalCode']//input")
    oktmo = (By.XPATH, "//oktmo-autocomplete[@name='oktmo']")
    department = (By.XPATH, "//department-classifier[@name='department']")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    expenditure_goal_act = (By.XPATH, "//expenditure-goal-act-classifier[@name='expenditureGoalAct']")
    document_foundation_kind = (By.XPATH, "//document-foundation-kind-autocomplete[@name='documentFoundationKind']")
    document_foundation_number = (By.XPATH, "//text-input[@name='documentFoundationNumber']//input")
    document_foundation_date = (By.XPATH, "//date-input[@name='documentFoundationDate']//input")
    recepient_kbk = (By.XPATH, "//recepient-kbk-autocomplete[@name='recepientKbk']")
    recepient_oktmo = (By.XPATH, "//oktmo-autocomplete[@name='recepientOktmo']")
    chief = (By.XPATH, "//*[@name='chief']")
    chief_accountant = (By.XPATH, "//*[@name='chiefAccountant']")
    priority_of_payment = (By.XPATH, "//*[@name='paymentPriority']//input")
    payment_purpose = (By.XPATH, "//text-area-input[@name='paymentPurpose']//textarea")
    payment_type = (By.XPATH, "//*[@name='paymentForm']//select")
    type_funds_for_return = (By.XPATH, "//*[@name='activityKind']//select")
    outstanding_payment_document_number = (By.XPATH, "//text-input[@name='outstandingPaymentDocumentNumber']//input")
    outstanding_payment_document_date = (By.XPATH, "//date-input[@name='outstandingPaymentDocumentDate']//input")
    outstanding_payment_document_amount = (
        By.XPATH, "//currency-input[@name='outstandingPaymentDocumentAmount']//input")
    outstanding_payment_document_inn = (By.XPATH, "//text-input[@name='outstandingPaymentDocumentInn']//input")
    outstanding_payment_document_kpp = (By.XPATH, "//text-input[@name='outstandingPaymentDocumentKpp']//input")


# Уведомления об уточнении вида и принадлежности платежа
class NotificationTypeAndPaymentTypeLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    activity_kind = (By.XPATH, "//activity-kind-dropdown-input[@name='activityKind']//select")
    budget_commitment_info_number = (By.XPATH, "//text-input[@name='budgetCommitmentInfoNumber']//input")
    notification_kind = (By.XPATH, "//notification-kind-dropdown-input[@name='notificationKind']//select")
    unit = (By.XPATH, "//department-classifier[@name='unit']")
    counterparty = (By.XPATH, "//counterparty-classifier[@name='counterparty']")
    counterparty_account_details = (
        By.XPATH, "//counterparty-account-details-classifier[@name='counterpartyAccountDetails']")
    federal_treasury_request_number = (By.XPATH, "//text-input[@name='federalTreasuryRequestNumber']//input")
    federal_treasury_request_date = (By.XPATH, "//date-input[@name='federalTreasuryRequestDate']//input")
    region = (By.XPATH, "//region-classifier[@name='region']")
    is_employee = (By.XPATH, "//check-input[@name='isEmployee']//input")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    passport = (By.XPATH, "//text-input[@name='passport']//input")
    chief = (By.XPATH, "//signatory-classifier[@name='chief']")
    contractor = (By.XPATH, "//employee-classifier[@name='contractor']")
    contractor_phone = (By.XPATH, "//text-input[@name='contractorPhone']//input")


# Уведомления об уточнении вида и принадлежности платежа - добавление уведомления
class NotificationTypeAndPaymentTypeNotificationLocators(object):
    order_number = (By.XPATH, "//div[@class='modal-content']//number-input[@name='orderNumber']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='amount']//input")
    operation = (By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='operation']")
    document_type = (
        By.XPATH, "//div[@class='modal-content']//*[@name='documentType']//select")
    document_number = (By.XPATH, "//div[@class='modal-content']//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//div[@class='modal-content']//date-input[@name='documentDate']//input")
    billing_document = (
        By.XPATH, "//div[@class='modal-content']//*[@name='billingDocument']")
    document_foundation = (
        By.XPATH, "//div[@class='modal-content']//*[@name='documentFoundation']")
    recepient = (By.XPATH, "//div[@class='modal-content']//counterparty-classifier[@name='recepient']")
    recepient_name = (By.XPATH, "//div[@class='modal-content']//text-input[@name='recepientName']//input")
    recepient_account_details = (
        By.XPATH, "//div[@class='modal-content']//*[@name='recepientAccountDetails']")
    inn = (By.XPATH, "//div[@class='modal-content']//text-input[@name='inn']//input")
    kpp = (By.XPATH, "//div[@class='modal-content']//text-input[@name='kpp']//input")
    oktmo = (By.XPATH, "//div[@class='modal-content']//text-input[@name='oktmo']//input")
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='Kbk']")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//cost-elements-classifier[@name='costElement']")
    statement_analysis_code = (
        By.XPATH, "//div[@class='modal-content']//statement-analysis-code-classifier[@name='statementAnalysisCode']")
    purpose_code = (By.XPATH, "//div[@class='modal-content']//text-input[@name='purposeCode']//input")
    purpose_payment = (By.XPATH, "//div[@class='modal-content']//text-input[@name='purposePayment']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")


# Уведомления об уточнении вида и принадлежности платежа - добавление уведомления + Изменение реквизитов
class NotificationTypeAndPaymentTypeImageLocators(object):
    amount = (By.XPATH, "(//div[@class='modal-content']//currency-input[@name='amount']//input)[2]")
    recepient = (By.XPATH, "(//div[@class='modal-content']//counterparty-classifier[@name='recepient'])[2]")
    recepient_account_details = (By.XPATH, "(//div[@class='modal-content']//*[@name='recepientAccountDetails'])[2]")
    inn = (By.XPATH, "(//div[@class='modal-content']//text-input[@name='inn']//input)[2]")
    kpp = (By.XPATH, "(//div[@class='modal-content']//text-input[@name='kpp']//input)[2]")
    oktmo = (By.XPATH, "(//div[@class='modal-content']//text-input[@name='oktmo']//input)[2]")
    recepient_personal_account = (
        By.XPATH, "(//div[@class='modal-content']//text-input[@name='recepientPersonalAccount']//input)[2]")
    is_taxes = (By.XPATH, "(//div[@class='modal-content']//check-input[@name='isTaxes']//input)[2]")
    kbk = (By.XPATH, "(//div[@class='modal-content']//kbk-classifier[@name='Kbk']")
    kosgu = (By.XPATH, "(//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "(//div[@class='modal-content']//cost-elements-classifier[@name='costElement'])[2]")
    recepient_kbk = (By.XPATH, "(//div[@class='modal-content']//recepient-kbk-autocomplete[@name='recepientKbk'])[2]")
    activity_kind = (
        By.XPATH, "(//div[@class='modal-content']//activity-kind-dropdown-input[@name='activityKind']//select)[2]")
    purpose_code = (By.XPATH, "(//div[@class='modal-content']//text-input[@name='purposeCode']//input)[2]")
    statement_analysis_code = (
        By.XPATH, "(//div[@class='modal-content']//*[@name='statementAnalysisCode'])[2]")
    purpose_payment = (By.XPATH, "(//div[@class='modal-content']//text-input[@name='purposePayment']//input)[2]")


# Заявка на получение наличных денег
class ApplicationForCashWithdrawalLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    deadline = (By.XPATH, "//date-input[@name='deadline']//input")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    operation_master = (By.XPATH, "//operation-master-hierarchy-classifier[@name='OperationMaster']")
    trustee = (By.XPATH, "//employee-classifier[@name='Trustee']")
    trustee_position_dative_case = (By.XPATH, "//*[@name='trusteePositionDativeCase']//input")
    trustee_name_dative_case = (By.XPATH, "//text-input[@name='trusteeNameDativeCase']//input")
    trustee_position = (By.XPATH, "//position-classifier[@name='TrusteePosition']")
    chief = (By.XPATH, "//signatory-classifier[@name='Chief']")
    accountant_general = (By.XPATH, "//*[@name='AccountantGeneral']")
    foundation = (By.XPATH, "//text-area-input[@name='foundation']//textarea")
    check_series = (By.XPATH, "//text-input[@name='checkSeries']//input")
    check_number = (By.XPATH, "//number-input[@name='checkNumber']//input")
    check_date = (By.XPATH, "//date-input[@name='checkDate']//input")
    check_valid_till = (By.XPATH, "//date-input[@name='checkValidTill']//input")


# Заявка на получение наличных денег добавление строк
class ApplicationForCashWithdrawalAddLineLocators(object):
    operation_master = (
        By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='OperationMaster']")
    kbk_type = (By.XPATH, "//div[@class='modal-content']//kbk-type-dropdown-input[@name='kbkType']//select")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    department_unit = (By.XPATH, "//div[@class='modal-content']//department-unit-classifier[@name='departmentUnit']")
    act = (By.XPATH, "//div[@class='modal-content']//expenditure-goal-act-classifier[@name='act']")
    code_goal = (By.XPATH, "//div[@class='modal-content']//text-input[@name='codeGoal']//input")
    cash_transaction_code = (By.XPATH, "//*[@name='CashTransactionCode']//select")
    funds_source = (By.XPATH, "//*[@name='fundsSource']//select")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    payment_purpose = (By.XPATH, "//text-area-input[@name='paymentPurpose']//textarea")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# Заявка на получение денежных средств, перечисляемых на карту
class ApplyingForCardLocators(object):
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    operation_master = (By.XPATH, "//operation-master-hierarchy-classifier[@name='OperationMaster']")
    account_details = (By.XPATH, "//current-organization-account-details-classifier[@name='accountDetails']")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    activity_kind = (By.XPATH, "//activity-kind-dropdown-input[@name='activityKind']//select")
    card_number = (By.XPATH, "//card-number-input[@name='cardNumber']//input")
    trustee = (By.XPATH, "//employee-classifier[@name='Trustee']")
    employee_position = (By.XPATH, "//position-classifier[@name='employeePosition']")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    employee_name_in_ablative_case = (By.XPATH, "//text-input[@name='employeeNameInAblativeCase']//input")
    employee_position_in_ablative_case = (By.XPATH, "//text-input[@name='employeePositionInAblativeCase']//input")
    foundation = (By.XPATH, "//text-input[@name='foundation']//input")
    chief = (By.XPATH, "//signatory-classifier[@name='Chief']")
    accountant_general = (By.XPATH, "//signatory-classifier[@name='AccountantGeneral']")


# Заявка на получение денежных средств, перечисляемых на карту добавление строк
class ApplyingForCardAddLineLocators(object):
    operation_master = (
        By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='OperationMaster']")
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='kbk']")
    kbk_type = (By.XPATH, "//div[@class='modal-content']//kbk-type-dropdown-input[@name='kbkType']//select")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//cost-elements-classifier[@name='costElement']")
    amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='amount']//input")
    goal_code = (By.XPATH, "//div[@class='modal-content']//text-input[@name='goalCode']//input")
    department_unit = (By.XPATH, "//div[@class='modal-content']//department-unit-classifier[@name='departmentUnit']")
    act = (By.XPATH, "//div[@class='modal-content']//expenditure-goal-act-classifier[@name='act']")
    payment_purpose = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='paymentPurpose']//textarea")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")


# Расшифровка сумм неиспользованных средств
class DecodingAmountsUnusedFundsLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    card_number = (By.XPATH, "//card-number-input[@name='cardNumber']//input")
    operation_type = (By.XPATH, "//operation-type-dropdown-input[@name='operationType']//select")
    personal_account = (By.XPATH, "//current-organization-account-details-classifier[@name='personalAccount']")
    operation_master = (By.XPATH, "//operation-master-hierarchy-classifier[@name='OperationMaster']")
    tracking_number = (By.XPATH, "//text-input[@name='trackingNumber']//input")
    investment_program = (By.XPATH, "//federal-targeted-investment-program-classifier[@name='investmentProgram']")
    chief = (By.XPATH, "//signatory-classifier[@name='chief']")
    accountant_general = (By.XPATH, "//signatory-classifier[@name='accountantGeneral']")


# Расшифровка сумм неиспользованных средств добавление строки
class DecodingAmountsUnusedFundsAddLineLocators(object):
    operation_master = (
        By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='OperationMaster']")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//cost-elements-classifier[@name='costElement']")
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='kbk']")
    kbk_type = (By.XPATH, "//div[@class='modal-content']//kbk-type-dropdown-input[@name='kbkType']//select")
    activity_kind = (
        By.XPATH, "//div[@class='modal-content']//activity-kind-dropdown-input[@name='activityKind']//select")
    amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='amount']//input")
    goal_code = (By.XPATH, "//div[@class='modal-content']//text-input[@name='goalCode']//input")
    department_unit = (By.XPATH, "//div[@class='modal-content']//department-unit-classifier[@name='departmentUnit']")
    act = (By.XPATH, "//div[@class='modal-content']//expenditure-goal-act-classifier[@name='act']")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")


#  Расходный кассовый ордер
class AccountCashWarrantLocators(object):
    document_kind = (By.XPATH, "//*[@name='documentKind']")
    document_number = (By.XPATH, "//*[@name='documentNumber']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    document_date = (By.XPATH, "//*[@name='documentDate']//input")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    operation_master = (By.XPATH, "//operation-master-hierarchy-classifier[@name='OperationMaster']")
    employee = (By.XPATH, "//*[@name='employee']")
    issue = (By.XPATH, "//*[@name='issue']//input")
    foundation = (By.XPATH, "//*[@name='foundation']//textarea")
    cash_report_number = (By.XPATH, "//*[@name='cashReportNumber']//input")


#  Расходный кассовый ордер+заполнение строк
class AccountCashWarrantLocatorsAddLine(object):
    operation = (By.XPATH, "//*[@name='operation']")
    kbk = (By.XPATH, "//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//*[@name='costElement']")
    department_unit = (By.XPATH, "//div[@class='modal-content']//department-unit-classifier[@name='departmentUnit']")
    sender = (By.XPATH, "//div[@class='modal-content']//materially-responsible-person-classifier[@name='sender']")
    material_inventory = (
        By.XPATH, "//div[@class='modal-content']//material-inventory-classifier[@name='materialInventory']")
    quantity = (By.XPATH, "//div[@class='modal-content']//decimal-input[@name='quantity']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//*[@name='comment']//textarea")
    act = (By.XPATH, "//div[@class='modal-content']//expenditure-goal-act-classifier[@name='act']")


# Расходный кассовый ордер приложение
class AccountCashWarrantPagePlusLocators(object):
    document_foundation = (By.XPATH, "//imprest-foundation-classifier[@name='documentFoundation']")
    advance_report = (By.XPATH, "//advance-report-classifier[@name='advanceReport']")
    supplement = (By.XPATH, "//text-input[@name='supplement']//input")
    accountant = (By.XPATH, "//signatory-classifier[@name='accountant']")
    chief = (By.XPATH, "//signatory-classifier[@name='chief']")
    cashier = (By.XPATH, "//signatory-classifier[@name='cashier']")


# Журнал проводок
class PostingJournalLocators(object):
    date_from = (By.XPATH, "//input[@id='date1']")
    date_by = (By.XPATH, "//input[@id='date2']")
    balance_sheet_account = (By.XPATH, "//*[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH, "//*[@name='balanceSheetAccountGroup']")


#  Основание для выдачи подотчетных сумм
class BasisForReportingAmountsLocators(object):
    number = (By.XPATH, "//*[@name='documentNumber']//input")
    document_date = (By.XPATH, "//*[@name='documentDate']//input")
    document_kind = (By.XPATH, "//*[@name='documentKind']")
    employee = (By.XPATH, "//*[@name='employee']")
    position = (By.XPATH, "//*[@name='position']")
    department = (By.XPATH, "//*[@name='department']")
    trip_start_date = (By.XPATH, "//*[@name='tripStartDate']//input")
    trip_end_date = (By.XPATH, "//*[@name='tripEndDate']//input")
    comment = (By.XPATH, "//*[@name='comment']//textarea")
    trip_route = (By.XPATH, "//*[@name='tripRoute']//textarea")


#  Основание для выдачи подотчетных сумм добавление строки
class BasisForReportingAmountsAddLineLocators(object):
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    employee = (By.XPATH, "//div[@class='modal-content']//*[@name='employee']")
    position = (By.XPATH, "//div[@class='modal-content']//*[@name='position']")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//*[@name='comment']//textarea")


# авансовый отчет
class AvansReportLocators(object):
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    entry_date = (By.XPATH, "date-input[@name='entryDate']//input")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    position = (By.XPATH, "//position-classifier[@name='position']")
    department = (By.XPATH, "//position-classifier[@name='department']")
    employee_full_name = (By.XPATH, "//text-input[@name='employeeFullName']//input")
    document_foundation = (By.XPATH, "//imprest-foundation-classifier[@name='documentFoundation']")
    purpose = (By.XPATH, "//text-area-input[@name='purpose']//textarea")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# авансовый отчет добавление строки
class AvansReportAddLineLocators(object):
    operation_master = (
        By.XPATH, "//div[@class='modal-content']//operation-master-hierarchy-classifier[@name='OperationMaster']")
    kbk = (By.XPATH, "//div[@class='modal-content']//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//div[@class='modal-content']//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//div[@class='modal-content']//cost-elements-classifier[@name='costElement']")
    document_date = (By.XPATH, "//div[@class='modal-content']//date-input[@name='documentDate']//input")
    document_number = (By.XPATH, "//div[@class='modal-content']//number-input[@name='documentNumber']//input")
    amount = (By.XPATH, "//div[@class='modal-content']//currency-input[@name='amount']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//text-area-input[@name='comment']//textarea")