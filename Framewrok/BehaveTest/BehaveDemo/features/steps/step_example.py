from behave import given, when, then
import logging


@given('the ninja has a third level black-belt')
def step_given(context):
    logging.info("the ninja has a third level black-belt")


@when('attacked by a samurai')
def step_when(context):
    logging.info("attacked by a samurai")


@then('the ninja should engage the opponent')
def step_then(context):
    logging.info("the ninja should engage the opponent")
