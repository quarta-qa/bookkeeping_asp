from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='UserName']")
    password = (By.XPATH, "//input[@id='Password']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):
    pass


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
        drawee_kbk_type = (By.XPATH, "//select[@name='draweeKbkType']")
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
    document_number = (By.XPATH, "//input[@id='documentNumber']")
    document_date = (By.XPATH, "//input[@id='date1']")
    personal_account = (By.XPATH, "(//button[@title='Выбрать'])[1]")
    recipient_name = (By.XPATH, "(//button[@title='Выбрать'])[2]")
    ofk_registration_number = (By.XPATH, "//input[@id='ofkRegistrationNumber']")
    entry_date = (By.XPATH, "//input[@id='date1']")
    typical_operation = (By.XPATH, "(//button[@title='Выбрать'])[3]")
    recipient_account = (By.XPATH, "(//button[@title='Выбрать'])[4]")
    document_type = (By.XPATH, "(//button[@title='Выбрать'])[5]")

    class Request(object):
        #Закладка Расшифровка заявки
        summa_rub = (By.XPATH, "//input[@id='outstandingPaymentDocumentAmount']")
        oktmo = (By.XPATH, "(//button[@title='Выбрать'])[10]")

    class Doc(object):
        #Закладка Документы по зачислению невыясненного платежа
        number = (By.XPATH, "//input[@id='outstandingPaymentDocumentNumber']")

