from interface.interface import Interface
from logique.chiffrement import Chiffrement

# Lecture du dictionnaire et création de la liste de test
filename = "ressources/dictionnaire.txt"
result_dict = Chiffrement.read_file_and_create_dictionary(filename)

test = []
for i in range(1, len(result_dict) + 1):
    test.append(result_dict[i])

# Création de l'interface graphique avec la liste de test
interface = Interface(test)
interface.create_interface()

