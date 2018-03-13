from time import localtime, strftime, sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from xlutils.copy import copy as xlcopy
import datetime
import os
import json
import xlrd
import xlwt
import hashlib
import shutil


class Browser(object):
    """
    Methods for working with browser
    """
    def __init__(self, driver, timeout=60, log=True):
        self.driver = driver
        self.timeout = timeout
        self.log = log
        self.wait = Wait(self.driver, self.timeout)
        self.checker = Checker(self.driver, self.timeout)


    #
    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().accept()
        except TimeoutException:
            pass

    #
    def decline_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().decline()
        except TimeoutException:
            pass

    # Click по локатору(Пример: (By.XPATH, "//input[@id='documentNumber']"))
    def click(self, locator, label=None):
        self.wait.loading()
        element = self.wait.element_appear(locator)
        self.move_to_element(element)
        element.click()
        if label and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), label))

    # Click по тексту для кнопки или ссылки по тексту
    def click_by_text(self, text, order=1, exactly=False):
        self.wait.loading()
        if exactly:
            locator = (By.XPATH, "(//*[self::a or self::button][normalize-space()='%s'])[%s]" % (text, order))
        else:
            locator = (By.XPATH,
                       "(//*[self::a or self::button][contains(normalize-space(), '%s')])[%s]" % (text, order))
        element = self.wait.element_appear(locator)
        self.move_to_element(element)
        element.click()
        if text and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), text))

    # Click по атрибуту объекта на странице
    def click_by_value(self, value, order=1, exactly=False):
        self.wait.loading()
        if exactly:
            locator = (By.XPATH, "(//input[@value='%s'])[%s]" % (value, order))
        else:
            locator = (By.XPATH, "(//input[contains(@value, '%s')])[%s]" % (value, order))
        element = self.wait.element_appear(locator)
        self.move_to_element(element)
        element.click()
        if value and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))

    # выбор меню
    def click_menu(self, locator):
        sleep(1)
        element = self.driver.find_element_by_xpath(locator[1])
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    # Функция перехода на страницу
    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    # Функция скролирования до элемента
    def move_to_element(self, element):
        self.wait.loading()
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    # Функция скролирования вниз страницы
    def scroll_to_top(self):

        self.wait.loading()
        self.driver.execute_script("window.scrollTo(0, 0);")

    # Функция скролирования вниз страницы
    def scroll_to_bottom(self):

        self.wait.loading()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Функция скролирования модального окна вверх
    def scroll_modal_to_top(self, class_name='modal-body mCustomScrollbar', order=1):
        """
        Method for scrolling to top modal window
        :param class_name: tag class of modal window. there is value by default. change it if tag is different
        :param order: order in case of few modal windows. order starts from 0. that's why there is decreasing by 1
        :return:
        """
        self.driver.execute_script("""
               var modal = document.getElementsByClassName('%s')[%s];
               modal.scrollTo(0, 0);
           """ % (class_name, order - 1))

    # Функция скролирования модального окна вниз
    def scroll_modal_to_bottom(self, class_name='modal-body mCustomScrollbar', order=1):
        """
        Method for scrolling to bottom modal window
        :param class_name: tag class of modal window. there is value by default. change it if tag is different
        :param order: order in case of few modal windows. order starts from 0. that's why there is decreasing by 1
        :return:
        """
        self.driver.execute_script("""
               var modal = document.getElementsByClassName('%s')[%s];
               modal.scrollTo(0, modal.scrollHeight);
           """ % (class_name, order - 1))

    # Функция поиска строки в таблице по текстовому полю "Все поля"
    def search_string(self, value, label=None):
        self.wait.loading()
        self.set_text((By.XPATH, "//*[@placeholder='Все поля']"), value + Keys.RETURN, label)
        if label and self.log:
            print(
                "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция очистка поисковой строки если выбрано несколько фильтров
    def select2_clear(self, locator):
        self.wait.loading()
        element = self.wait.element_appear(locator)
        while True:
            try:
                element.click()
            except (ec.StaleElementReferenceException, ec.NoSuchElementException):
                break

    # Функция заполнение поля через троеточие(выбор из справочника)
    def set_type(self, locator, value, label=None):
        self.wait.loading()
        self.click(locator)
        self.set_text((By.XPATH, "//div[@class='modal-content']//input[@placeholder='Все поля']"),
                      value + Keys.RETURN, label)
        self.click((By.XPATH, "//tr[contains(., '%s')]" % value))
        self.click_by_text("Выбрать")

    # Функция заполнения текстового поля
    def set_text(self, locator, value, label=None):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            element.send_keys(value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения текстового поля без локатора
    def set_text_wl(self, name, value, label=None, order=1):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(
                (By.XPATH, "(//*[@name='%s'])[%s]//*[self::input or self::textarea]" % (name, order)))
            element.clear()
            element.send_keys(value)
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print(
                    "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения поля Дата
    def set_date(self, locator, value, label=None):
        if value:
            if value == "=":
                value = Date.get_today_date()
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            sleep(1)
            element.send_keys(value + Keys.TAB)
            if label and self.log:
                print(
                    "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения поля Дата без локатора
    def set_date_wl(self, name, value, label=None, order=1):
        if value:
            if value == "=":
                value = Date.get_today_date()
            self.wait.loading()
            locator = (By.XPATH, "(//*[@name='%s'])[%s]//input" % (name, order))
            element = self.wait.element_appear(locator)
            element.clear()
            sleep(1)
            element.send_keys(value + Keys.TAB)
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print(
                    "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения текстового поля и проверка содержимого
    def set_text_and_check(self, locator, value, label=None):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            element.send_keys(value)
            self.wait.lamb(lambda x: element.get_attribute("value") == value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения/снятия чек-бокса
    def set_checkbox(self, locator, value=True, label=None):
        element = self.wait.element_appear(locator)
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция заполнения/снятия чек-бокса без локатора
    def set_checkbox_wl(self, name, value=True, label=None, order=1):
        locator = (By.XPATH, "(//*[@name='%s'])[%s]//input" % (name, order))
        element = self.wait.element_appear(locator)
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция(общая) заполнения/снятия чек-бокса по порядку элемента на страницу
    def set_checkbox_by_order(self, order=1, value=True, label=None):
        element = self.wait.element_appear((By.XPATH, "(//input[@type='checkbox'])[%s]" % order))
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция заполнения/снятия радио-баттон
    def set_radio(self, locator, label=None):
        element = self.wait.element_appear(locator)
        element.click()
        if label and self.log:
            print("[%s] [%s] выбор опции" % (strftime("%H:%M:%S", localtime()), label))

    # Функция выбора значения из выпадающего списка
    def set_select(self, locator, value, label=None):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            Select(element).select_by_visible_text(value)
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция выбора значения из выпадающего списка без локататора
    def set_select_wl(self, name, value, label=None, order=1):
        if value:
            self.wait.loading()
            locator = (By.XPATH, "(//*[@name='%s'])[%s]//select" % (name, order))
            element = self.wait.element_appear(locator)
            Select(element).select_by_visible_text(value)
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция выбора значения без локатора
    def set_select2_wl(self, name, value, label=None, exactly=True, order=1):
        if value:
            locator = (By.XPATH, "(//*[@name='%s'])[%s]" % (name, order))
            text_box = self.wait.element_appear((By.XPATH, locator[1] + "//input"))
            text_box.clear()
            text_box.send_keys(value)
            if exactly:
                self.wait.element_appear((By.XPATH, locator[1] + "//li[@role='treeitem' and .='%s']" % value)).click()
            else:
                self.wait.element_appear(
                    (By.XPATH, locator[1] + "//li[@role='treeitem' and contains(., '%s')]" % value)).click()
            self.wait.element_disappear((By.XPATH, "//span[contains(@class, 'select2-dropdown')]"))
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция выбора значения из Select2
    def set_select2(self, locator, value,  label=None, exactly=True):
        if value:
            text_box = self.wait.element_appear((By.XPATH, locator[1] + "//input"))
            # dots_button = self.wait.element_appear((By.XPATH, locator[1]+"//button[@title='Выбрать']"))
            # try:
            #
            #     parent.find_element(By.XPATH, "//button[@title='Очистить']").click()
            # except ec.NoSuchElementException:
            #     pass
            text_box.clear()
            text_box.send_keys(value)

            if exactly:
                self.wait.element_appear((By.XPATH, locator[1] + "//li[@role='treeitem' and .='%s']" % value)).click()
            else:
                self.wait.element_appear(
                    (By.XPATH, locator[1] + "//li[@role='treeitem' and contains(., '%s')]" % value)).click()
            self.wait.element_disappear((By.XPATH, "//span[contains(@class, 'select2-dropdown')]"))
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция выбора строки в таблице и нажатие на неё
    def table_select_row_click(self, text, order=1, label=None):
        self.wait.loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')])[%s]" % (text, order))
        self.click(locator, label)

    # Функция выбора строки в таблице  и проставление чек-бокса
    def table_select_row(self, text, order=1, label=None):
        self.wait.loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')]//input[@type='checkbox'])[%s]" % (text, order))
        self.set_checkbox(locator, True, label)

    # Функция проставления всех чек-боксов в таблице
    def table_choose_all_checkbox(self, label=None):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//*[@class='w2ui-col-header  ']//input)")
        self.set_checkbox(locator, label)
        sleep(1)

    # Функция выбора чек-бокса в таблице по порядку
    def table_row_checkbox(self, order=1):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='checkbox'])[%s]" % order)
        self.set_checkbox(locator, True)
        sleep(1)

    # Функция выбора радио-баттон в таблице по порядку
    def table_row_radio(self, order=1):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='radio'])[%s]" % order)
        self.set_radio(locator)
        sleep(1)

    # Функция загрузки файла
    def upload_file(self, value, order=1):
        self.wait.loading()
        # открываем страницу с формой загрузки файла
        element = self.driver.find_element(By.XPATH, "(//input[@type='file'])[%s]" % order)

        element.clear()
        element.send_keys("%s/%s" % (os.getcwd(), value))
        WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located((By.XPATH, "//li[@class=' qq-upload-success']")))

    # Функция выбор месяца
    def select_month(self, month, year):
        self.click((By.XPATH, "//button[@class='period-text dropdown-period-toggle']"))
        sleep(1)
        self.click((By.XPATH, "//*[span='%s']" % month))
        sleep(1)
        self.click((By.XPATH, "//*[span='%s']" % year))
        sleep(1)
        self.click((By.XPATH, "//span[@class='qa-icon-close']"))

    def save_screenshot(self, name, default_folder="", overwrite=True):
        """
        Method making screenshot of current page of driver
        :param name: Name of file. Extension is png by default
        :param default_folder: Folder with script by default. Important: use raw-strings if you using different one
        :param overwrite: Overwite file if True
        :return:
        """
        if os.path.isfile("%s%s.png" % (default_folder, name)):
            if overwrite:
                self.driver.save_screenshot("%s%s.png" % (default_folder, name))
            else:
                for i in range(100):
                    if not os.path.isfile("%s%s-%s.png" % (default_folder, name, i + 1)):
                        self.driver.save_screenshot("%s%s-%s.png" % (default_folder, name, i + 1))
                        break
        else:
            self.driver.save_screenshot("%s%s.png" % (default_folder, name))

    # Функция проверки текста в классе. Параметры: value - ожидаемый результат, class_name - имя класса, в котором
    # будет извлечен текст, text_errors - текст ошибки, который будет записан в файл logs.txt
    def checking_text_by_class(self, value, class_name, text_errors):
        find_value = self.driver.find_element_by_class_name(class_name).text
        if value == find_value:
            return True
        else:
            File.add_text_in_file("logs", text_errors)
            return False

    # Проверка текста в локаторе с записью в логфайл
    def check_text_and_logfile(self, locator, value, text_error):
        if self.wait.element_appear(locator).text == value:
            return True
        else:
            File.add_text_in_file("logs", text_error + str(value))
            return False


class Date(object):
    """
    Methods for working with date
    """
    # Функция возвращающая текущую дату
    @staticmethod
    def get_today_date():
        return datetime.date.today().strftime("%d.%m.%Y")

    @staticmethod
    def get_today_file():
        return datetime.date.today().strftime("%Y%d%m")


class Wait(object):
    """
    Methods for waiting
    """
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    # Функция ожидания текста пока не появится
    def text_appear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    # Функция ожидания пока текст не пропадёт
    def text_disappear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    # Функция ожидания элемента пока не появится  в скрытых
    def presence_of_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    # Функция ожидания элемента пока не появится
    def element_appear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))

    # Функция ожидания пока элемент не пропадёт
    def element_disappear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located(locator))

    def lamb(self, exe):
        return WebDriverWait(self.driver, self.timeout).until(exe)

    # Функция ожидания окончания закгрузки - пока не пропал лоадер
    def loading(self):
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='loading-spinner']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='windows8']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='w2ui-lock']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.presence_of_element_located((By.XPATH, "//*[contains(., 'Документ сохранен')]")))


