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

    def test_name_of_fixed_assets(self):
        page = MenuPage(self.driver)
        page.references()
        page.click_by_text('Объекты ОС, НМА, НПА')
        page.click_by_text("Добавить")
        #page.click_by_text("Добавить папку")
        #суб-кнопки "Добавить - папку" на портале нет, в сценарии она есть
        page = CardIndexOSNMANPAPage(self.driver)
        page.tag_no_first_part("10112")
        page.tag_no_second_part("1")
        page.tag_no("1011200001")
        page.full_name("Жилое здание, Малая Никитская, д.2")
        page.property_designation("Административное здание")
        page.start_up_date("05.07.1968")
        page.unit_of_measure("Штука")

        page.scroll_to_bottom()
        page.cost("1430000.00")
        page.exlude_from_depreciation_accrual()
        page.value_added_used("1200")
        page.okof("Здания производственные административные")
        page.amortization_group("10 ГРУППА")
        sleep(5)






