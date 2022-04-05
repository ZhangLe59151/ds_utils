import unittest

from utils_for_ds import data_utils
import pandas as pd

class TestCase1(unittest.TestCase):
    def test_create_date_df(self):
        df = pd.DataFrame(['column_1', 'column_2'], [1, 2])
        df_res = pd.DataFrame(['column_2', 'column_1'], [2, 1])
        self.assertEqual(data_utils.switch_y_column(df, 'column_1'), df_res)
        # self.assertNotEqual(PyDash.lower("test"), "TEST")

    def test_switch_y_column_1_columns(self):
        df = pd.DataFrame(['column_1'], [1])
        df_res = pd.DataFrame(['column_1'], [1])
        self.assertEqual(data_utils.switch_y_column(df, 'column_1'), df_res)
        # self.assertNotEqual(PyDash.upper("TEST"), "test")

    def test_title_method(self):
        self.assertEqual(PyDash.title("hello world"), "Hello world")
        self.assertNotEqual(PyDash.title("hELLO wORLD"), "hello world")

    def test_kebab_method(self):
        self.assertEqual(PyDash.kebab("Kebab case adds hyphens BetWEEN lowerCASE text"),
                         "kebab-case-adds-hyphens-between-lowercase-text")
        self.assertNotEqual(PyDash.kebab("Kebab case doesn't contain spaces"), "kebab-case-doesn't contain spaces")
