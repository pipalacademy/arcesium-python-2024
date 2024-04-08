
def test_function_name():
    import combined_daily_time_series
    assert hasattr(
        combined_daily_time_series, "combined_daily_time_series"), "Could not find function combined_daily_time_series"

    assert hasattr(
        combined_daily_time_series, "get_total_volume"), "Could not find function get_total_volume"


def test_combined_daily_time_series():
    from pandas.api.types import is_numeric_dtype
    from combined_daily_time_series import combined_daily_time_series, get_total_volume
    symbols = ['AAPL', 'IBM']
    df = combined_daily_time_series(symbols)
    cols = ['open', 'high', 'low', 'close', 'volume']
    assert all([c in df.columns for c in cols])
    assert len(df) == 200
    assert all([is_numeric_dtype(df[c]) for c in cols])
    assert get_total_volume(df).equals(df.groupby('symbol').sum()['volume'])
    assert set(df.symbol.unique()) == set(symbols)
