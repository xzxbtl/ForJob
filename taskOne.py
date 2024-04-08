from tasks_for_first_job.loggingErrors.errors import logger


def first_task(*args: list) -> list:
    """Возвращает новый список, содержащий только уникальные элементы из исходного списка."""
    new_list = sorted(list(set(args)))
    return new_list


# Если ввод пользователя
"""
try:
    input_from_user = list(map(int, input("Введите числа через пробел: ").split()))
except ValueError as err:
    logger.info(f"Похоже, вы ввели неверный тип данных: \n{err}")
else:
    print(first_task(*input_from_user))
"""

# Если самостоятельно:
for_func_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 65]
print(first_task(*for_func_list))
