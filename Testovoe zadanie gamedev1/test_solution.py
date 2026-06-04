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