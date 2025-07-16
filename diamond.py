import argparse
import string

def gen_line(i, target_index):
    letter = string.ascii_uppercase[i]
    outer = abs(target_index - i)
    inner = (i * 2 - 1)

    compose = {
        0: lambda: f"{'_' * outer}{letter}{'_' * outer}",
        1: lambda: f"{'_' * outer}{letter}{'_' * inner}{letter}{'_' * outer}"
    }

    return compose[i > 0]()  # usa 1 se i > 0, senão usa 0

def diamond(letter):
    letter = letter.upper()
    index = string.ascii_uppercase.index(letter)

    top = [gen_line(i, index) for i in range(index + 1)]
    bottom = top[:-1][::-1]
    return "\n".join(top + bottom)

def main():
    parser = argparse.ArgumentParser(description="Diamond Kata com underscores.")
    parser.add_argument("--letter", type=str, required=True, help="Letra final do losango (A-Z)")
    args = parser.parse_args()

    print(diamond(args.letter))

if __name__ == "__main__":
    main()
