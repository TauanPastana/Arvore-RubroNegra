from RBTree import RBTree


arvore = RBTree()




# arvore.insert(2, arvore.root)
# arvore.insert(1, arvore.root)
# arvore.insert(4, arvore.root)
# arvore.insert(3, arvore.root)
# arvore.insert(5, arvore.root)
# arvore.insert(6, arvore.root)
# arvore.insert(7, arvore.root)
arvore.insert(4, arvore.root)
arvore.insert(5, arvore.root)
arvore.insert(6, arvore.root)
# arvore.insert(0, arvore.root)
# arvore.insert(1, arvore.root)
# arvore.insert(6, arvore.root)
# arvore.insert(7, arvore.root)



print("Raiz:", arvore.root.key, "cor:", "B" if arvore.root.color else "R")
print("Esq da raiz:", arvore.root.left.key if arvore.root.left else None)
print("Dir da raiz:", arvore.root.right.key if arvore.root.right else None)
print(arvore)

print("\nÁrvore Rubro-Negra (em ordem):")
print("Valor\tCor")
print("-" * 20)
print(arvore)
