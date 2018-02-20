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
        page.username("Test666")
        page.password("warrior1358")
        page.submit()
        page.wait.text_appear("Документы — Бухгалтерский учет")


    def test_adding_entries_to_the_directory_of_fixed_assets(self):
        page = MenuPage(self.driver)
        page.select_month("Сентябрь", "2018")
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Машины и оборудование") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Машины и оборудование") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        page.click_by_text("Добавить")

        # Создание ОС Жилое здание, Малая Никитская, д.2

        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_first_part("10112")
        page.tag_no_second_part("1")
        page.tag_no("1011200001")
        page.full_name("Жилое здание, Малая Никитская, д.2")
        page.property_designation("Административное здание")
        page.start_up_date("05.09.2018")
        page.unit_of_measure("Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.cost("1430000.00")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.value_added_used("1200")
        page.amortization_group("10 ГРУППА")
        page.okof("Здания производственные административные")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        #page.click_by_text("Да")
        sleep(1)

        # Создание ОС "Ноутбук Toshiba"

        page.click_by_text("Добавить")
        page.tag_no_first_part("10134")
        page.tag_no_second_part("1")
        page.tag_no("1013400001")
        page.full_name("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.start_up_date("01.09.2018")
        page.serial_number("JKN87628764")
        page.unit_of_measure("Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.cost("36500.00")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.value_added_used("36")
        page.okof("ЭВМ общего назначения")
        page.amortization_group(" 2 ГРУППА")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        sleep(1)
        
        # Создание ОС "Копировальный аппарат"

        page.click_by_text("Добавить")
        page.set_text_wl("tagNoFirstPart", "10134", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "2", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013400002", ">>>")
        page.set_text_wl("fullName", "Копировальный аппарат Xerox Phaser 8200", "Полное наименование")
        page.set_date_wl("startUpDate", "16.09.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "GH57654898672FGD", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "18000.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "120", "Срок полезного использования (месяцев)")
        page.set_select2_wl("okof","Оборудование фоторепродукционное,копировальное и для обработки фотоматериалов", 
        "ОКОФ")
        page.set_select2_wl ("amortizationGroup", " 5 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        sleep(1)
    
        # Создание ОС "Автомобиль"

        page.click_by_text("Добавить")
        page.set_text_wl("tagNoFirstPart", "10135", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "1", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013500001", ">>>")
        page.set_text_wl("fullName", "Автомобиль Volswagen passat 2.0 TFSI", "Полное наименование")
        page.set_text_wl("propertyDesignation", "ООО Германика", "Поставщик")
        page.set_date_wl("issueDate", "23.06.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "15.09.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "BNV876876JH093S", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "1256000.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "60", "Срок полезного использования (месяцев)")
        page.set_select2_wl("okof",
         "Автомобили легковые среднего класса (срабочим объемом двигателя свыше 1,8 до 3,5 лвключительно)", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 3 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        sleep(1)
        
    def test_creation_of_a_materially_responsible_person(self):
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Материально ответственные лица')
        page.click_by_text('Добавить')
        page.set_select2_wl("employee", "Абдуллина З.Ш.", "Ссылка на сотрудника")
        sleep(2)
        # Выпадающего поля  "Категория МОЛ" нет на портале, в сценарии оно есть
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(5)
        
    def test_creation_of_document_coming_TMC_and_OS(self):
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Январь", "2018")
        page.click_by_text('Поступление НФА')
        # page.click_by_text("Добавить - Новый документ") на портале нет суб-кнопки, в сценарии есть
        page.click_by_text("Добавить")
        page = Browser(self.driver)
        # Информация о документе
        page.set_text_wl("documentNumber", "Нач.ост.", "Номер")
        page.set_select2_wl("documentKind", "Приёмный акт", "Приёмный акт")
        page.set_date_wl("documentDate","01.01.2018","Дата")
        page.set_date_wl("entryDate","01.01.2018","Дата проводки")
        page.set_text_wl("comment", "Начальные остатки ОС", "Комментарий")
        # Реквизиты документа
        page.set_select2_wl("materiallyResponsiblePerson", "Абдуллина З.Ш.", "МОЛ")
        page.set_select_wl("senderSenderType","Организация","Вид отправителя")
        page.set_select2_wl("organization", 'ООО "КВАРТА ВК"',"МОЛ")
        # Создать строку "ОС,НМА"
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page.set_select2_wl("operation", "Приход ОС", "Типовая операция")
        page.set_text_wl("tagNo", "1011200001", "Инвентарный №")
        sleep(3)
        # Нет зависимости "Наименования" и "Инвентарного номера" (дописать тест стр. 13-16 после испр. ошибки)
        # Также не работает контексный поиск в справочнике "Картотека ОС, НМА, НПА"
        # ...
        page.click_by_text("Сохранить", 2)
        sleep(2)
        page.click_by_text("Закрыть",2)
        page.click_by_text("Сохранить",1)
        page.click_by_text("Закрыть",1)
        
    def test_add_another_entry_to_the_asset_catalog(self):
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Сентябрь", "2018")
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page.set_text_wl("tagNoFirstPart", "10134", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "3", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013400003", ">>>")
        page.set_text_wl("fullName", "Систмный блок", "Полное наименование")
        page.set_text_wl("propertyDesignation", "ООО 'ОЛДИ'", "Поставщик")
        page.set_date_wl("issueDate", "01.09.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "01.09.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "JO4445566", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.set_select2_wl("group","С/блоки","Группа ОС, НМА, НПА")
        page.scroll_to_bottom()
        page.set_text_wl("cost", "25300.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "60", "Срок полезного использования (месяцев)")
        page.set_select2_wl("okof", "Машины вычислительные электронные цифровые", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 3 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # Нет суб-кнопки "Действие - Создать папку" по сценарию ее надо добавить
        # page.click_by_text("Сохранить")

    def test_create_a_new_asset_record_using_the_card_template(self):
        # Создание Шаблона карточки ОС, НМА, НПА
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Сентябрь", "2018")
        page.references()
        page.click_by_text('Шаблоны карточки ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page.set_text_wl("name", "Шкаф для документации", "Наименование объекта")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(3)
        # По сценарию нужно добавить папку "ХОЗ. ИНВЕНТАРЬ" в справочнике "Объекты ОС, НМА, НПА" но на портале нет функционал добавить папку
        page.set_select2_wl("group", "Мебель", "Группа ОС, НМА, НПА")
        page.set_select2_wl("okof", "Шкафы для документации", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 4 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить", 2)
        page.click_by_text("Закрыть", 2)
        # Создание новой записи основного средства с использованием созданного шаблона карточки ОС, НМА, НПА
        # На портале не работает автозополнение полей при выборе шаблона карточки
        # page.references()
        # page.click_by_text('Объекты ОС, НМА, НПА')
        # page.click_by_text("Добавить")
        # page.set_text_wl("tagNoFirstPart", "10106", "Первая часть инвентарного номера")
        # page.set_text_wl("tagNoSecondPart", "1", "Вторая часть инвентарного номера")
        # page.set_select2_wl("template", "Шкаф для документации", "Шаблон карточки")

    def test_copy_entries_to_the_directory_of_fixed_assets(self):
        # Копирование записи ОС
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page.click_by_text('Копию строки')
        # Данной суб-кнопки нет на портале, по сценарию она должна быть
    
    def test_editing_copy_entries_to_the_directory_of_fixed_assets(self):
        # Редактирование записи ОС
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        # Поиск строки по 'text' в локаторе
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.click_by_text('Открыть')
        page.set_text_wl("tagNoSecondPart", "2", "Вторая часть инвентарного номера")
        page.set_text_wl("serialNumber", "JO4445567", "Серийный №")
        sleep(3)
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        
    def test_deletion_of_a_record_in_the_fixed_assets_directory(self):
        # Удаление записи ОС
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        # Поиск строки по 'text' в локаторе
        page.table_select_row("Жилое здание, Малая Никитская, д.2")
        page.click_by_text('Удалить')
        sleep(5)
        page.click_by_text('Да')
        page.click_by_text('Закрыть')
        sleep(5)
    # def test_print_inventory_card_OKUD0504031(self):
        # Печать инвентарной карточки учета ОКУД 504031/функция печати недописана

    # def test_printing_of_a_group_inventory_cardOKUD0504032(self):
        # Печать инвентарной карточки учета ОКУД 504032/функция печати недописана

    def test_Checking_the_mode_Mass_filling_of_OS_parameters(self):
        # Проверка режима «Массовое заполнение параметров ОС»
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.table_select_row("Жилое здание, Малая Никитская, д.2")
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.table_select_row("Копировальный аппарат Xerox Phaser 8200")
        page.table_select_row("Автомобиль Volswagen passat 2.0 TFSI")
        page.click_by_text("Действия")
        page.click_by_text('Массовое заполнение параметров объектов')
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        page.set_text_wl("propertyDesignation", "Массовое заполнение 3-х полей", "Назначение объекта")
        page.set_date_wl("startUpDate", "25.02.2018", "Дата ввода в эксплуатацию")
        page.set_date_wl("issueDate", "02.03.2018", "Дата выпуска")
        page.click_by_text('Выполнить')
        page.click_by_text('Закрыть')
