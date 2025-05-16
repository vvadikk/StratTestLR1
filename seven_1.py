def dec_to_string_bin(d):
    if d == 0:
        return '0'
    b = ''
    while d > 0:
        b = str(d % 2) + b
        d //= 2
    return b
def string_bin_to_dec(b):
    d = 0
    for i in range(len(b)):
        d += int(b[i]) * 2 ** (len(b) - i - 1)
    return d
def dec_to_string_hex(d):
    hex_digits = '0123456789ABCDEF'
    if d == 0:
        return '0'
    h = ''
    while d > 0:
        h = hex_digits[d % 16] + h
        d //= 16
    return h
def string_hex_to_dec(h):
    hex_digits = '0123456789ABCDEF'
    d = 0
    for i in range(len(h)):
        d += hex_digits.find(h[i]) * 16 ** (len(h) - i - 1)
    return d