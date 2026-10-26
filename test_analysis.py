
import pandas as pd
from analysis import analyse_sales


def test_analyse_sales():
    df, total_revenue, product_revenue = analyse_sales("data/sales.csv")

    # Check whether the data is loaded
    assert not df.empty

    # Check whether Revenue column exists
    assert "Revenue" in df.columns

    # Check total revenue
    assert total_revenue == 1397300

    # Check product revenue
    assert product_revenue["Keyword"] == 754800
