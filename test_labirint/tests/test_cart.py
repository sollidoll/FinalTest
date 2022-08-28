import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def test_add_book_to_cart():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Запоминаем название первой книги
    name = pytest.driver.find_element(By.XPATH, '//div[@class="genres-carousel__item"][1]//span[@class="product-title"]').text
    # Добавляем книгу в корзину
    pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[0].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Проверяем наличие книги в корзине
    name_in_wish_list = pytest.driver.find_element(By.CLASS_NAME, 'product-title').text

    assert name_in_wish_list == name


def test_add_several_books_to_cart():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в корзину
    for x in range(1, 6):
        pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[x].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Проверяем количество книг в списке
    amount_of_book = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-padding product-padding-cart"]')))

    assert len(amount_of_book) == 5


def test_change_amount_of_book():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Запоминаем цену товара
    price = pytest.driver.find_elements(By.XPATH, '//span[@class="price-val"]/span')[0].text
    # Добавляем книгу в корзину
    pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[0].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Изменяем количество товара
    pytest.driver.find_element(By.XPATH, '//input[@class="quantity"]').clear()
    pytest.driver.find_element(By.XPATH, '//input[@class="quantity"]').send_keys('10')
    # Время ожидания добавлено для того, чтобы итоговая цена изменилась
    time.sleep(2)
    # Запоминаем итоговую стоимость
    final_price = pytest.driver.find_element(By.XPATH, '//span[@id="basket-default-sumprice-discount"]').text
    final_price = final_price.replace(' ','')

    assert int(price)*10 == int(final_price)


def test_remove_book_from_cart():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книгу в корзину
    pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[0].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Удаляем книгу из корзины
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="checkbox-ui-e-bg b-checkbox-e-bg-m-white b-checkbox-m-radius"]'))).click()
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-small btn-invert btn-pad-10 b-action-panel-e-btn-m-main js-ap-btn-remove"]'))).click()
    # Ждём подгрузки страницы
    page = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="b-bask-panel"]/span')))

    assert 'ВАША КОРЗИНА ПУСТА' in page.text


def test_remove_several_books_from_cart():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в корзину
    for x in range(1, 6):
        pytest.driver.find_elements(By.XPATH, '//a[@class="btn buy-link btn-primary"]')[x].click()
    # Переходим в корзину
    pytest.driver.find_element(By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]/span[@class="b-header-b-personal-e-text"]').click()
    # Очищаем корзину
    pytest.driver.find_element(By.XPATH, '//div/a[@class="b-link-popup"]').click()
    # Ждём подгрузки страницы
    page = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="b-bask-panel"]/span')))

    assert 'ВАША КОРЗИНА ПУСТА' in page.text