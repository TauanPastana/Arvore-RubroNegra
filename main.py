# main.py
from RBTree import RBTree

if __name__ == "__main__":
    arvore = RBTree()

    for v in (11,2,14,1,7,5,8,13):
        arvore.insert(v)

    print("\nÁrvore Rubro-Negra: antes")
    print("Valor\tCor")
    print("-" * 20)
    print(arvore)

    print("remover 13")
    arvore.remover(13)
    print(arvore)

    print("remover 14")
    arvore.insert(13)
    arvore.remover(14)
    print(arvore)

    print("remover 1")
    arvore.remover(1)
    print(arvore)

    print("\nÁrvore Rubro-Negra :Depois")
    print("Valor\tCor")
    print("-" * 20)
    print(arvore)
