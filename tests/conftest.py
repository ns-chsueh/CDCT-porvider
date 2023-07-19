# conftest.py is where you setup test configurations and store the testcases that are used by test functions.
from distutils.util import strtobool

def pytest_addoption(parser):
    parser.addoption(
        "--branch", type=str, action="store", 
        help="Git branch")
    parser.addoption(
        "--broker-token", type=str, action="store", 
        help="The broker token to read/write broker"
    )
    parser.addoption(
        "--broker-url", type=str, action="store", 
        help="The broker URL"
    )
    parser.addoption(
        "--publisher-version", type=str, action="store", 
        help="The publisher version"
    )
    parser.addoption(
        "--publish-verification", type=lambda x: bool(strtobool(x)), action="store", 
        help="Whether to published verification results or not.")
