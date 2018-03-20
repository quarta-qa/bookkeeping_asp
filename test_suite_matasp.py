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

    def telst_adding_entries_to_the_directory_of_fixed_assets(self):
        # Добавление в справочник «Объекты ОС,НМА,НПА» 4 основных средства, стр. 8-10

        page = MenuPage(self.driver)
        page.select_month("Февраль", "2018")
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Машины и оборудование") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Здания") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        # page.click_to_eagle("Сохранить")

        # Создание ОС Жилое здание, Малая Никитская, д.2

        page = CardIndexOSNMANPAPage(self.driver)
        page.click_by_text("Добавить")
        page.tag_no_first_part("10112")
        page.tag_no_second_part("1")
        page.checker.check_text("tagNo", "1011200001")
        # page.tag_no("1011200001") - если не работает автозаполнение
        page.full_name("Жилое здание, Малая Никитская, д.2")
        page.property_designation("Административное здание")
        page.unit_of_measure("Штука")
        page.issue_date("11.02.2018")
        page.start_up_date("11.02.2018")
        sleep(1)
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.scroll_to_bottom()
        page.cost("1430000.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока". Дописать после исправления.
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
        page.checker.check_text("tagNo", "1013400001")
        # page.tag_no("1013400001") - если не работает автозаполнение
        page.full_name("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.unit_of_measure("Штука")
        page.issue_date("12.02.2018")
        page.serial_number("JKN87628764")
        page.start_up_date("12.02.2018")
        sleep(1)
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.scroll_to_bottom()
        page.cost("36500.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока". Дописать после исправления.
        page.value_added_used("36")
        page.amortization_group(" 2 ГРУППА")
        page.okof("ЭВМ общего назначения")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        sleep(1)

        # Создание ОС "Копировальный аппарат"

        page.click_by_text("Добавить")
        page.tag_no_first_part("10134")
        page.tag_no_second_part("2")
        page.checker.check_text("tagNo", "1013400002")
        # page.tag_no("1013400002") - если не работает автозаполнение
        page.full_name("Копировальный аппарат Xerox Phaser 8200")
        page.unit_of_measure("Штука")
        page.issue_date("13.02.2018")
        page.serial_number("GH57654898672FGD")
        page.start_up_date("13.02.2018")
        sleep(1)
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.scroll_to_bottom()
        page.cost("18000.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока". Дописать после исправления.
        page.value_added_used("120")
        page.amortization_group(" 5 ГРУППА")
        page.okof("Оборудование фоторепродукционное,копировальное и для обработки фотоматериалов")
        page.click_by_text("Сохранить")
        sleep(1)
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")

        # Создание ОС "Автомобиль"

        page.click_by_text("Добавить")
        page.tag_no_first_part("10135")
        page.tag_no_second_part("1")
        page.checker.check_text("tagNo", "1013500001")
        # page.tag_no("1013500001") - если не работает автозаполнение
        page.full_name("Автомобиль Volswagen passat 2.0 TFSI")
        page.unit_of_measure("Штука")
        page.supplier('ООО "АВТОС"')
        page.issue_date("14.02.2018")
        page.serial_number("BNV876876JH093S")
        page.start_up_date("14.02.2018")
        sleep(1)
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.scroll_to_bottom()
        page.cost("1256000.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока".
        page.value_added_used("60")
        page.amortization_group(" 3 ГРУППА")
        page.okof("Автомобили легковые среднего класса (срабочим объемом двигателя свыше 1,8 до 3,5 лвключительно)")
        page.click_by_text("Сохранить")
        sleep(1)
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")

    def test_creation_of_a_materially_responsible_person(self):
        # Создание материально-ответственного лица, стр. 11-12
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text("Материально ответственные лица")
        page.click_by_text("Добавить")
        page = MateriallyResponsiblePersonPage(self.driver)
        page.employee("Ротко С.В.")
        page.checker.check_text("name", "Ротко С.В.")
        page.checker.check_text("fullName", "Ротко Сергей Васильевич")
        # page.name("Ротко С.В.") - если не работает автозаполнение
        # page.full_name("Ротко Сергей Васильевич") - если не работает автозаполнение
        # Текстового поля "Код" нет на портале. Дописать после исправления.
        # Выпадающего поля  "Категория МОЛ" нет на портале. Дописать после исправления.
        page.valid_till("01.01.2050")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    def test_creation_of_document_admission_nfa_and_attachment_4oc(self):
        # Создание поступление НФА и прикрепление созданных 4-ех ОС, 12-16 стр.
        # При заполнении поля "Инвентарный №" ссылочное поле "Наименование" автоматически не заполняется
        #  Ошибка №234 в TFS.

        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.click_by_text("Поступление НФА")
        # page.click_by_text("Добавить - Новый документ") на портале нет суб-кнопки. Дописать после исправления.
        page.click_by_text("Добавить")
        # ШАПКА ДОКУМЕНТА
        page = ReceiptOfNonFinancialAssetsCapPage(self.driver)
        page.document_number("Пр.акт.")
        page.document_kind("Начальные остатки")
        page.document_date("01.02.2018")
        page.entry_date("01.02.2018")
        page.materially_responsible_person("Ротко С.В.")
        page.sender_sender_type("Организация")
        page.organization('ООО "КВАРТА ВК"')
        page.comment("Начальные остатки ОС")

        # СТРОКА ДОКУМЕНТА
        # СОЗДАТЬ СТРОКУ "ОС,НМА" - Жилое здание, Малая Никитская, д.2
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page = ReceiptOfNonFinancialAssetsRowPage(self.driver)
        page.operation("Начальные остатки Здания")
        page.tag_no("1011200001")
        page.checker.check_text_input("item", "Жилое здание, Малая Никитская, д.2")
        page.amount("1 430 000,00")
        page.checker.check_text("accountableAmount", "1 430 000,00")
        page.amortization("600 600.00")
        page.comment("Начальные остатки")
        page.scroll_modal_to_bottom()
        page.kbk("(2016) - ЦА 242")
        page.kosgu("310")
        page.click_by_text("Сохранить", order=2)

        # СОЗДАТЬ СТРОКУ "ОС,НМА" - Ноутбук Toshiba
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page = ReceiptOfNonFinancialAssetsRowPage(self.driver)
        page.operation("Начальные остатки Машины и оборудование")
        page.tag_no("1013400001")
        page.checker.check_text_input("item", "Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.amount("36 500,00")
        page.checker.check_text("accountableAmount", "36 500,00")
        page.amortization("28 389.89")
        page.comment("Начальные остатки")
        page.scroll_modal_to_bottom()
        page.kbk("(2016) - ЦА 242")
        page.kosgu("310")
        page.click_by_text("Сохранить", order=2)

        # СОЗДАТЬ СТРОКУ "ОС,НМА" - Копировальный аппарат
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page = ReceiptOfNonFinancialAssetsRowPage(self.driver)
        page.operation("Начальные остатки Машины и оборудование")
        page.tag_no("1013400002")
        page.checker.check_text_input("item", "Копировальный аппарат Xerox Phaser 8200")
        page.amount("18 000,00")
        page.checker.check_text("accountableAmount", "18 000,00")
        page.amortization("3 150.00")
        page.comment("Начальные остатки")
        page.scroll_modal_to_bottom()
        page.kbk("(2016) - ЦА 242")
        page.kosgu("310")
        page.click_by_text("Сохранить", order=2)

        # СОЗДАТЬ СТРОКУ "ОС,НМА" - Автомобиль
        page.click_by_text("Добавить")
        page.click_by_text("Новая строка ОС, НМА")
        page = ReceiptOfNonFinancialAssetsRowPage(self.driver)
        page.operation("Начальные остатки Машины и оборудование")
        page.tag_no("1013400002")
        page.checker.check_text_input("item", "Автомобиль Volswagen passat 2.0 TFSI")
        page.amount("1 256 000,00")
        page.checker.check_text("accountableAmount", "1 256 000,00")
        page.amortization("62 800.00")
        page.comment("Начальные остатки")
        page.scroll_modal_to_bottom()
        page.kbk("(2016) - ЦА 242")
        page.kosgu("310")
        page.click_by_text("Сохранить", order=2)
        page.click_by_text("Сохранить")
        sleep(5)
        page.click_by_text("Закрыть")

    def test_carrying_out_document_admission_nfa(self):
        # Проведение документа Поступление НФА с 4-мя записями ОС, стр. 16

        page = MenuPage(self.driver)
        page.click_to_eagle()
        page.click_by_text('Поступление НФА')
        page.select_month("Февраль", "2018")
        # page.table_select_row('ООО "КВАРТА ВК"')
        page.table_select_row('01.02.2018')
        page.click_by_text("Действия")
        sleep(5)
        page.click_by_text("Провести", order=2)
        sleep(5)
        page.set_date_wl("lddate_prov", "01.02.2018", "Дата проводки")
        page.click_by_text("Провести", order=3)
        page.checker.check_message("Проведено документов: 1 Не проведено: 0")
        # page.click((By.XPATH, "//button[.='Провести']"), "Провести")
        page.click_by_text('Закрыть')

    def test_viewing_of_document_admission_nfa(self):
        # Просмотр проводок по документу Поступление НФА с 4-мя записями ОС, стр. 16.
        
        page = Browser(self.driver)
        page.table_select_row('ООО "КВАРТА ВК"')
        page.click_by_text('Действия')
        page.click_by_text('Просмотр проводок')
        sleep(3)

    def test_add_another_entry_to_the_asset_catalog(self):
        # Добавление в справочник ОС еще одной записи и помещение ее в папку, стр. 16-19
        # По сценарию созданную запись нужно поместить в папку, но суб-кнопки "Добавить-Новую папку" на портале нет,
        # ошибка в TFS №2364

        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text('Добавить')
        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_first_part("10134")
        page.tag_no_second_part("3")
        page.checker.check_text("tagNo", "1013400003")
        # page.tag_no("1013400001") - если не работает автозаполнение
        page.full_name("Системный блок")
        page.unit_of_measure("Штука")
        page.supplier('ООО "ОЛДИ 3"')
        page.issue_date("12.02.2018")
        page.start_up_date("12.02.2018")
        page.serial_number("JO4445566")
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.group('С/блоки')
        page.scroll_to_bottom()
        page.cost("25 300.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока". Дописать после исправления.
        page.value_added_used("60")
        page.amortization_group(" 3 ГРУППА")
        page.okof("Машины вычислительные электронные цифровые")
        page.click_by_text("Сохранить")
        sleep(2)
        page.click_by_text("Закрыть")
        # page.click_by_text("Да")
        # page.click_by_text("Добавить - Папку - ХОЗ Инвентарь") - на портале нет суб-кнопки "Добавить папку",
        #  дописать после после исправлния.

    def test_create_a_template_for_the_card_os_nma_npa(self):
        # Создание Шаблона карточки ОС, НМА, НПА, стр. 21-23

        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Шаблоны карточки ОС, НМА, НПА')
        page.click_by_text("Добавить")
        page = CreateATemplateForTheCardOSNMANPA(self.driver)
        page.name("Шкаф для документации")
        page.unit_of_measure("Штука")
        # По сценарию нужно заполнить поле "Папка" значением - "ХОЗ. ИНВЕНТАРЬ",
        # но на портале в справочнике "Картотека ОС, НМА, НПА" нет функционала - добавить папку
        page.group("Мебель")
        page.okof("Шкафы для документации")
        page.amortization_group(" 4 ГРУППА")
        page.click_by_text("Сохранить", order=2)
        sleep(3)
        page.click_by_text("Закрыть", order=2)

    def test_creation_of_the_basic_means_using_the_created_template_of_the_card_osnmanpa(self):
        # Cоздание основного средства используя созданный шаблон карточки ОС,НМА,НПА, 23-24
        # На портале не работает автозополнение полей в ОС при выборе шаблона карточки, TFS - product backlog item №589

        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text("Добавить")
        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_first_part("10136")
        page.tag_no_second_part("1")
        page.checker.check_text("tagNo", "1013600001")
        page.template("Шкаф для документации")
        # После выбора значения из поля "Шаблон карточки" автоматич. заполн-ся следующие поля:
        page.checker.check_text("fullName", "Шкаф для документации")
        page.checker.check_text_input("unitOfMeasure", "Штука")
        page.checker.check_text_input("group", "Мебель")
        page.scroll_to_bottom()
        page.checker.check_text_input("amortizationGroup", " 4 ГРУППА")
        page.checker.check_text_input("okof", "Шкафы для документации")
        # Т.к. автозаполнение не работет, эти поля заполняем вручную т.к. некоторые из них обязательные
        page.full_name("Шкаф для документации")
        page.unit_of_measure("Штука")
        page.unit_of_measure("Штука")
        page.supplier('АБ "АСПЕКТ"')
        page.issue_date("15.02.2018")
        page.start_up_date("15.02.2018")
        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется. Дописать после исправления.
        page.group('Мебель')
        page.scroll_to_bottom()
        page.cost("25 300.00")
        # Нет чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока". Дописать после исправления.
        page.value_added_used("84")
        page.amortization_group(" 3 ГРУППА")
        page.okof("Шкафы для документации")
        page.click_by_text("Сохранить")
        sleep(3)
        page.click_by_text("Закрыть")

    # def test_copy_entries_to_the_directory_of_fixed_assets(self):
    #     # Копирование записи ОС, стр. 25
    #     # По сценарию нужно сделать копию строки, но суб-кнопки "Добавить - Копию строки" на портале нет,
    #     # ошибка в TFS №2364, дописасть тест после исправления
    #     page.Browser(self.driver)
    #     page.references()
    #     page.click_by_text('Объекты ОС, НМА, НПА')
    #     page.click_by_text('Добавить')
    #     page.click_by_text('Копию строки')
        
    def test_editing_copy_entries_to_the_directory_of_fixed_assets(self):
        # Редактирование записи ОС, стр. 25-27

        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.click_by_text('Открыть')
        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_second_part("2")
        page.serial_number("JO4445567")
        sleep(3)
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')

    def test_deletion_of_a_record_in_the_fixed_assets_directory(self):
        # Удаление записи ОС, стр. 27-28

        page = Browser(self.driver)
        page.table_select_row("transsed 32 GB USB-флеш накопитель (с системой Гарант)")
        page.click_by_text('Удалить')
        page.click_by_text('Да')
        page.click_by_text('Закрыть')

    def test_print_inventory_card_okud_0504031(self):
        # Печать инвентарной карточки учета ОКУД 504031, стр. 30

        page = Browser(self.driver)
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)", order=1)
        page.click_by_text('Печать')
        page.click_by_text('Инвентарная карточка учета (форма по ОКУД 0504031)')
        sleep(2)
        File.compare_files('Инвентарная карточка НФА.xls')

    # def test_printing_of_a_group_inventory_cardOKUD0504032(self):
        # Печать инвентарной карточки учета ОКУД 504032, стр. 31
        # Строка 314-319 актуальна после исправления ошибки -
        # На портале не формируется файл, нельзя проверить печатную форму

        # page = Browser(self.driver)
        # page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)", order=1)
        # page.click_by_text('Печать')
        # page.click_by_text('Групповая инвентарная карточка (форма по ОКУД 0504032)')
        # sleep(2)
        # File.compare_files('Групповая инвентарная карточка НФА.xls')

    def test_checking_the_mode_mass_filling_of_os_parameters(self):
        # Проверка режима «Массовое заполнение параметров ОС», стр. 31-32
        
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.table_select_row("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.table_select_row("Копировальный аппарат Xerox Phaser 8200")
        page.table_select_row("Автомобиль Volswagen passat 2.0 TFSI")
        page.table_select_row("Систмный блок")
        page.click_by_text("Действия")
        page.click_by_text('Массовое заполнение параметров объектов')
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        page.set_text_wl("propertyDesignation", "Массовое заполнение 3-х полей", "Назначение объекта")
        page.set_date_wl("startUpDate", "25.02.2018", "Дата ввода в эксплуатацию")
        page.set_date_wl("issueDate", "02.02.2018", "Дата выпуска")
        page.click_by_text('Выполнить')
        page.click_by_text('Закрыть')

    def test_creating_a_new_entry_in_the_directory_objects_oz(self):
        # Создание новой записи в справочнике «Объекты ОЗ», стр. 31-33

        # Создание первой записи
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
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)

        # Создание второй записи
        page.click_by_text("Добавить")
        page.click_by_text("Новую строку")
        page.set_text_wl("tagNo", "555", "Шифр")
        page.set_date_wl("name", "Степлер", "Наименование")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        page.set_select2_wl("group", "Канцтовары", "Группа материальных запасов")
        page.set_date_wl("validTill", "01.01.2050", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)

    # def test_copy_entry_in_the_directory_Objects_OZ(self):

    #     # Копирование записи в справочнике «Объекты ОЗ», стр.33
    #     # По сценарию нужно сделать копию строки, но суб-кнопки "Добавить - Копию строки" на портале нет,
    #     # ошибка в TFS №2364
    #     page = MenuPage(self.driver)
    #     page.table_select_row("Бумага формата А4")
    #     page.click_by_text("Добавить")
    #     page.click_by_text("Копию карточки")

    def test_editing_created_entry_in_the_directory_objects_oz(self):
        # Редактирование созданной записи в справочнике «Объекты ОЗ», стр.34

        page = Browser(self.driver)
        page.search_string("Степлер")
        page.table_select_row("Степлер", order=1)
        page.click_by_text("Открыть")
        page.set_text_wl("tagNo", "666", "Шифр")
        page.set_date_wl("name", "Степлер2", "Наименование")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")
        page.set_select2_wl("group", "Канцтовары", "Группа материальных запасов")
        page.set_select2_wl("parentHierarchy", "Канцелярские товары", "Входит в папку")
        page.set_date_wl("validTill", "01.01.2030", "Дата актуальности")
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')
        sleep(2)

    def test_delete_created_entry_in_the_directory_objects_oz(self):
        # Удаление созданной записи в справочнике «Объекты ОЗ», стр. 35

        page = Browser(self.driver)
        sleep(2)
        page.search_string("Степлер2")
        page.table_select_row("Степлер2", order=1)
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        sleep(2)
        page.click_by_text("Закрыть")
        sleep(2)

    def test_creating_an_entry_in_the_additional_characteristics_of_mz(self):
        # Cоздание записи во вкладке «Дополнительные характеристики МЗ», стр. 35-36

        page = Browser(self.driver)
        page.search_string("Бумага формата А4")
        page.table_select_row("Бумага формата А4", order=1)
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

    def test_creation_of_a_new__materially_responsible_person(self):
        # Создание записи в справочнике «МОЛ», стр. 36-37

        page = MenuPage(self.driver)
        page.click_to_eagle()
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

    def test_creation_document_admission_nfa(self):
        # Создание документа «Поступление НФА», стр.38-40
        # По сценарию по нажатию на кнопку "Нов." должно открываться модальное окно ОС
        # (оно должно быть над текущим окном),после его заполнения и сохранения одинаковые поля должны заполняться
        # в Поступление НФА, но вместо этого перебрасывает в шапку документа без сохранения строки, ошибка в TFS 1714

        page = MenuPage(self.driver)
        page.select_month("Февраль", "2018")
        page.click_to_eagle()
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
        page.click_by_text('Сохранить')
        # Добавить Новую строку ОС,НМА
        page.click_by_text('Добавить')
        page.click_by_text('Новая строка ОС, НМА')
        page.set_select2_wl("operation", "Начальные остатки Машины и оборудование", "Типовая операция")
        page.set_select2_wl("kbk", "(2016) - ЦА 242", "КБК", exactly=False)
        page.scroll_modal_to_bottom()
        page.set_select2_wl("kosgu", "310", "КОСГУ", exactly=False)
        page.click((By.XPATH, "//a[contains(.,'Новое')]"), "Новое")
        page.click_by_text("Сохранить", order=2)
        # При нажатие на кнопку "Сохранить - order=2" строка не сохраняется

        page.set_text_wl("tagNoFirstPart", "10134", "Первая часть инвентарного номера")
        page.set_text_wl("tagNoSecondPart", "4", "Вторая часть инвентарного номера")
        page.set_text_wl("tagNo", "1013400004", ">>>")
        page.set_text_wl("fullName", "Принтер Epson 35C", "Полное наименование")
        page.set_text_wl("propertyDesignation", '"ООО "ОЛДИ 3""', "Поставщик")
        page.set_date_wl("issueDate", "01.02.2018", "Дата выпуска")
        page.set_date_wl("startUpDate", "01.02.2018", "Дата ввода в эксплуатацию")
        page.set_text_wl("serialNumber", "MDV87628764", "Серийный №")
        page.set_select2_wl("unitOfMeasure", "Штука", "Единица измерения")

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется

        page.scroll_to_bottom()
        page.set_text_wl("cost", "7500.00", "Первоначальная стоимость")
        # Чек-бокса "Начислять бухгалтерскую амотризацию исходя из срока" нет на портале, в сценарии он есть
        page.set_text_wl("valueAddedUsed", "36", "Срок полезного использования (месяцев)")
        page.set_select2_wl("amortizationGroup", " 2 ГРУППА", "Амортизационная группа")
        page.set_select2_wl("okof", "Устройства ввода и вывода информации", "ОКОФ")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")

    # def test_checking_the_mode_check_Mass_receipt_of_OS_NMA(self):
    #     # Проверка режима «Массовое поступление ОС,НМА»
    #     # На портале не реализован функционал массового заполнения строк
    #
    #     page = MenuPage(self.driver)
    #     page.select_month("Февраль", "2018")
    #     page.references()
    #     page.click_by_text("Поступление НФА")
    #     page.table_select_row('ООО "ОЛДИ 3"', order=1)
    #     page.click_by_text('Открыть')
    #     page.table_select_row("", order=1)
    #     page.click_by_text('Добавить')
    #     page.click_by_text('Массовое поступление ОС, НМА')
    #     page.accept_alert('Ок')
    #     # При нажатие на суб-кнопку "Массовое поступление ОС, НМА" появляется уведомление- Функционал не реализован
    #
    # def test_carrying_out_document_admission_NFA2(self):
    #     # Проведение документа «Поступление НФА», стр. 42
    #     # Нельзя провести документ от 01.02.2018 Отправитель - ООО "ОЛДИ 3", т.к. не работает массовое поступление
    #
    #     page = MenuPage(self.driver, 5)
    #     page.select_month("Февраль", "2018")
    #     page.click_by_text('Поступление НФА')
    #     page.table_select_row('ООО "ОЛДИ 3"', order=1)
    #     page.click_by_text('Действия')
    #     page.click_by_text('Провести')
    #     page.set_date_wl("lddate_prov", "01.02.2018", "Дата проводки")
    #     page.set_select2_wl("OperationMaster", "Начальные остатки Машины и оборудование", "Типовая операция")
    #     page.click((By.XPATH, "//button[.='Провести']"), "Провести")
    #     sleep(3)
    #     page.click_by_text('Закрыть')
    #
    # def test_viewing_of_the_document_with_the_group_entrance_Admission_of_the_NFA(self):
    #     # Просмотр проведения документа c групповым приходом «Поступление НФА», стр. 42-43
    #     # Нельзя просмотреть проводки документа от 01.02.2018 Отправитель - ООО "ОЛДИ 3",
    #     # т.к. не работает массовое поступление
    #
    #     page = Browser(self.driver, 5)
    #     page.table_select_row('ООО "ОЛДИ 3"', order=1)
    #     page.click_by_text('Действия')
    #     page.click_by_text('Просмотр проводок')

    def test_сhecking_the_print_receipt_of_materials(self):
        # Проверка печати «Акта о приеме-передаче объектов нефинансовых активов», стр. 43-48
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату и файл в C:\Compare!

        page = MenuPage(self.driver, 5)
        page.select_month("Январь", "2018")
        page.click_by_text('Поступление НФА')
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Печать')
        page.click_by_text('Акт приемки материалов')
        sleep(5)
        File.compare_files('Акт приемки материалов.xls')

    def test_checking_the_printing_of_a_receipt_receipt_for_valuables(self):
        # Проверка печати «Акта о приеме-передаче объектов нефинансовых активов», стр. 43-48
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату и файл в C:\Compare!

        page = Browser(self.driver)
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Печать')
        page.click_by_text('Приходный ордер на приемку материальных ценностей')
        sleep(5)
        File.compare_files('Приходный ордер на приемку материальных ценностей (НФА).xls')

    def test_checking_the_printing_of_act_acceptance_transfer_of_objects_of_non_financial_assets(self):
        # Проверка печати «Акта о приеме-передаче объектов нефинансовых активов», стр. 43-48
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату и файл в C:\Compare!

        page = Browser(self.driver)
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Печать')
        page.click_by_text('Акт о приеме-передаче объектов нефинансовых активов')
        page.set_text_wl("foundationDocument", "Акт о приеме-передаче объектов нефинансовых активов", "Основание")
        page.set_text_wl("foundationNumber", "1", "Номер")
        page.set_date_wl("foundationDate", "01.01.2018", "Дата")
        page.click_by_text('Сформировать')
        sleep(2)
        File.compare_files('Акт о приеме-передаче объектов нефинансовых активов.xls')
        sleep(2)

    # def test_checking_the_printing_of_act_on_acceptance_of_the_repaired_objects_of_fixed_assets(self):
    #     # Проверка печати «Акта о приеме-сдаче отремонтированных,
    #     # реконструированных и модернизированных объектов основных средств», стр. 43-48
    #     # Проверить нельзя т.к. на портале не формируется файл + документ  создается неправильно
    #
    #     page = Browser(self.driver)
    #     page.table_select_row('ООО "ОЛДИ 3"', order=1)
    #     page.click_by_text('Печать')
    #     page.click_by_text('Акт о приеме-сдаче отремонтированных,'
    #                        ' реконструированных и модернизированных объектов основных средств')
    #     sleep(2)
    #     page.click_by_text('Добавить', order=2)
    #     page.set_text_wl("positionPrintedName", "Директор", "Должность")
    #     page.set_date_wl("employeePrintedName", "Иванов И.И.", "Расшифровка подписи")
    #     page.set_date_wl("inventoryDateFrom", "01.01.2018", "Срок инвентаризации с")
    #     page.set_text_wl("inventoryDateTo", "28.01.2018", "по")
    #     page.click_by_text('Сформировать')
    #     sleep(2)
    #     File.compare_files('Акт о приеме-сдаче отремонтированных,'
    #                        ' реконструированных и модернизированных объектов основных средств.xls')
    #     sleep(2)

    def test_editing_created_document_admission_nfa(self):
        # Редактирование созданной записи в документе «Поступление НФА», 48-49
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату!

        page = MenuPage(self.driver)
        page.select_month("Январь", "2018")
        page.click_by_text('Поступление НФА')
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Открыть')
        page.table_select_row("7 500,00", order=1)
        page.click_by_text('Добавить')
        page.click_by_text('Копию строки')
        page.table_select_row("7 500,00", order=1)
        page.click_by_text('Открыть')
        page.set_select2_wl("kbk", "110 0408 23 4 10 90019 851", "КБК", exactly=False)
        page.set_text_wl("amount", "7 500,00", "Сумма по документу", order=2)
        page.click_by_text('Сохранить', order=2)
        page.click_by_text('Сохранить', order=1)
        sleep(2)
        page.click_by_text("Закрыть")

    def test_mass_parameter_replacement_in_the_document_lines_admission_nfa(self):
        # Массовая замена параметров в строках документа «Поступление НФА», стр. 50-52
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату!

        page = Browser(self.driver)
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Открыть')
        page.scroll_to_bottom()
        page.table_choose_all_checkbox('Выбрать все строки')
        page.click_by_text('Замена')
        page.set_select2_wl("operation", "Начальные остатки Машины и оборудование", "Типовая операция")
        page.set_select2_wl("kbk", "(2016) - ЦА 242", "Код бюджетной классификации", exactly=False)
        sleep(2)
        page.click_by_text('Выполнить')
        page.click_by_text('Закрыть', order=2)
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')

    def test_carrying_of_the_amended_document_admission_nfa(self):
        # Проведение измененного документа «Поступление НФА»
        # Т.к. документ №1 от 01.02.2018 формируется не правильно, для тестирования был создан аналогичный документ
        # (заполненный вручную) от 01.01.2018. После исправления бага изменить дату!

        page = Browser(self.driver)
        page.table_select_row('ООО "ОЛДИ 3"', order=1)
        page.click_by_text('Действия')
        page.click_by_text('Провести')
        page.set_date_wl("lddate_prov", "01.01.2018", "Дата проводки")
        page.set_select2_wl("OperationMaster", "Начальные остатки Машины и оборудование", "Типовая операция")
        page.click((By.XPATH, "//button[.='Провести']"), "Провести")
        sleep(2)
        page.click_by_text('Закрыть')

    def test_accrual_of_amortization_on_the_os_under_the_account(self):
        # Начисление Амортизации на ОС по счету, стр. 52-54

        page = MenuPage(self.driver, 5)
        page.select_month("Март", "2018")
        page.click_by_text('Начисление амортизации')
        page.click_by_text('Добавить')
        page.click_by_text('Расчет по бухгалтерским данным')
        page.set_date_wl('balancesCollectionDate', "01.03.2018", "Дата сбора остатков")
        page.set_date_wl('operationDate', "01.03.2018", "Дата формирования операции")
        page.set_select2_wl("balanceSheetAccount", "1 101 34", "Счет учета ОС, НМА")
        page.click_by_text('Выполнить')
        sleep(2)
        page.click_by_text('Да')
        page.click_by_text('Сохранить')
        page.click_by_text('Закрыть')

    # def test_check_printing_of_the_statement_of_the_calculation_of_depreciation(self):
        # Проверка печати ведомости «начисление Амортизации», стр. 54
        # При нажатие на суб-кнопку "Печать" появляется уведомление- Функционал не реализован

        # page = Browser(self.driver)
        # page.table_select_row("4 074,08", "1")
        # page.click_by_text('Печать')
        # File.compare_files('Ведомость начисления амортизации.xls')
        # Появляется ошибка XML

    def test_deletion_of_the_calculation_of_depreciation(self):
        # Удаление записи «Начисление Амортизации», стр. 54

        page = Browser(self.driver)
        page.table_select_row("01.03.2018", "1")
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        page.click_by_text("Закрыть")

    def test_accrual_of_depreciation_on_a_group_of_accounts(self):
        # Начисление амотризации на ОС по группе счетов, стр. 55-56
        # Начисление производится только по балансовому счету № 110112, который находится в группе счетов "ОС",
        # ошибка в TFS № 2372

        page = MenuPage(self.driver, 5)
        page.select_month("Март", "2018")
        page.click_by_text('Начисление амортизации')
        page.click_by_text('Добавить')
        page.click_by_text('Расчет по бухгалтерским данным')
        page.set_date_wl('balancesCollectionDate', "01.03.2018", "Дата сбора остатков")
        page.set_date_wl('operationDate', "01.03.2018", "Дата формирования операции")
        page.set_select2_wl("balanceSheetAccountGroup", "ОС", "Группа счетов учета ОС, НМА")
        page.click_by_text('Выполнить')
        sleep(2)
        page.click_by_text('Нет')
