
from behave.__main__ import main as behave_main

from Utils import Logger

if __name__ == '__main__':

    # behave_main("features/Login/Login.feature --tags=@valid")

    # behave_main("features/Work_Item/Work_Item.feature")

    # behave_main("features/Work_Item/Work_Item.feature -f json.pretty -o test.json --no-summary")

    behave_main("features/Login/Login.feature -f json.pretty -o test.json --no-summary")