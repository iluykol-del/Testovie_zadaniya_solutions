#Напишите функцию и автотесты к ней на любом языке программирования.
#Функция должна выполнять следующую задачу:
#Принимать массив чисел и возвращать новый массив, в котором удалены подряд идущие дубликаты.
#Например: [1, 1, 2, 2, 3] → [1, 2, 3] [0, 0, 1, 1, 0] → [0, 1, 0]

#Требования к решению

#Реализовать функцию compress_numbers (или аналогичное название на вашем языке).

#Написать набор автотестов, покрывающих различные случаи



#Решение
def delete_dubl(numbers: list[int]) -> list[int]:
    result = []

    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        elif num != numbers[i - 1]:
            result.append(num)

    return result




# Автотесты
from solution import delete_dubl


def test_pystoi_list():
    assert delete_dubl([]) == []


def test_odin_element():
    assert delete_dubl([1]) == [1]

def test_bez_dublikatov():
    assert delete_dubl([1, 2, 3]) == [1, 2, 3]

def test_vse_dublikaty():
    assert delete_dubl([1, 1, 2, 2, 3, 3]) == [1, 2, 3]


def test_duplikaty_v_nachale():
    assert delete_dubl([1, 1, 1, 2, 3]) == [1, 2, 3]

def test_duplikaty_v_konce():
    assert delete_dubl([1, 2, 3, 3, 3]) == [1, 2, 3]


def test_duplikaty_v_sredine():
    assert delete_dubl([1, 2, 2, 2, 3]) == [1, 2, 3]

def test_mnogie_duplikaty():
    assert delete_dubl([1, 1, 2, 3, 3, 2, 2, 1]) == [1, 2, 3, 2, 1]


def test_vse_elementy_odinakovie():
    assert delete_dubl([5, 5, 5, 5]) == [5]

def test_nuli():
    assert delete_dubl([0, 0, 1, 1, 0]) == [0, 1, 0]


def test_otricatelnye_chisla():
    assert delete_dubl([-1, -1, 0, 0, -1]) == [-1, 0, -1]