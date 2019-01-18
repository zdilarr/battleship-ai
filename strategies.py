from constants import *
import random

def Parity (coordinate):
    """
    paritet definiran kao suma reda i kolone u kojoj se nalazi,
    po modulu 2.
    :param coordinate:
    :return:
    """
    return (coordinate[0] + coordinate[1]) % 2

def smart_ai_moves_order():
    """
    nasumicno izmjesa poteze i sortira takve poteze po paritetu.
    Ideja je u tome da svaki brod zauzima bar po jedno polje razlicitog pariteta,
    pa treba ciljati manje nasumicnih polja da se dodje do pogotka.
    :return:
    """
    rows = list(range(0, BOARDHEIGHT))
    columns = list(range(0, BOARDWIDTH))
    random.shuffle(columns)
    random.shuffle(rows)
    moves_order = [(x, y) for x in rows for y in columns]
    random.shuffle(moves_order)
    moves_order.sort(key=Parity)
    return moves_order


def not_so_smart_ai_moves_order():
    """
    nasumicno izmjesa moguce poteze
    :return:
    """
    rows = list(range(0, BOARDHEIGHT))
    columns = list(range(0, BOARDWIDTH))
    random.shuffle(columns)
    random.shuffle(rows)
    moves_order = [(x, y) for x in rows for y in columns]
    random.shuffle(moves_order)
    return moves_order
