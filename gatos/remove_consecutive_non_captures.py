from itertools import groupby
from operator import itemgetter


def get_last_cumsum(singular_data, index_list):
    return singular_data.loc[index_list].cumsum().iloc[-1]


def split_non_consecutive_indexes(index_list):
    return [
        list(map(itemgetter(1), g))
        for k, g in groupby(enumerate(index_list), lambda i_x: i_x[0] - i_x[1])
    ]


def get_non_captures_index(data):
    return data.index[data.Capturas == 0].to_list()


def drop_unused_non_captures(data, non_captures_indexes):
    return data.drop(non_captures_indexes[:-1])
