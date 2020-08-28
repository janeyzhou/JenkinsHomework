from behave import given, when, then
import logging


@given('I put "{thing}" in a blender')
def step_given(context, thing):
    # out line headers and cell value
    # logging.info(f'headers is: {context.active_outline.headings} and cells : {context.active_outline.cells}')
    logging.info(f'The cell value we use: {thing}')


@then('it should transform into "{other_thing}"')
def step_then(context, other_thing):
    logging.info(f'The cell value we use: {other_thing}')


@then('Put params into step "{success}"')
def step_params(context, success):
    logging.info(f'The cell value we use: {success}')
