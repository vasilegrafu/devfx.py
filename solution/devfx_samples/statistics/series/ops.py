import devfx.statistics as stats

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""------------------------------------------------------------------------------------------------
"""
result = stats.series.count(data)
print(f"count: {result}")


"""------------------------------------------------------------------------------------------------
"""
result = stats.series.get(data, 1)
print(f"get: {result}")

result = stats.series.get(data, (1, 2))
print(f"get: {result}")

result = stats.series.get(data, slice(None, 3))
print(f"get: {result}")

result = stats.series.get(data, slice(3, None))
print(f"get: {result}")


"""------------------------------------------------------------------------------------------------
"""
result = stats.series.sample(data, 4)
print(f"sample: {result}")

result = stats.series.shuffle(data)
print(f"shuffle: {result}")

"""------------------------------------------------------------------------------------------------
"""
result = stats.series.split(data, 4)
print(f"split: {result}")

result = stats.series.split(data, 0.4)
print(f"split: {result}")

