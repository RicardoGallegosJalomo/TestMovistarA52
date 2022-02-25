import time
import unittest

import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones
from Funciones.Funciones import Funciones_Globales

tie = 3

def setup_function(function):
    print("\nInicia Test")
    global driver, func
    driver = webdriver.Chrome(executable_path="C:/driverchrome/chromedriver.exe")

    func = Funciones_Globales(driver)
    func.navegar("https://tienda.movistar.com.ar", tie)
    driver.maximize_window()

def teardown_function(function):
    print("Finaliza Test")
    driver.close()

def test_A32_Validando_Cuotas():

    func.click_xpath_val("//span[@class='name'][contains(.,'Galaxy A32')]",tie)
    allure.attach(driver.get_screenshot_as_png(), name="Galaxy", attachment_type=AttachmentType.PNG)
    func.Existe("xpath","(//span[contains(@id,'installments-text')])[2]",tie)
    allure.attach(driver.get_screenshot_as_png(), name="Meses", attachment_type=AttachmentType.PNG)

    el1 = func.Selector_xpath("(//span[contains(.,'sin interés')])[6]")
    el1 = el1.text

    if el1 == "sin interés":
        print("\n Si cuenta con 12 meses sin interese")
    else:
        print("\n No Cuenta con 12 meses")

def test_A32_Validando_Gama_Alta():

    func.click_xpath_val("//div[@class='actions'][contains(.,'Search')]",tie)
    func.click_xpath_val("//strong[@data-role='title'][contains(.,'Filtrar por')]",tie)
    func.click_xpath_val("//a[contains(.,'256GB')]",tie)
