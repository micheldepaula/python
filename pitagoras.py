import argparse
import math

def calcular_catetos(c):
    try:
        c2 = c**2
        resultados = [
            (a, b)
            for a in range(1, int(c))
            for b in range(a, int(c))  # b >= a para evitar repetições invertidas
            if math.isclose(a**2 + b**2, c2)
        ]
        
        if not resultados:
            print(f"Nenhum par inteiro (a, b) encontrado para c = {c}")
        else:
            for a, b in resultados:
                print(f"a = {a}, b = {b}, c = {c:.2f}")
        return resultados

    except Exception as e:
        print(f"Erro: {e}")

def main():
    parser = argparse.ArgumentParser(description="Calcula lados do triângulo retângulo a partir da hipotenusa.")
    parser.add_argument('--c', type=float, default=None, help="Hipotenusa (c)")
    parser.add_argument('--a', type=float, default=None, help="Cateto a")
    parser.add_argument('--b', type=float, default=None, help="Cateto b")

    args = parser.parse_args()

    fornecidos = sum(x is not None for x in [args.a, args.b, args.c])

    # Escolha da função com base nos argumentos (sem if usando dict)
    funcoes = {
        1: lambda: calcular_catetos(args.c),
        2: lambda: pitagoras(a=args.a, b=args.b, c=args.c)
    }

    funcoes.get(fornecidos, lambda: print("Informe a hipotenusa (c), ou dois lados."))()

def pitagoras(a=None, b=None, c=None):
    lados = {'a': a, 'b': b, 'c': c}
    fornecidos = list(filter(lambda x: x[1] is not None, lados.items()))
    faltantes = list(filter(lambda x: x[1] is None, lados.items()))

    try:
        assert len(fornecidos) == 2 and len(faltantes) == 1
        nomes_forn, valores_forn = zip(*fornecidos)
        faltando = faltantes[0][0]

        calcular = {
            'c': lambda x, y: math.sqrt(x**2 + y**2),
            'a': lambda x, y: math.sqrt(y**2 - x**2),
            'b': lambda x, y: math.sqrt(y**2 - x**2),
        }

        resultado = calcular[faltando](*valores_forn)
        print(f"{faltando} = {resultado:.2f}")
        return resultado

    except Exception:
        print("Erro: informe dois lados válidos.")

if __name__ == "__main__":
    main()
