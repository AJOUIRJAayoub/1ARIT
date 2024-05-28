Ce MINI-PROJET est une application de chiffrement et déchiffrement de messages utilisant la méthode du Cylindre de Jefferson. Il permet de chiffrer et déchiffrer des messages en utilisant cette technique historique de chiffrement.




- Structure du projet

Le projet est structuré comme ceçi :



                 1ARIT-AYOUB/
                     ├── logique/
                     │   ├── chiffrement.py
                     │   
                     ├── interface/
                     │   ├── interface.py
                     │  
                     ├── ressources/
                     │   └── dictionnaire.txt
                     └── main.py


- Le dossier logique contient le module chiffrement.py qui implémente les fonctions de chiffrement et de déchiffrement utilisées dans l'application.

- Le dossier interface contient le module interface.py qui gère l'interface graphique de l'application.

- Le dossier ressources contient le fichier dictionnaire.txt qui est utilisé comme dictionnaire pour le chiffrement de Jefferson.

- Le fichier main.py est le point d'entrée du programme.




- Prérequis :

Avant d'exécuter l'application, assurez-vous d'avoir Python installé sur votre système.





- Installation et exécution :

1. Clonez ou téléchargez ce dépôt sur votre machine.

2. Ouvrez une console ou un terminal et placez-vous dans le répertoire racine du projet 1ARIT-AYOUB.

3. Installez les dépendances en exécutant la commande suivante :
             
                pip install -r requirements.txt


4. Pour lancer l'interface graphique, exécutez le fichier main.py avec la commande suivante :

                python main.py

5. L'interface graphique de l'application s'ouvrira, vous permettant de chiffrer et déchiffrer des messages en utilisant le chiffrement de Jefferson.




Fonctionnalités : 



- Chiffrement de messages en utilisant la méthode de chiffrement de Jefferson.

- Déchiffrement de messages chiffrés avec la méthode de chiffrement de Jefferson.

- Possibilité d'ouvrir un fichier texte contenant des cylindres pour afficher son contenu.

- Régénération du dictionnaire utilisé pour le chiffrement avec un nombre spécifié de lignes.




