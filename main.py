from RBTree import RBTree


arvore = RBTree()




arvore.insert(5, arvore.root)
arvore.insert(4, arvore.root)
arvore.insert(7, arvore.root)
arvore.insert(8, arvore.root)
arvore.insert(3, arvore.root)
arvore.insert(9, arvore.root)
arvore.insert(12, arvore.root)



print("\nÁrvore Rubro-Negra (em ordem):")
print("Valor\tCor")
print("-" * 20)
print(arvore)
