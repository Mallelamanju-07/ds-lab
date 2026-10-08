import pandas as pd
dates = pd.to_datetime([
    '2026-01-20',
    '2026-01-21',
    '2026-01-22',
    '2026-01-23',
    '2026-01-24'])
temperature = [38, 28, 29, 32, 35]
time_series = pd.Series(temperature,index=dates)
print("Time Series:")
print(time_series)