# Проверка текста
class Checker(object):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = Wait(self.driver, self.timeout)

    # Проверка текста без локатора в input или textarea(поля ввода) в атрибуте title
    def check_text_title(self, name, value):
        fact_value = self.wait.element_appear(
            (By.XPATH, "//*[@name='%s']//*[self::input or self::textarea]" % name)).get_attribute("title")
        if fact_value == value:
            print(fact_value + " - значение поля СООТВЕТСТВУЕТ эталону - " + str(value))
            return True
        else:
            print("Значение :" + fact_value + " значение поля НЕ СООТВЕТСТВУЕТ эталону :" + str(value))
            return False

    # Проверка текста без локатора в input или textarea(поля ввода) в атрибуте value
    def check_text_input(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//*[self::input or self::textarea]" % (name, order)))
        actual_value = element.get_attribute("value")
        if actual_value == value:
            print(actual_value + " - значение поля СООТВЕТСТВУЕТ эталону - " + str(value))
            return True
        else:
            print("Значение :" + actual_value + " значение поля НЕ СООТВЕТСТВУЕТ эталону :" + str(value))
            return False

            # Проверка текста без локатора в select(поле выбора из справочника)

    def check_text_select(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//li" % (name, order)))
        actual_value = element.get_attribute("title")
        if actual_value == value:
            print(actual_value + " - значение поля СООТВЕТСТВУЕТ эталону - " + str(value))
            return True
        else:
            print("Значение :" + actual_value + " значение поля НЕ СООТВЕТСТВУЕТ эталону :" + str(value))
            return False

            # Проверка текста c локатором в input

    def check_text_locator(self, locator, value):
        element = self.wait.element_appear(locator)
        actual_value = element.get_attribute("value")
        if actual_value == value:
            print(actual_value + " - значение поля СООТВЕТСТВУЕТ эталону - " + str(value))
            return True
        else:
            print("Значение :" + actual_value + " значение поля НЕ СООТВЕТСТВУЕТ эталону :" + str(value))
            return False

    # Проверка текста без локатора в input

    def check_text(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//input" % (name, order)))
        actual_value = element.get_attribute("value")
        if actual_value == value:
            print(actual_value + " - значение поля СООТВЕТСТВУЕТ эталону - " + str(value))
            return True
        else:
            print("Значение :" + actual_value + " значение поля НЕ СООТВЕТСТВУЕТ эталону :" + str(value))
            return False

    def check_message(self, value):
        element = self.wait.element_appear(
            (By.XPATH, "//document-execution-result/div"))
        actual_value = ' '.join(element.text.split('\n'))
        print(actual_value)
        print('Проверка...')
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("СООТВЕТСТВУЕТ")
            return True
        else:
            print("НЕ СООТВЕТСТВУЕТ")
            return False


# Работа с данными
class Data(object):
    """
    Methods for working with data
    """
    @staticmethod
    def load_data(file):
        script_path = os.path.dirname(__file__)
        filename = os.path.join(script_path, 'data\\%s.json' % file)
        return json.loads(open(filename, encoding="utf8").read())

    @staticmethod
    def get_data_by_value(data, parent, key, value):
        for i in data[parent]:
            if value == i[key]:
                return i
        return None

    @staticmethod
    def get_data_by_number(data, parent, number=0):
        return data[parent][number]


class File(object):
    """
    Методы для работы с файлами
    """
    # Добавление текста в файл
    @staticmethod
    def add_text_in_file(filename, text):
        with open(filename + ".txt") as my_file:
            tmp = my_file.read()
        with open(filename + ".txt", "w") as my_file:
            my_file.write(tmp + "\n" + text)

    @staticmethod
    def file_copy(filename):
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        test_buch = ('C:\\TestBuch\\')
        # Проверка наличия папки C:\TestBuch
        if os.access(test_buch, os.F_OK ):
            pass
        else:
            os.mkdir(test_buch)
        # Проверка наличия папки C:\Users\'Доменное имя пользователя'\Downloads
        if os.access(test_default, os.F_OK ):
            pass
        else:
            os.mkdir(test_default)
        # os.chdir(test_buch)
        path = Date.get_today_file()
        # Проверка наличия папки с датой проведения теста
        if os.access(test_buch+path, os.F_OK ):
            pass
        else:
            os.mkdir(test_buch+path)
        # os.chdir(test_default)
        # Копируем полученную печатную форму в отдельный каталог C:\TestBuch
        shutil.copy2(test_default + filename, test_buch+path)
        # os.remove(filename) удаление  файла из Downloads
        if os.access(test_default + "example.xls", os.F_OK):
            pass
        else:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Лист1")
            sheet.write(0, 0, 'Тест')
            workbook.save(test_default + "example.xls")
        if os.access(test_default + "example_new.xls", os.F_OK):
            pass
        else:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Лист1")
            sheet.write(0, 0, 'Тест')
            workbook.save(test_default + "example_new.xls")

    @staticmethod
    def get_max_rows_and_cols(file):
        rows_max = 0
        cols_max = 0
        for name in file.sheet_names():
            sheet = file.sheet_by_name(name)
            if rows_max < sheet.nrows:
                rows_max = sheet.nrows
            if cols_max < sheet.ncols:
                cols_max = sheet.ncols
        return [rows_max, cols_max]

    # Сравнение excel файлов 1
    @staticmethod
    def analyze_two_files(filename):
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        test_compare = ('C:\\Compare\\')
        File.file_copy(filename)
        reference_file = test_default + filename
        output_file = test_compare + filename
        # output_hash = self.md5(output_file)
        # reference_hash = self.md5(reference_file)
        # открываем исходный файл
        output = xlrd.open_workbook(output_file, on_demand=True, formatting_info=True)
        reference = xlrd.open_workbook(reference_file, on_demand=True, formatting_info=True)
        if output.nsheets != reference.nsheets:
            print('Количество книг не совпадает')
        else:
            output_max = File.get_max_rows_and_cols(output)
            reference_max = File.get_max_rows_and_cols(reference)
            max_rows = max(reference_max[0], output_max[0])
            max_cols = max(reference_max[1], output_max[1])

            reference_new = xlcopy(reference)
            for i in range(reference.nsheets):
                sheet = reference_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            reference_new.save(test_default + "example.xls")
            output_new = xlcopy(output)
            for i in range(output.nsheets):
                sheet = output_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            output_new.save(test_default + "example_new.xls")
            return [test_default + "example.xls", test_default + "example_new.xls"]

    @staticmethod
    def compare_files(filename):
        files = File.analyze_two_files(filename)
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        reference = xlrd.open_workbook(files[0], on_demand=True, formatting_info=True)
        output = xlrd.open_workbook(files[1], on_demand=True, formatting_info=True)
        flag = True
        print("[%s] ПРОВЕРКА ПЕЧАТНОЙ ФОРМЫ : \"%s\"" % (strftime("%H:%M:%S", localtime()), filename))
        for index in range(reference.nsheets):
            reference_sheet = reference.sheet_by_index(index)
            output_sheet = output.sheet_by_index(index)
            reference_sheet_name = reference_sheet.name
            output_sheet_name = output_sheet.name
            if reference_sheet_name != output_sheet_name:
                print("Название книги[%s] не совпадает с эталонным [%s]!" % (output_sheet_name, reference_sheet_name))
            for i in range(reference_sheet.nrows):
                for j in range(reference_sheet.ncols):
                    reference_cell = reference_sheet.cell(i, j).value
                    output_cell = output_sheet.cell(i, j).value
                    if reference_cell != output_cell:
                        if flag:
                            flag = False
                        print("Книга [%s]:" % reference_sheet_name)
                        print("\tЯчейка [%s, %s]. Значение [%s] не совпадает с эталонным [%s]!"
                              % (i+1, j+1,reference_cell, output_cell))
        reference.release_resources()
        output.release_resources()
        del reference
        del output
        if flag:
            print("[%s] Печатные формы одинаковы" % (strftime("%H:%M:%S", localtime())))
        os.remove(test_default + "example.xls")
        os.remove(test_default + "example_new.xls")

    # Получение хеша
    @staticmethod
    def md5(filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def checking_file_export_UFK():
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        flag = True
        for file in os.listdir(test_default):
            if file.endswith(".ZR3"):
                print("[%s] Фаил с именем [%s] Выгружен" % (strftime("%H:%M:%S", localtime()), file))
                flag = False
        if flag:
            print("[%s] Файлов выгрузки не найдено" % strftime("%H:%M:%S", localtime()))
