def double_until_limit(start, limit):
    steps = 0
    while start < limit:
        start *= 2
        steps += 1
    return steps

number = 1
limit = 50
result = double_until_limit(number, limit)
print(f"Чтобы достичь {limit}, надо: {result} шагов удвоения.")


# Алгоритм увеличивает число, умножая его на 2, пока не достигнет или превысит заданный предел.