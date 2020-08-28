import logging
import time

from behave import given, when, then

from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from PageObject.ResetTestDataPage import ResetTestDataPage
from PageObject.UpdateWorkItemPage import UpdateWorkItemPage
from PageObject.WorkItemDetailPage import WorkItemDetailPage
from PageObject.WorkItemListPage import WorkItemListPage, WorkItemListPage


@given('I login in with valid account')
def login_with_valid_account(context):
    try:
        # logging.info("Check cookies")
        # context.driver.check_cookie()

        logging.info("Go to login page")
        login_page = LoginPage(context.driver)
        login_page.go_to_page(LoginPage.url, LoginPage.title)

        logging.info("Login with valid user account")
        login_page.login(context.test_data["user_account"]["username"],
                         context.test_data["user_account"]["password"])

        logging.info("Verify greeting information")
        home_page = HomePage(context.driver)
        home_page.verify_greeting(context.test_data["user_account"]["username"])

        logging.info("Reset test data")
        home_page.click_reset_test_data_button()
        reset_test_data_page = ResetTestDataPage(context.driver)
        reset_test_data_page.reset_test_data()

    except Exception as e:
        logging.error(e)
        raise e


@when('I update work item status')
def update_work_item_status(context):
    try:
        for index in context.test_data["row_number"]:
            logging.info("Go to work item list page")
            work_item_list_page = WorkItemListPage(context.driver)
            work_item_list_page.go_to_page(WorkItemListPage.url, WorkItemListPage.title)

            logging.info("Go to work item details page for row {}".format(index))
            work_item_list_page.click_one_work_item(context.driver, index)

            logging.info("Go to update work item page for row {}".format(index))
            work_item_detail_page = WorkItemDetailPage(context.driver)
            work_item_detail_page.click_update_work_item_button()

            logging.info("Update work item for row {}".format(index))
            update_work_item_page = UpdateWorkItemPage(context.driver)
            update_work_item_page.update_work_item(context.test_data['update_info']["comments"],
                                                   context.test_data["update_info"]["status"])

    except Exception as e:
        logging.error(e)
        raise e


@then('I update status successfully')
def check_status_udpated_to_latest_value(context):
    try:
        logging.info("Verify status")
        logging.info("Go to work item list page")
        work_item_list_page = WorkItemListPage(context.driver)
        work_item_list_page.go_to_page(WorkItemListPage.url, WorkItemListPage.title)

        for row in context.test_data["row_number"]:
            work_item_list_page.verify_status(row, context.test_data["update_info"]["status"])
    except Exception as e:
        logging.error(e)
        raise e
