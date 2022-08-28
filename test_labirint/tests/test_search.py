import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import data_for_search, cases_for_search
from driver import driver_path


@pytest.fixture(autouse=True)
def testing():

    # Указываем путь к драйверам браузера
    pytest.driver = webdriver.Chrome(executable_path=driver_path)
    # Переходим на страницу сайта
    pytest.driver.get('https://www.labirint.ru/')
    # Нажимаем на принятие cookie
    pytest.driver.find_element(By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]').click()

    yield

    # Закрываем все вкладки
    pytest.driver.quit()


@pytest.mark.parametrize('data', data_for_search, ids=cases_for_search)
def test_search_field_with_positive_data(data):

    # Вводим данные в поле поиска
    pytest.driver.find_element(By.ID, 'search-field').send_keys(data)
    # Нажимаем на кнопку поиска
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()

    assert 'search' in pytest.driver.current_url


def test_search_field_with_empty_string():

    # Вводим данные в поле поиска
    pytest.driver.find_element(By.ID, 'search-field').send_keys('')
    # Нажимаем на кнопку поиска
    search_button = pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')
    search_button.click()

    assert pytest.driver.current_url == 'https://www.labirint.ru/'


def test_amount_of_book():

    # Вводим данные в поле поиска
    pytest.driver.find_element(By.ID, 'search-field').send_keys('Git')
    # Нажимаем на кнопку поиска
    pytest.driver.find_element(By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]').click()
    # Запоминаем число книг, которое выдал поиск
    amount_books = pytest.driver.find_element(By.XPATH, '//a[@href="/search/Git/?stype=0"]/span[@class]').text
    # Подсчитываем количество книг
    current_books = pytest.driver.find_elements(By.CLASS_NAME, 'genres-carousel__item')

    assert int(amount_books) == len(current_books)