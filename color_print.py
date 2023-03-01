# based on https://stackabuse.com/how-to-print-colored-text-in-python/

def print_scheme(line_down : int = 24):
    print(
        "".join(f"\033[38;5;{x}m{str(x).ljust(5, ' ')}" + ('\n' if (x + 1) % line_down == 0 else "") 
                for x in range(0, 256))
    )
    print('\033[0;0m')

red = 196
green = 46
blue = 33
yellow = 11
black = 0

def get_colored(value : str, text_color : int = None, back_color : int = None):
    return (((f"\033[38;5;{text_color}m" if text_color else "") +
             (f"\033[48;5;{back_color}m" if back_color else "")) 
             + value + '\033[0;0m')

def print_colored(value : str, text_color : int = None, back_color : int = None, end = '\n'):
    print(get_colored(value, text_color, back_color), end=end)

#print_scheme()