import allure
from allure_commons.types import Severity
from selene import browser, by, have, be


# 1. Чистый Selene (без шагов)
def test_plain_selene():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
    browser.element(".FormControl-input").submit()

    browser.element(by.link_text("eroshenkoam/allure-playwright-example")).click()
    browser.element("#issues-tab").click()
    browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)


# 2. Лямбда шаги через with allure.step
def test_allure_lambda_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-button").click()
        browser.element(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
        browser.element(".FormControl-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-playwright-example")).click()

    with allure.step("Кликаем по табу Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем, что есть Issue #1"):
        browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)


# 3. Шаги с декоратором @allure.step
@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element(".FormControl-input").send_keys(repo)
    browser.element(".FormControl-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем вкладку Issues")
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем, что есть Issue #1")
def should_see_issue():
    browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)


def test_allure_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-playwright-example")
    go_to_repository("eroshenkoam/allure-playwright-example")
    open_issues_tab()
    should_see_issue()


# 4. Все аннотации Allure
@allure.tag("web", "smoke")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "student")
@allure.feature("Issues в репозитории")
@allure.story("Проверка наличия Issue в репозитории")
@allure.link("https://github.com", name="Testing")
@allure.title("Проверка Issue #1 в репозитории")
@allure.description("Тест проверяет, что в репозитории есть Issue с номером 1")
def test_allure_annotations():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="main_page",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-button").click()
        browser.element(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
        browser.element(".FormControl-input").submit()
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="search_results",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-playwright-example")).click()
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="repository_page",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Открываем вкладку Issues"):
        browser.element("#issues-tab").click()
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="issues_tab",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Проверяем наличие Issue #1"):
        browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="issue_found",
                      attachment_type=allure.attachment_type.PNG)