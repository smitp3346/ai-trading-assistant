import yfinance as yf
from interface.predict_config import INDEX_CONFIG


def predict_next_day(index_name):
    if index_name not in INDEX_CONFIG:
        raise ValueError(f"Unknown index: {index_name}")

    ticker = INDEX_CONFIG[index_name]["ticker"]

    df = yf.download(ticker, period="5d", progress=False)

    if df.empty:
        raise RuntimeError("Unable to fetch market data")

    last_close = float(df["Close"].iloc[-1])

    # Dummy prediction (+1%)
    pred_close = last_close * 1.01
    pred_open = last_close * 1.005

    return {
        "Close": pred_close,
        "Open": pred_open
    }


if __name__ == "__main__":
    print(predict_next_day("nifty50"))