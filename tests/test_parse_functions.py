import pandas as pd
import pytest
from . import *


def test_open_har():
    har_dict = parse_har.open_har('./input/test_data.har')
    assert type(har_dict) == dict


def test_har_to_pdDf():
    har_dict = parse_har.open_har('./input/test_data.har')
    plos_df = parse_har.har_to_pdDf(har_dict)
    assert type(plos_df) == pd.DataFrame


def test_save_to_excel_current():
    har_dict = parse_har.open_har('./input/test_data.har')
    plos_df = parse_har.har_to_pdDf(har_dict)
    parse_har.save_to_excel(plos_df, 'test_data')
    parse_har.save_to_excel(plos_df, 'test_data', save_to='./output')


def test_controller():
    controller.parse_input()
