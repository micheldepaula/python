import argparse
import math

def pitagoras(a=None, b=None, c=None):
    lados = {'a': a, 'b': b, 'c': c}

    # Descobre os lados fornecidos e o faltante
    fornecidos = list(filter(lambda x: x[1] is not None, lados.items()))
    faltantes = list(filter(lambda x: x[1] is None, lados.items()))

    try:
        # Deve haver exatamente dois lados fornecidos e um faltando
        assert len(fornecidos) == 2 and len(faltantes) == 1

        # Extrai nomes e valores dos lados 
        nomes_forn, valores_forn = zip(*fornecidos)
        faltando = faltantes[0][0]

        # Tabela de calculo 
        calcular = {
            'c': lambda x, y: math.sqrt(x**2 + y**2),
            'a': lambda x, y: math.sqrt(y**2 - x**2),
            'b': lambda x, y: math.sqrt(y**2 - x**2),
        }

        resultado = calcular[faltando](*valores_forn)
        print(f"{faltando} = {resultado:.2f}")
        return resultado

    except (AssertionError, ValueError):
        print("Erro: informe exatamente dois lados válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Calculadora do Teorema de Pitágoras. Informe dois lados (a, b ou c) e o terceiro será calculado."
    )

    parser.add_argument('--a', type=float, default=None, help="Cateto a")
    parser.add_argument('--b', type=float, default=None, help="Cateto b")
    parser.add_argument('--c', type=float, default=None, help="Hipotenusa c")

    args = parser.parse_args()
    pitagoras(a=args.a, b=args.b, c=args.c)

if __name__ == "__main__":
    main()
