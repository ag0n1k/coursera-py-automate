from automate.sum_and_divide_click import logic


def test_logic():
    assert logic([1.1, 2.4]) == 3
    assert logic([1.6, 1.2, 2.1, 1.5]) == 3
    assert logic([1, 1, 1, 1, 1]) == 4
    assert logic([0, 0, 0, 0, 0, 0]) == 0
    assert logic([1, 1, 1, 1, 1, 1, 1, 6, 1]) == 2

    assert logic([1, 1], twice=True) == 4
    assert logic([1, 1, 1, 1], twice=True) == 6
    assert logic([1, 1, 1, 2], twice=True) == 1
    assert logic([1, 1, 1, 2, 1], twice=True) == 3
