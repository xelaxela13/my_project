def check_len_and_dot(x):
    return len(x) == 1 and '.' not in x


def horizontal(game_result):
    for row in game_result:
        x = set(row)
        if check_len_and_dot(x):
            return True, x.pop()
    return False, 'D'


def diagonal_left(game_result):
    x = set(r[i] for i, r in enumerate(game_result))
    return (True, x.pop()) if check_len_and_dot(x) else (False, 'D')


def diagonal_right(game_result):
    x = set(r[-i - 1] for i, r in enumerate(game_result))
    return (True, x.pop()) if check_len_and_dot(x) else (False, 'D')


def vertical(game_result):
    for i, row in enumerate(game_result):
        x = set(r[i] for r in game_result)
        if check_len_and_dot(x):
            return True, x.pop()
    return False, 'D'


def checkio(game_result: list[str]) -> str:
    h, hr = horizontal(game_result)
    dl, dlr = diagonal_left(game_result)
    dr, drr = diagonal_right(game_result)
    v, vr = vertical(game_result)
    return h and hr or dl and dlr or dr and drr or v and vr or vr


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
