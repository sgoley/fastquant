import pandas as pd
from fastquant import (
    get_pse_data,
    get_yahoo_data,
    get_stock_data,
    get_crypto_data,
    pse_data_to_csv,
)

PHISIX_SYMBOL = "JFC"
CRYPTO_SYMBOL = "BTC/USDT"
YAHOO_SYMBOL = "GOOGL"
DATE_START = "2018-01-01"
DATE_END = "2019-01-01"


def test_get_pse_data():
    stock_df = get_pse_data(PHISIX_SYMBOL, DATE_START, DATE_END)
    assert isinstance(stock_df, pd.DataFrame)


def test_get_yahoo_data():
    stock_df = get_yahoo_data(YAHOO_SYMBOL, DATE_START, DATE_END)
    assert isinstance(stock_df, pd.DataFrame)


def test_get_stock_data():
    # Test w/ respective sources
    stock_df = get_stock_data(
        PHISIX_SYMBOL, DATE_START, DATE_END, source="phisix"
    )
    assert isinstance(stock_df, pd.DataFrame)

    stock_df = get_stock_data(
        YAHOO_SYMBOL, DATE_START, DATE_END, source="yahoo"
    )
    assert isinstance(stock_df, pd.DataFrame)

    # Test getting yahoo when (default) phisix fails on a non PSE SYMBOL
    stock_df = get_stock_data(YAHOO_SYMBOL, DATE_START, DATE_END)
    assert isinstance(stock_df, pd.DataFrame)


def test_get_crypto_data():
    # test that multiple exchanges work
    from fastquant.crypto import CRYPTO_EXCHANGES

    exchange_pairs = {
        "binance": "BTC/USDT",
        "coinbasepro": "BTC/USD",
        "bithumb": "XRP/KRW",
        "kraken": "BTC/USD",
        "kucoin": "BTC/USDT",
        "bitstamp": "BTC/USD",
    }

    for ex in CRYPTO_EXCHANGES:
        crypto_df = get_crypto_data(
            exchange_pairs[ex], DATE_START, DATE_END, exchange=ex
        )
        assert isinstance(crypto_df, pd.DataFrame)
