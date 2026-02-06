# main.py
from RBTree import RBTree

if __name__ == "__main__":
    arvore = RBTree()

    for v in (10, 5, 15, 3, 7, 6):
        arvore.insert(v)

    print("\nÁrvore Rubro-Negra: antes")
    print("Valor\tCor")
    print("-" * 20)
    print(arvore)

    arvore.remover(5)

    print("\nÁrvore Rubro-Negra :Depois")
    print("Valor\tCor")
    print("-" * 20)
    print(arvore)
