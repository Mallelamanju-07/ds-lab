import pandas as pd
p = pd.Period('2026-03', freq='M')
print("Original Period:")
print(p)
print("\nAfter adding 4:")
print(p + 4)

print("\nAfter adding 5:")
print(p + 5)

print("\nAfter subtracting 2:")
print(p - 2)

print("\nAfter subtracting 4:")
print(p - 4)
periods = pd.period_range(
    start='2026-03',
    periods=5,
    freq='M'
)

print("\nRange of Periods:")
print(periods)
