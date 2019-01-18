"""
Defines strategies for moves order.
Author: Emilija Zdilar on 05-05-2018
"""
from typing import List, Tuple
from constants import *
import random


def parity(coordinate: Tuple[int, int]) -> int:
    """
    Parity is defined as a sum of row and column where the coordinate is located.
    Args:
        coordinate: field

    Returns: parity as defined above

    """

    return (coordinate[0] + coordinate[1]) % 2


def smart_ai_moves_order() -> List[Tuple[int, int]]:
    """
    A method that shuffles the list of moves and sorts the new list by parity. The
    idea behind is that every ship is of length at least two, so it takes at least
    one field of each parity on the board. That way, AI needs to aim less fields to
    hit a ship.
    Returns: new moves order

    """

    rows = list(range(0, BOARD_HEIGHT))
    columns = list(range(0, BOARD_WIDTH))
    random.shuffle(columns)
    random.shuffle(rows)
    moves_order = [(x, y) for x in rows for y in columns]
    random.shuffle(moves_order)
    moves_order.sort(key=parity)
    return moves_order


def not_so_smart_ai_moves_order() -> List[Tuple[int, int]]:
    """
    A method that shuffles the list of moves and sorts the new list by parity. The

    Returns: new moves order

    """
    rows = list(range(0, BOARD_HEIGHT))
    columns = list(range(0, BOARD_WIDTH))
    random.shuffle(columns)
    random.shuffle(rows)
    moves_order = [(x, y) for x in rows for y in columns]
    random.shuffle(moves_order)
    return moves_order
