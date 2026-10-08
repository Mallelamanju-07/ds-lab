import pandas as pd

dates = pd.to_datetime([
    '2026-05-5',
    '2026-06-10',
    '2026-07-15',
    '2026-08-20'
])

sales = pd.Series(
    [1000, 1500, 1800, 2200],
    index=dates
)

print("Original Series:")
print(sales)



period_series = sales.to_period('M')

print("\nSeries converted to Monthly Periods:")
print(period_series)



df = pd.DataFrame(
    {
        'Sales': [1000, 1500, 1800, 2200],
        'Profit': [225, 300, 450, 500]
    },
    index=dates
)

print("\nOriginal DataFrame:")
print(df)



period_df = df.to_period('M')

print("\nDataFrame converted to Monthly Periods:")
print(period_df)
