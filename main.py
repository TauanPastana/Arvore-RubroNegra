from RBTree import RBTree

# Criar uma árvore rubro-negra
arvore = RBTree()

# Inserir alguns valores para teste
print("Inserindo valores na árvore...")
valores = [5,3,6,2,8,9,1,]


arvore.insert(5, arvore.root)
arvore.insert(4, arvore.root)
arvore.insert(7, arvore.root)
arvore.insert(8, arvore.root)
arvore.insert(3, arvore.root)
arvore.insert(9, arvore.root)
arvore.insert(12, arvore.root)


# Exibir a árvore em ordem (in-order traversal)
print("\nÁrvore Rubro-Negra (em ordem):")
print("Valor\tCor")
print("-" * 20)
print(arvore)
