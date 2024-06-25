import unittest

import pandas as pd

from utils.market_utils import MarketUtils


class MarketUtilsTest(unittest.TestCase):
    def test_rsi_calculator(self):
        dummy_data = [1.23, 4.56, 7.89, 10.11, 13.14, 16.17, 19.20, 22.23, 25.26, 28.29, 4.56, 7.89, 10.11, 13.14,
                      16.17]
        dummy_df = pd.DataFrame(dummy_data, columns=['closePrice'])

        expected_rsi = [100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 44.48, 48.78,
                        51.47, 54.96, 58.19, ]
        expected_rsi_df = pd.DataFrame(expected_rsi, columns=['rsi'])

        calculated_rsi = MarketUtils.calculate_rsi(dummy_df["closePrice"])

        self.assertEqual(calculated_rsi[0], expected_rsi_df["rsi"][0])
        self.assertEqual(calculated_rsi[1], expected_rsi_df["rsi"][1])
        self.assertEqual(calculated_rsi[10], expected_rsi_df["rsi"][10])

    def test_kline_data_to_df(self):
        data = [
            [1.23, 4.56, 7.89, 10.11, 13.14, 7.89, 10.11],
            [16.17, 19.20, 22.23, 25.26, 28.29, 19.20, 22.23],
            [31.32, 34.35, 37.38, 40.41, 43.44, 79.80, 82.83],
            [46.47, 49.50, 52.53, 55.56, 58.59, 49.50, 52.53],
            [61.62, 64.65, 67.68, 70.71, 73.74, 28.29, 19.20],
            [76.77, 79.80, 82.83, 85.86, 88.89, 34.35, 37.38],
            [91.92, 94.95, 97.98, 100.01, 103.04, 58.59, 49.50],
        ]
        dataframe = MarketUtils.kline_data_to_dataframe(data)

        self.assertEqual(dataframe["closePrice"][0], 13.14)
        self.assertEqual(dataframe["turnover"][3], 52.53)
        self.assertEqual(dataframe["closePrice"][5], 88.89)


if __name__ == '__main__':
    unittest.main()
