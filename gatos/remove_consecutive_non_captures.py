def get_non_captures_index(data):
    return data.index[data.Capturas == 0].to_list()
