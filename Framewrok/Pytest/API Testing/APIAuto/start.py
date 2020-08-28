import os
import sys

import pytest


def call_pytest():
    root = os.path.join(os.path.dirname(__file__), "")
    exitcode = pytest.main(
        [
            root,
            "-k test_user",
            "-v",
	        "-s",
            "--junitxml=report/create_user.xml"        ]
    )
    return exitcode


if __name__ == '__main__':
    running_result = call_pytest()
    sys.exit(running_result)
