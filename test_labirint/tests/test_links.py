import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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


def test_app_store_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//a[@data-event-content="App Store"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'apps.apple.com' in pytest.driver.current_url


def test_google_play_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//a[@data-event-content="Google Play"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'play.google.com' in pytest.driver.current_url


def test_app_gallery_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//a[@data-event-content="App Gallery"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'appgallery.huawei.com' in pytest.driver.current_url


def test_vk_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://vk.com/labirintru"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'vk.com' in pytest.driver.current_url


def test_vk_kids_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://vk.com/labirintdeti"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'vk.com' in pytest.driver.current_url


def test_youtube_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://www.youtube.com/user/labirintruTV"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'youtube.com' in pytest.driver.current_url


def test_ok_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://ok.ru/labirintru"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'ok.ru' in pytest.driver.current_url


def test_ya_dzen_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://zen.yandex.ru/labirintru"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 'zen.yandex.ru' in pytest.driver.current_url


def test_tg_link():

    # Переходим по ссылке
    pytest.driver.find_element(By.XPATH, '//li/a[@href="https://t.me/labirintru"]').click()
    # Переключаем фокус на новую вкладку
    handles = pytest.driver.window_handles
    pytest.driver.switch_to_window(handles[1])

    assert 't.me' in pytest.driver.current_url