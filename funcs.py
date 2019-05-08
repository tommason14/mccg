def get_coords():
    
    file = """\
    C  13.456 12.321 13.054
    H  11.222 12.542 10.342
    H  10.321  9.896  5.341
    O   3.451  5.759  4.531
    N   8.421  9.582 10.888"""
    
    return file.split('\n')

def get_atomic_number(symbol):

    atnums = {}
    atnums['C'] = 6.0
    atnums['H'] = 1.0
    atnums['N'] = 7.0
    atnums['O'] = 8.0

    return atnums[symbol]    

def add_atomic_number(line):
    
    sym, x, y, z = line.split()
    atnum = get_atomic_number(sym) 
    return f"{sym:<2} {atnum:<4} {x:<6} {y:<6} {z:<6}\n"

def modify_coords(coords):
    new_coords = []
    for line in coords:
        line = add_atomic_number(line)
        new_coords.append(line)
    return new_coords

def print_file(file):
    print(''.join(file))

def main():
    coords = get_coords()
    new_coords = modify_coords(coords)
    print_file(new_coords)

main()

Output:
C  6.0  13.456 12.321 13.054
H  1.0  11.222 12.542 10.342
H  1.0  10.321 9.896  5.341 
O  8.0  3.451  5.759  4.531 
N  7.0  8.421  9.582  10.888
