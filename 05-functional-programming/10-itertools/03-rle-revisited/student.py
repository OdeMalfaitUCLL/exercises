from itertools import groupby
def rle_encode(data):
    groups = (list(group) for _, group in groupby(data))
    return ((group[0],len(group)) for group in groups)


def rle_decode(data):
    return (datum for (datum,count) in data for _ in range(count))