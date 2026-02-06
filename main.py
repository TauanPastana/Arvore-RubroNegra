# main.py
from RBTree import RBTree

if __name__ == "__main__":
    arvore = RBTree()

    for v in (2, 1, 4, 3, 5, 6, 7):
        arvore.insert(v)

    print("\nÁrvore (estrutura):")
    print(arvore)

    arvore.remover(4)

    print("\nÁrvore Rubro-Negra (em ordem):")
    print("Valor\tCor")
    print("-" * 20)
    print(arvore)
