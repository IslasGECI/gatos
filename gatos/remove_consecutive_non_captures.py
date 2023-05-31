from itertools import groupby
from operator import itemgetter


def split_non_consecutive_indexes(index_list):
    return [
        list(map(itemgetter(1), g))
        for k, g in groupby(enumerate(index_list), lambda i_x: i_x[0] - i_x[1])
    ]


def get_non_captures_index(data):
    return data.index[data.Capturas == 0].to_list()
