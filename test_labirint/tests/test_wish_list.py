import pytest
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


def test_add_book_to_wish_list():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Запоминаем название первой книги
    name = pytest.driver.find_element(By.XPATH, '//div[@class="genres-carousel__item"][1]//span[@class="product-title"]').text
    # Добавляем книгу в отложенные
    pytest.driver.find_element(By.XPATH, '//div[@class="genres-carousel__item"][1]//a[@class="icon-fave  track-tooltip js-open-deferred-block "]').click()
    # Переходим на вкладку отложенные
    pytest.driver.find_element(By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown"]/a/span[@class="b-header-b-personal-e-text"]').click()
    # Проверяем наличие книги в списке и соответствие названий
    name_in_wish_list = pytest.driver.find_element(By.XPATH, '//div[@class="products-row "][1]//span[@class="product-title"]').text

    assert name_in_wish_list == name


def test_add_several_books_to_wish_list():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в отложенные
    for x in range(1,6):
        pytest.driver.find_element(By.XPATH, f'//div[@class="genres-carousel__item"][{x}]//a[@class="icon-fave  track-tooltip js-open-deferred-block "]').click()
    # Переходим на вкладку отложенные
    pytest.driver.find_element(By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown"]/a/span[@class="b-header-b-personal-e-text"]').click()
    # Проверяем количество книг в списке
    amount_of_book = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-padding product-padding-cart"]')))

    assert len(amount_of_book) == 5


def test_remove_book_from_wish_list():

    # Вводим запрос в поиск
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Агата Кристи')
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Добавляем книги в отложенные
    for x in range(1, 4):
        pytest.driver.find_element(By.XPATH, f'//div[@class="genres-carousel__item"][{x}]//a[@class="icon-fave  track-tooltip js-open-deferred-block "]').click()
    # Переходим на вкладку отложенные
    pytest.driver.find_element(By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown"]/a/span[@class="b-header-b-personal-e-text"]').click()
    # Убираем книгу из отложенных
    pytest.driver.find_element(By.XPATH, '//a[@class="icon-fave active track-tooltip js-open-deferred-block js-deferred-remove hovering"]/span').click()
    # Перезагружаем страницу
    pytest.driver.refresh()
    # Проверяем количество книг в списке
    amount_of_book = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-padding product-padding-cart"]')))

    assert len(amount_of_book) == 2