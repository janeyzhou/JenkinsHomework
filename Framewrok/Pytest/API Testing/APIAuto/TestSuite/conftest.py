import os

import pytest
from pip._vendor.distlib._backport import shutil

# #
# @pytest.fixture(scope = session)
# def preprocessing():
#     # replace existed result file
#     current_dir = os.path.dirname(__file__)
#     result_path = os.path.join(current_dir, "..", "result")
#     print(result_path)
#     if os.path.exists(result_path):
#         for i in os.listdir(result_path):
#             file_path = os.path.join(result_path, i)
#             if os.path.isfile(file_path):
#                 os.remove(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#     else:
#         os.mkdir(result_path)

