from seven_1 import dec_to_string_bin, dec_to_string_hex, string_bin_to_dec, string_hex_to_dec
dec1 = 712975
dec2 = 206
sb = '1000101110110101011'
sh = 'CB692'
print(f'{dec2} = {dec_to_string_bin(dec2)}_2')
print(f'{dec1} = {dec_to_string_hex(dec1)}_16')
print(f'{sb} = {string_bin_to_dec(sb)}')
print(f'{sh} = {string_hex_to_dec(sh)}')