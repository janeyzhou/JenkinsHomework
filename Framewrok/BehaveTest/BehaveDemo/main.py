from behave.__main__ import main as behave_main
import logger

# https://acme-test.uipath.com/account/login
# aaa@test.com
# 123456
if __name__ == '__main__':
    # Config logger
    logger.init_logging()
    # Run example feature
    # behave_main("features/Example.feature")
    # behave_main("features/Outline.feature -f json.pretty -o test.json --no-summary")

    # Run outline feature {-n "<scenario_name>"}
    # behave_main("features/Outline.feature -f json.pretty -o test.json --no-summary")

    # Run multiple features
    # behave_main("features/Outline.feature features/Example.feature -f json.pretty -o test.json --no-summary")

    # Run selenium features
    behave_main("features/Selenium.feature -f json.pretty -o test.json --no-summary")

    # Run step data scenario -- multiple scenarios run {-n "<scenario_name>" -n "<scenario_name>"}
    # behave_main("features/Outline.feature -n Example1 -n Example2 -f json.pretty -o test.json --no-summary")

    # Run feature by tags
    # behave_main("features/Outline.feature --tags=@tag -f json.pretty -o test.json --no-summary")
