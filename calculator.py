def addition(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculatrice : addition de deux nombres")
    x = float(input("Entrez le premier nombre : "))
    y = float(input("Entrez le deuxième nombre : "))
    resultat = addition(x, y)
    print(f"Le résultat de {x} + {y} est {resultat}")

