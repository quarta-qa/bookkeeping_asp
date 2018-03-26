from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='UserName']")
    password = (By.XPATH, "//input[@id='Password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):
    menu = (By.XPATH, "//button[contains(@class,'left-menu-toggle')]")
    # menu_close = (By.XPATH, "//button[@class='left-menu-toggle active']")


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
    references = (By.XPATH, "//a[contains(.,'Справочники')]")
    report = (By.XPATH, "//a[contains(.,'Отчет')]")
    turnover_statement = (By.XPATH, "//a[contains(.,'Оборотная ведомость')]")
    summary_reporting = (By.XPATH, "//a[contains(.,'Сводная отчетность')]")
    printed_forms = (By.XPATH, "//a[contains(.,'Печатные формы')]")
    remains_NFA = (By.XPATH, "//*[@href='#/report/non-financial-assets/balances-gathering']")
    salary = (By.XPATH, "(//a[contains(.,'АИС «Зарплата.NET»')]")
    document_journal = (By.XPATH, "//a[contains(.,'Журнал документов')]")
    recycle_bin = (By.XPATH, "//a[contains(.,'Корзина документов ')]")


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


#   ПКО
class IncomingOrderLocators(object):
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    organization = (By.XPATH, "//counterparty-classifier[@name='organization']")
    received_from = (By.XPATH, "//text-input[@name='receivedFrom']//input")
    department_unit = (By.XPATH, "//department-unit-classifier[@name='departmentUnit']")
    cash_report_number = (By.XPATH, "//text-input[@name='cashReportNumber']//input")
    foundation = (By.XPATH, "//text-area-input[@name='foundation']//textarea")
    operation = (By.XPATH, "//*[@name='operation']")


# Добавление  строки в ПКО
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
    date_begin = (By.XPATH, "//*[@name='startDate']//input")
    date_end = (By.XPATH, "//*[@name='endDate']//input")
    payment_type = (By.XPATH, "//*[@name='considerationPeriod']//select")
    subject_contract = (By.XPATH, "//*[@name='subject']//textarea")
    payment_terms = (By.XPATH, "//*[@name='paymentTerm']//textarea")
    note = (By.XPATH, "//*[@name='comment']//textarea")


class ContractWithSupplierDetailKBKPageLocators(object):
    financial_year = (By.XPATH, "//*[@name='financialYear']//input")
    entry_date = (By.XPATH, "//*[@name='entryDate']//input")
    operation = (By.XPATH, "//*[@name='operation']")
    kbk = (By.XPATH, "//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    contract_subject = (By.XPATH, "//*[@name='contractSubject']//textarea")
    amounts_amount = (By.XPATH, "//*[@name='amountsAmount']//input")
    amounts_nds_percent = (By.XPATH, "//*[@name='amountsNdsPercent']//input")
    advance = (By.XPATH, "//*[@name='advance']//input")
    cost_Element = (By.XPATH, "//*[@name='costElement']")


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
    date = (By.XPATH, "//date-input[@name='date']//input")
    balance_sheet_account = (By.XPATH, "//balance-sheet-account-classifier[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH, "//balance-sheet-account-group-classifier[@name='balanceSheetAccountGroup']")
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
    personal_account = (By.XPATH, "//*[@name='accountDetails']")
    bank_account_number = (By.XPATH, "//*[@name='counterpartyAccountDetails']")
    recipient = (By.XPATH, "//*[@name='counterparty']")
    number_ufk = (By.XPATH, "//*[@name='ofkNumber']//input")
    limit_date = (By.XPATH, "//*[@name='limitDate']//input")
    foundation = (By.XPATH, "//div[@class='tab-content']//*[@name='foundation']")
    operation = (By.XPATH, "//*[@name='operation']")


class DecodingOfTheApplicationLocators(object):
    operation = (By.XPATH, "//div[@class='modal-content']//*[@name='operation']")
    kbk = (By.XPATH, "//div[@class='modal-content']//*[@name='kbk']")
    kosgu = (By.XPATH, "//*[@name='kosgu']")
    cost_element = (By.XPATH, "//*[@name='costElement']")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    nds_percent = (By.XPATH, "//*[@name='ndsPercent']//input")
    document_foundation_counterparty = (By.XPATH, "//*[@name='documentFoundationCounterparty']")
    foundation = (By.XPATH, "//div[@class='modal-content']//*[@name='foundation']")
    comment = (By.XPATH, "//*[@name='comment']//textarea")
    draweeKbkType = (By.XPATH, "//*[@name='drawee_kbk_type']//select")


class InvoiceFromTheSupplierLocators(object):
    document_number = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    supplier = (By.XPATH, "//counterparty-classifier[@name='supplier']")
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
    comment = (By.XPATH, "//div[@class='modal in']//*[@name='comment']//textarea")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    vat_percent = (By.XPATH, "//nds-percent-input[@name='vatPercent']//input")


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
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    kbk_type = (By.XPATH, "//kbk-type-dropdown-input[@name='kbkType']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    outstanding_payment_document_amount = (By.XPATH, "//*[@name='outstandingPaymentDocumentAmount']//input")
    nds_percent = (By.XPATH, "//nds-percent-input[@name='ndsPercent']//input")
    nds_amount = (By.XPATH, "//currency-input[@name='ndsAmount']//input")
    chief = (By.XPATH, "//*[@name='chief']")
    chief_accountant = (By.XPATH, "//*[@name='chiefAccountant']")


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
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    cash_transaction_code = (By.XPATH, "//*[@name='CashTransactionCode']//select")
    funds_source = (By.XPATH, "//*[@name='fundsSource']//select")
    amount = (By.XPATH, "//div[@class='modal-content']//*[@name='amount']//input")
    payment_purpose = (By.XPATH, "//text-area-input[@name='paymentPurpose']//textarea")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# рко
class AccountCashWarrantLocators(object):
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    document_number = (By.XPATH, "//text-input[@name='documentNumber']//input")
    entry_date = (By.XPATH, "//date-input[@name='entryDate']//input")
    document_date = (By.XPATH, "//*[@name='documentDate']//input")
    employee = (By.XPATH, "//*[@name='employee']")
    issue = (By.XPATH, "//text-input[@name='issue']//input")
    foundation = (By.XPATH, "//text-area-input[@name='foundation']//textarea")
    cash_report_number = (By.XPATH, "//text-input[@name='cashReportNumber']//input")


# рко+заполнение строк
class AccountCashWarrantLocatorsAddLine(object):
    operation = (By.XPATH, "//operation-master-hierarchy-classifier[@name='operation']")
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    amount = (By.XPATH, "//amount-input[@name='amount']//input")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")


# Журнал проводок
class PostingJournalLocators(object):
    date_from = (By.XPATH, "//input[@id='date1']")
    date_by = (By.XPATH, "//input[@id='date2']")
    balance_sheet_account = (By.XPATH, "//*[@name='balanceSheetAccount']")
    balance_sheet_account_group = (By.XPATH, "//*[@name='balanceSheetAccountGroup']")


#  Основание для выдачи подотчетных сумм
class BasisForReportingAmountsLocators(object):
    number  = (By.XPATH, "//number-input[@name='documentNumber']//input")
    document_date = (By.XPATH, "//date-input[@name='documentDate']//input")
    document_kind = (By.XPATH, "//document-kind-classifier[@name='documentKind']")
    employee = (By.XPATH, "//employee-classifier[@name='employee']")
    position = (By.XPATH, "//position-classifier[@name='position']")
    department = (By.XPATH, "//department-classifier[@name='department']")
    trip_start_date = (By.XPATH, "//date-input[@name='tripStartDate']//input")
    trip_end_date = (By.XPATH, "//date-input[@name='tripEndDate']//input")
    comment = (By.XPATH, "//text-area-input[@name='comment']//textarea")
    trip_route = (By.XPATH, "//text-area-input[@name='tripRoute']//textarea")


#  Основание для выдачи подотчетных сумм добавление строки
class BasisForReportingAmountsAddLineLocators(object):
    kbk = (By.XPATH, "//kbk-classifier[@name='kbk']")
    kosgu = (By.XPATH, "//kosgu-classifier[@name='kosgu']")
    cost_element = (By.XPATH, "//cost-elements-classifier[@name='costElement']")
    employee = (By.XPATH, "//div[@class='modal-content']//*[@name='employee']")
    amount = (By.XPATH, "//currency-input[@name='amount']//input")
    comment = (By.XPATH, "//div[@class='modal-content']//*[@name='comment']//textarea")



