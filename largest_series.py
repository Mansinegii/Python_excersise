def larger(data) :
    result = 1
    for x in data:
        result = result * int(x)
    return result
def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if not len(series) and size != 0:
        raise ValueError("span must be greater than zero")
    for x in series:
        if not x.isnumeric():
            raise ValueError("digits input must only contain digits")
    result = 0
    for x in range(0,len(series) - size + 1):
        f = larger(series[x:x+size])
        if f > result:
            result = f
    return result
