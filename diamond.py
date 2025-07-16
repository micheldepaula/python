import argparse
import string

def gen_line(i, target_index):
    letter = string.ascii_uppercase[i]
    outer_spaces = abs(target_index - i)
    inner_spaces = (i * 2 - 1)

    compose = {
        0: lambda: f"{' ' * outer_spaces}{letter}{' ' * outer_spaces}",
        1: lambda: f"{' ' * outer_spaces}{letter}{' ' * inner_spaces}{letter}{' ' * outer_spaces}"
    }

    return compose[i > 0]()  # 0 or 1

def diamond(letter):
    letter = letter.upper()
    index = string.ascii_uppercase.index(letter)

    top = [gen_line(i, index) for i in range(index + 1)]
    bottom = top[:-1][::-1]  # espelha sem duplicar o meio
    return "\n".join(top + bottom)

def main():
    parser = argparse.ArgumentParser(description="Diamond Kata: imprime um losango com letras.")
    parser.add_argument("--letter", type=str, required=True, help="Letra do losango (A-Z)")

    args = parser.parse_args()
    print(diamond(args.letter))

if __name__ == "__main__":
    main()
