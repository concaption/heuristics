from greedy_coin import greedy_coin


def test_greedy_coin():
    assert greedy_coin(0.67) == {0.25: 2, 0.10: 1, 0.05: 1, 0.01: 2}
    assert greedy_coin(0.99) == {0.25: 3, 0.10: 2, 0.05: 0, 0.01: 4}
