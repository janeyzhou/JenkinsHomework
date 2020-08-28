from behave import given, when, then
import logging


@given('a sample text loaded into the object')
def step_given_text(context):
    given_text = context.text
    logging.info(f"Text is: {given_text}")


@when('we activate the object')
def step_when(context):
    logging.info("@@@@@@@@@@@@@@@@ we activate the object")


@given('a set of specific users')
def step_given_table(context):
    data_table = context.table
    for row in data_table:
        logging.info(f"Row value: {row['name']}")
        logging.info(f"Row value: {row['department']}")
