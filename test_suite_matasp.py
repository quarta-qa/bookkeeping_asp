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
        page.select_month("Февраль", "2018")
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
        page.start_up_date("05.02.2018")
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
        # page.click_by_text("Да")
        sleep(1)

        # Создание ОС "Ноутбук Toshiba"

        page.click_by_text("Добавить")
        page.tag_no_first_part("10134")
        page.tag_no_second_part("1")
        page.tag_no("1013400001")
        page.full_name("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.start_up_date("01.02.2018")
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
        page.set_date_wl("startUpDate", "16.02.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "GH57654898672FGD", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "18000.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "120", "Срок полезного использования (месяцев)")
        page.set_select2_wl("okof", "Оборудование фоторепродукционное,"
                                    "копировальное и для обработки фотоматериалов", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 5 ГРУППА", "Амортизационная группа")
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
        page.set_date_wl("issueDate", "23.02.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "15.03.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "BNV876876JH093S", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "1256000.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "60", "Срок полезного использования (месяцев)")
        page.set_select2_wl("okof", "Автомобили легковые среднего класса "
                                    "(срабочим объемом двигателя свыше 1,8 до 3,5 лвключительно)", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 3 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        sleep(1)

    def test_creation_of_a_materially_responsible_person(self):
        # Создание материально-ответственного лица
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Материально ответственные лица')
        page.click_by_text('Добавить')
        page.set_select2_wl("employee", "Абдуллина З.Ш.", "Ссылка на сотрудника")
        # Выпадающего поля  "Категория МОЛ" нет на портале, в сценарии оно есть
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    def test_creation_of_document_coming_TMC_and_OS(self):
        # Создание поступление НФА и прикрепление созданных 4 ОС
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Февраль", "2018")
        page.click_by_text('Поступление НФА')
        # page.click_by_text("Добавить - Новый документ") на портале нет суб-кнопки, в сценарии есть
        page.click_by_text("Добавить")
        # Информация о документе
        page.set_text_wl("documentNumber", "Нач.ост.", "Номер")
        page.set_select2_wl("documentKind", "Приёмный акт", "Приёмный акт")
        page.set_date_wl("documentDate", "01.02.2018", "Дата")
        page.set_date_wl("entryDate", "01.02.2018", "Дата проводки")
        # Реквизиты документа
        page.set_select2_wl("materiallyResponsiblePerson", "Абдуллина З.Ш.", "МОЛ")
        page.set_select_wl("senderSenderType", "Организация", "Вид отправителя", order=2)
        page.set_select2_wl("organization", 'ООО "КВАРТА ВК"', "Наименование отправителя")
        page.set_text_wl("comment", "Начальные остатки ОС", "Комментарий")
        # Создать строку "ОС,НМА"
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page.set_select2_wl("operation", "Приход ОС", "Типовая операция")
        page.set_text_wl("tagNo", "1011200001", "Инвентарный №")
        # Нет зависимости "Наименования" и "Инвентарного номера" (дописать тест стр. 13-16 после испр. ошибки)
        # Также не работает контексный поиск в справочнике "Картотека ОС, НМА, НПА"
        # ...
        page.click_by_text("Сохранить", order=2)
        page.click_by_text("Закрыть", order=2)
        page.click_by_text("Сохранить", order=1)
        page.click_by_text("Закрыть", order=1)

    def test_add_another_entry_to_the_asset_catalog(self):
        # Добавление в справочник ОС еще одной записи и помещение ее в папку
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page.set_text_wl("tagNoFirstPart", "10134", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "3", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013400003", ">>>")
        page.set_text_wl("fullName", "Систмный блок", "Полное наименование")
        page.set_text_wl("propertyDesignation", "ООО 'ОЛДИ'", "Поставщик")
        page.set_date_wl("issueDate", "01.02.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "01.02.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "JO4445566", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.set_select2_wl("group", "С/блоки", "Группа ОС, НМА, НПА")
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
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Шаблоны карточки ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page.set_text_wl("name", "Шкаф для документации", "Наименование объекта")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(3)
        # По сценарию нужно добавить папку "ХОЗ. ИНВЕНТАРЬ" в справочнике "Объекты ОС, НМА, НПА",
        # но на портале нет функционала - добавить папку в справочнике "Объекты ОС,НМА,НПА"
        page.set_select2_wl("group", "Мебель", "Группа ОС, НМА, НПА")
        page.set_select2_wl("okof", "Шкафы для документации", "ОКОФ")
        page.set_select2_wl("amortizationGroup", " 4 ГРУППА", "Амортизационная группа")
        page.click_by_text("Сохранить", order=2)
        page.click_by_text("Закрыть", order=2)
        # Создание новой записи основного средства с использованием созданного шаблона карточки ОС, НМА, НПА
        # На портале не работает автозополнение полей при выборе шаблона карточки
        # page.references()
        # page.click_by_text('Объекты ОС, НМА, НПА')
        # page.click_by_text("Добавить")
        # page.set_text_wl("tagNoFirstPart", "10106", "Первая часть инвентарного номера")
        # page.set_text_wl("tagNoSecondPart", "1", "Вторая часть инвентарного номера")
        # page.set_select2_wl("template", "Шкаф для документации", "Шаблон карточки")

    # def test_copy_entries_to_the_directory_of_fixed_assets(self):
    #     # Копирование записи ОС
    #     page.references()
    #     page.click_by_text('Объекты ОС, НМА, НПА')
    #     page.click_by_text('Добавить')
    #     page.click_by_text('Копию строки')
    #     # Данной суб-кнопки нет на портале, по сценарию она должна быть

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
        page = Browser(self.driver)
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
        
    def test_checking_the_mode_Mass_filling_of_OS_parameters(self):
        # Проверка режима «Массовое заполнение параметров ОС»
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.table_select_row("Копировальный аппарат Xerox Phaser 8200")
        page.table_select_row("Автомобиль Volswagen passat 2.0 TFSI")
        page.click_by_text("Действия")
        page.click_by_text('Массовое заполнение параметров объектов')
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        page.set_text_wl("propertyDesignation", "Массовое заполнение 3-х полей", "Назначение объекта")
        page.set_date_wl("startUpDate", "25.02.2018", "Дата ввода в эксплуатацию")
        page.set_date_wl("issueDate", "02.02.2018", "Дата выпуска")
        page.click_by_text('Выполнить')
        page.click_by_text('Закрыть')
        
    def test_creat_a_new_folder_in_the_directory_Objects_OZ(self):
        # Создание новой папки в справочнике «Объекты ОЗ»
        page = MenuPage(self.driver)
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Объекты МЗ')
        page.click_by_text("Добавить")
        page.click_by_text("Новую папку")
        page.set_text_wl("tagNo", "666", "Код")
        page.set_text_wl("name", "Канцелярские товары", "Наименование")
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)
        
    def test_creating_a_new_entry_in_the_directory_Objects_OZ(self):
        # Создание новой записи в справочнике «Объекты ОЗ»
        page = MenuPage(self.driver)
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Объекты МЗ')
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.set_text_wl("tagNo", "555", "Шифр")
        page.set_date_wl("name", "Бумага формата А4", "Наименование")
        page.set_select2_wl("unitOfMeasure", "Упаковка", "Единица измерения")
        page.set_select2_wl("group", "Канцтовары", "Группа материальных запасов")
        page.set_select2_wl("parentHierarchy", "Канцелярские товары", "Входит в папку")
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)

    # def test_copy_entry_in_the_directory_Objects_OZ(self):
    #     # Копирование записи в справочнике «Объекты ОЗ»
    #     page = MenuPage(self.driver)
    #     page.table_select_row("Бумага формата А4")
    #     page.click_by_text("Добавить")
    #     page.click_by_text("Копию карточки")
    #     # Данной суб-кнопки нет на портале, по сценарию она должна быть

    def test_editing_created_entry_in_the_directory_Objects_OZ(self):
        # Редактирование созданной записи в справочнике «Объекты ОЗ»
        page = Browser(self.driver)
        page.search_string("Бумага формата А4")
        page.table_select_row("Бумага формата А4", order=1)
        page.click_by_text("Открыть")
        page.set_text_wl("tagNo", "666", "Шифр")
        page.set_date_wl("name", "Бумага формата А3", "Наименование")
        page.set_select2_wl("unitOfMeasure", "Упаковка", "Единица измерения")
        page.set_select2_wl("group", "Канцтовары", "Группа материальных запасов")
        page.set_select2_wl("parentHierarchy", "Канцелярские товары", "Входит в папку")
        page.set_date_wl("validTill", "01.01.2030", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)

    def test_creating_an_entry_in_the_Additional_characteristics_of_MZ(self):
        # Cоздание записи во вкладке «Дополнительные характеристики МЗ»
        page = Browser(self.driver)
        page.search_string("Бумага формата А3")
        page.table_select_row("Бумага формата А3", order=1)
        page.click_by_text("Открыть")
        page.scroll_to_bottom()
        page.click_by_text("Добавить", order=2)
        page.set_text_wl("name", "Бумага_Снегурочка", "Характеристика объекта", order=2)
        page.set_text_wl("price", "150.00", "Цена")
        page.set_date_wl("acquisitionDate", "15.02.2018", "Дата поступления")
        page.click_by_text("Сохранить", order=2)
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(2)

    def test_delete_created_entry_in_the_directory_Objects_OZ(self):
        # Удаление созданной записи в справочнике «Объекты ОЗ»
        page = Browser(self.driver)
        sleep(2)
        page.search_string("Бумага формата А3")
        page.table_select_row("Бумага формата А3", order=1)
        page.click_by_text("Удалить")
        page.click_by_text("Да")

    def test_creation_of_a_new__materially_responsible_person(self):
        # Создание записи в справочнике «МОЛ»
        page = MenuPage(self.driver)
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Материально ответственные лица')
        page.click_by_text("Добавить")
        page.set_text_wl("name", "Иванов И.И.", "Краткое наименование")
        page.set_text_wl("fullName", "Иванов Иван Иванович", "Полное наименование")
        page.set_select2_wl("position", "Начальник отдела", "Должность")
        page.set_select2_wl("department", "Департамент внешних коммуникаций", "Подразделение")
        page.set_checkbox_wl("isWarehouseWorker")
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text("Сохранить")
        sleep(1)
        page.click_by_text("Закрыть")
        
    def test_creation_document_receipt_OC(self):
        # Создание документа «Приход ОС»
        page = MenuPage(self.driver)
        page.click_button_eagle()
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text("Добавить")
        page.set_text_wl("tagNoFirstPart", "10134", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "4", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013400004", ">>>")
        page.set_text_wl("fullName", "Принтер Epson 35C", "Полное наименование")
        page.set_text_wl("propertyDesignation", '"ООО "ОЛДИ 3""', "Поставщик")
        page.set_date_wl("issueDate", "01.02.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "01.02.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "MDV87628764", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_modal_to_bottom()
        page.set_text_wl("cost", "7500.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "36", "Срок полезного использования (месяцев)")
        page.set_select2_wl("amortizationGroup", " 2 ГРУППА", "Амортизационная группа")
        page.set_select2_wl("okof", "Устройства ввода и вывода информации", "ОКОФ")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        sleep(1)
        page.click_button_eagle()
        page.click_by_text("Поступление НФА")
        page.click_by_text("Добавить")
        page.set_text_wl("documentNumber", "1", "Номер")
        page.set_select2_wl("documentKind", "Акт приема-передачи", "Вид документа")
        page.set_date_wl("documentDate", "01.02.2018", "Дата")
        page.set_date_wl("entryDate", "01.02.2018", "Дата проводки")
        page.set_text_wl("comment", "Приход ОС от поставщика", "Комментарий")
        page.set_select2_wl("materiallyResponsiblePerson", "Абдуллина З.Ш.", "МОЛ")
        page.set_select_wl("senderSenderType", "Организация", "Вид отправителя")
        page.set_select2_wl("organization", 'ООО "ОЛДИ 3"', "Наименование отправителя")
        page.click_by_text('Добавить')
        page.click_by_text('Новая строка ОС, НМА')
        page.set_select2_wl("operation", "Приход машин и оборудования через подотчет", "Типовая операция")
        # Нет зависимости "Наименования" и "Инвентарного номера" (дописать тест стр. 40 после испр. ошибки)
        # Также не работает контексный поиск в справочнике "Картотека ОС, НМА, НПА"
        # и механизм автозаполнения полей по нажатие на кнопку "Новое" в "Новом объекте ОС, НМА" (смтр. стр. 39)
        page.set_text_wl("tagNo", "1013400004", "Инвентарный №")
        page.set_text_wl("amount", "7500.00", "Сумма по документу", order=2)
        page.scroll_modal_to_bottom()
        page.set_select2_wl("kbk", "110 0408 23 4 10 90019 242", "КБК", exactly=False)
        page.set_select2_wl("kosgu", "310", "КОСГУ", exactly=False)
        page.set_select2_wl("costElement", "Увеличение стоимости основных средств", "Вид затрат")
        page.click_by_text('Сохранить', order=2)
        page.click_by_text('Сохранить', order=1)
        page.click_by_text("Закрыть")











