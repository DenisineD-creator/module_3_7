def calculate_s_sum(s):
    total = 0

    if isinstance(s, (int, float)):
        total += s
    elif isinstance(s, str):
        total += len(s)
    elif isinstance(s, dict):
        for key, value in s.items():
            total += calculate_s_sum(key)
            total += calculate_s_sum(value)
    elif isinstance(s, (list, tuple, set)):
        for item in s:
            total += calculate_s_sum(item)

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_s_sum(data_structure)
print(result)
