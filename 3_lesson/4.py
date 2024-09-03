str = "hhhabchghhh"
new_str = str.replace('h', 'H', str.count('h')-1).replace('H', 'h', 1)
print(new_str)
