from typing import Any


def task_four(string_array: list) -> tuple[list[Any], list[Any]]:
    """сортирует список строк по длине, сначала по возрастанию, а затем по убыванию"""
    list_sorted_positive = sorted(string_array, key=lambda string: len(string))
    list_sorted_negative = sorted(string_array, key=lambda string: -len(string))
    return list_sorted_positive, list_sorted_negative


list_for_input = ["123", "1234", "12345", "123456"]
positive_list, negative_list = task_four(list_for_input)
print(f" {positive_list} - Сортировка по возрастания \n {negative_list} - Сортировка по убыванию")
