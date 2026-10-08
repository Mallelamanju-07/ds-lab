import pandas as pd
date_index = pd.date_range(
    start='2026-01-20',
    periods=8,
    freq='D')
print("Generated DatetimeIndex:")
print(date_index)
