def task_two(minimal: int, maximum: int) -> list:
    """возвращает список всех простых чисел в заданном диапазоне"""

    def simple_num(num):
        if num < 2:
            return False
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True

    list_range = [num for num in range(minimal, maximum + 1) if simple_num(num)]
    return list_range


primes_in_range = task_two(1, 20)
print(primes_in_range)
