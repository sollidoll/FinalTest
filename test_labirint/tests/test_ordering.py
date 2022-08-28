import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from settings import data_for_ordering, cases_for_ordering, invalid_numbers, invalid_nums_cases
from driver import driver_path


@pytest.fixture(autouse=True)
def testing():

    # Указываем путь к драйверам браузера
    pytest.driver = pytest.driver = webdriver.Chrome(executable_path=driver_path)
    # Переходим на страницу сайта
    pytest.driver.get('https://www.labirint.ru/')
    # Нажимаем на принятие cookie
    pytest.driver.find_element(By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]').click()

    yield

    # Закрываем все вкладки
    pytest.driver.quit()


@pytest.mark.parametrize('data', data_for_ordering, ids=cases_for_ordering)
def test_name_field(data):

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в корзину
    for x in range(1, 6):
        pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[x].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Переходим к оформлению заказа
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-large fright start-checkout-js"]'))).click()
    # Вводим данные в поле Имя
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Имя"]'))).send_keys(data)
    # Выбираем другое поле, чтобы поле Имя проверило введенные данные
    pytest.driver.find_element(By.XPATH, '//input[@placeholder="Фамилия"]').click()
    # Проверяем наличие ошибки
    try:
        pytest.driver.find_element(By.XPATH, '//div[@class="text-xs css-default"]')
        error = True
    except NoSuchElementException:
        error = False
    # Проверяем какие данные были введены и в зависимости от этого делаем проверку
    if data.isalpha() and len(data)<=50:
        assert error == False
    else:
        assert error == True


@pytest.mark.parametrize('data', data_for_ordering, ids=cases_for_ordering)
def test_second_name_field(data):

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в корзину
    for x in range(1, 6):
        pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[x].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Переходим к оформлению заказа
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-large fright start-checkout-js"]'))).click()
    # Вводим данные в поле Фамилия
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Фамилия"]'))).send_keys(data)
    # Выбираем другое поле, чтобы поле Фамилия проверило введенные данные
    pytest.driver.find_element(By.XPATH, '//input[@placeholder="Имя"]').click()
    # Проверяем наличие ошибки
    try:
        pytest.driver.find_element(By.XPATH, '//div[@class="text-xs css-default"]')
        error = True
    except NoSuchElementException:
        error = False
    # Проверяем какие данные были введены и в зависимости от этого делаем проверку
    if data.isalpha() and len(data)<=50:
        assert error == False
    else:
        assert error == True


@pytest.mark.parametrize('data', invalid_numbers, ids=invalid_nums_cases)
def test_number_field(data):

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в корзину
    for x in range(1, 6):
        pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[x].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Переходим к оформлению заказа
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-large fright start-checkout-js"]'))).click()
    # Вводим данные в поле Мобильный телефон
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Мобильный телефон"]'))).clear()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Мобильный телефон"]'))).send_keys(data)
    # Выбираем другое поле, чтобы поле Мобильный телефо проверило введенные данные
    pytest.driver.find_element(By.XPATH, '//input[@placeholder="Имя"]').click()
    # Проверяем наличие кнопки подтвердить
    try:
        pytest.driver.find_element(By.XPATH, '//div[@class="pointer v-color--blue-link confirm-login-btn padding-s"][@style=""]')
        error = True
    except NoSuchElementException:
        error = False
    # Проверяем какие данные были введены и в зависимости от этого делаем проверку
    if data == '+375 29 123 23 23':
        assert error == True
    else:
        assert error == False