import devfx.statistics as stats

data = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]]

"""------------------------------------------------------------------------------------------------
"""
result = stats.mseries.columns(data)
print(f"columns: {result}")

result = stats.mseries.columns_count(data)
print(f"columns_count: {result}")


result = stats.mseries.rows(data)
print(f"rows: {result}")

result = stats.mseries.rows_count(data)
print(f"rows_count: {result}")

"""------------------------------------------------------------------------------------------------
"""
result = stats.mseries.get(data, 1)
print(f"get: {result}")

result = stats.mseries.get(data, (1, 2))
print(f"get: {result}")

result = stats.mseries.get(data, slice(3))
print(f"get: {result}")

result = stats.mseries.get(data, slice(3, stats.mseries.rows_count(data)))
print(f"get: {result}")

"""------------------------------------------------------------------------------------------------
"""
result = stats.mseries.shuffle(data)
print(f"get: {result}")