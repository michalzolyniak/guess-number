from random import randrange


def draw_number(start, end):
    """
    :param start: int begging of range to draw
    :param end:  int end of range to draw
    :return: int drawn number between start and end
    """
    return randrange(start, end)
