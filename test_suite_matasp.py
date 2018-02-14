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

    def test_directory_name_of_fixed_assets(self):
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Машины и оборудование") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Машины и оборудование") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить - Папку - Транспорт") - на портале нет суб-кнопки, в сценарии есть
        # page.click_by_text("Добавить")

        # Создание ОС Жилое здание, Малая Никитская, д.2

        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_first_part("10112")
        page.tag_no_second_part("1")
        page.tag_no("1011200001")
        page.full_name("Жилое здание, Малая Никитская, д.2")
        page.property_designation("Административное здание")
        page.start_up_date("05.07.1968")
        page.unit_of_measure("Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.cost("1430000.00")
        page.exlude_from_depreciation_accrual()
        page.value_added_used("1200")
        page.okof("Здания производственные административные")
        page.amortization_group("10 ГРУППА")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        page.click_by_text("Да")
        sleep(2)

        # Создание ОС "Ноутбук Toshiba"

        page.click_by_text("Добавить")
        page.tag_no_first_part("10134")
        page.tag_no_second_part("1")
        page.tag_no("1013400001")
        page.full_name("Ноутбук Toshiba (Intel Core Duo 2Ghz,2048Mb,120Gb)")
        page.start_up_date("01.08.2014")
        page.serialNumber("JKN87628764")
        page.unit_of_measure("Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.cost("36500.00")
        page.exlude_from_depreciation_accrual()
        page.value_added_used("36")
        page.okof("ЭВМ общего назначения")
        page.amortization_group(" 2 ГРУППА")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        page.click_by_text("Да")
        sleep(2)

        # Создание ОС "Копировальный аппарат"

        page.click_by_text("Добавить")
        page.set_text_wl("tagNoFirstPart", "10134")
        page.set_text_wl("tagNoSecondPart", "2")
        page.set_text_wl("tagNo", "1013400002")
        page.set_text_wl("fullName", "Копировальный аппарат Xerox Phaser 8200")
        page.set_date_wl("startUpDate", "16.03.2014")
        page.set_text_wl("serialNumber", "GH57654898672FGD")
        page.set_select2_wl("unitOfMeasure", "Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "18000.00")
        page.set_checkbox_wl("exludeFromDepreciationAccrual","True")
        page.set_text_wl("valueAddedUsed", "120")
        page.set_select2_wl("okof","Оборудование фоторепродукционное,копировальное и для обработки фотоматериалов")
        page.set_select2_wl ("amortizationGroup", " 5 ГРУППА")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        page.click_by_text("Да")
        sleep(2)

        # Создание ОС "Автомобиль"

        page.click_by_text("Добавить")
        page.set_text_wl("tagNoFirstPart", "10135")
        page.set_text_wl("tagNoSecondPart", "1")
        page.set_text_wl("tagNo", "1013500001")
        page.set_text_wl("fullName", "Автомобиль Volswagen passat 2.0 TFSI")
        page.set_text_wl("propertyDesignation", "ООО Германика")
        page.set_date_wl("issueDate", "23.06.2014")
        page.set_date_wl("startUpDate", "15.09.2014")
        page.set_text_wl("serialNumber", "BNV876876JH093S")
        page.set_select2_wl("unitOfMeasure", "Штука")
        sleep(1)

        # Выпадающего поля "Папка" нет на портале, в сценарии оно заполняется
        page.scroll_to_bottom()
        page.set_text_wl("cost", "1256000.00")
        page.set_checkbox_wl("exludeFromDepreciationAccrual", "True")
        page.set_text_wl("valueAddedUsed", "60")
        page.set_select2_wl("okof", "Автомобили легковые среднего класса "
                                    "(срабочим объемом двигателя свыше 1,8 до 3,5 лвключительно)")
        page.set_select2_wl("amortizationGroup", " 3 ГРУППА")
        page.click_by_text("Сохранить")
        page.click_by_text("Закрыть")
        page.click_by_text("Да")
        sleep(2)





