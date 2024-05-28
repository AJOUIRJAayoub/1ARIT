import tkinter as tk
from tkinter import filedialog, messagebox
from logique.chiffrement import Chiffrement

class Interface:
    def __init__(self, test):
        self.test = test

    def read_and_display_cylinders(self):
        filename = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=(("Fichiers texte", "*.txt"),))
        if filename:
            with open(filename, 'r') as file:
                content = file.read()
            messagebox.showinfo("Contenu du fichier", content)

    def generate_new_dictionary(self):
        filename = "ressources/dictionnaire.txt"
        num_lines = 26  # Nombre de lignes dans le dictionnaire (26 pour l'alphabet)
        Chiffrement.generate_random_lines(filename, num_lines)
        messagebox.showinfo("Nouveau dictionnaire", "Le dictionnaire a été régénéré avec succès.")

    def regenerate_dictionary(self):
        num_lines = int(self.entry_num_lines.get())
        filename = "ressources/dictionnaire.txt"
        Chiffrement.generate_random_lines(filename, num_lines)
        messagebox.showinfo("Nouveau dictionnaire", "Le dictionnaire a été régénéré avec succès.")

    def encrypt_message(self):
        message = self.entry_message.get()
        key = self.entry_key.get()

        if not key:
            messagebox.showerror("Erreur", "Veuillez saisir une clé de chiffrement.")
            return

        key_list = []
        try:
            key_parts = key.split()
            for part in key_parts:
                key_list.append(int(part))
        except ValueError:
            messagebox.showerror("Erreur", "La clé de chiffrement doit être une séquence de nombres.")
            return

        encrypted_message = Chiffrement.jefferson_encrypt(message, self.test, key_list)
        messagebox.showinfo("Message chiffré", encrypted_message)

    def decrypt_message(self):
        ciphertext = self.entry_ciphertext.get()
        key = self.entry_key.get()

        if not key:
            messagebox.showerror("Erreur", "Veuillez saisir une clé de chiffrement.")
            return

        key_list = []
        try:
            key_parts = key.split()
            for part in key_parts:
                key_list.append(int(part))
        except ValueError:
            messagebox.showerror("Erreur", "La clé de chiffrement doit être une séquence de nombres.")
            return

        decrypted_message = Chiffrement.jefferson_decrypt(ciphertext, self.test, key_list)
        messagebox.showinfo("Message déchiffré", decrypted_message)

    def create_interface(self):
        # Création de l'interface graphique Tkinter
        window = tk.Tk()
        window.title("Chiffrement de Jefferson")

        button_open_file = tk.Button(window, text="Ouvrir un fichier", command=self.read_and_display_cylinders)
        button_generate_dictionary = tk.Button(window, text="Régénérer le dictionnaire", command=self.generate_new_dictionary)

        label_num_lines = tk.Label(window, text="Nombre de lignes dans le dictionnaire:")
        self.entry_num_lines = tk.Entry(window)

        label_num_lines.pack()
        self.entry_num_lines.pack()

        button_generate_dictionary = tk.Button(window, text="Régénérer le dictionnaire", command=self.regenerate_dictionary)
        button_generate_dictionary.pack()

        label_message = tk.Label(window, text="Message:")
        self.entry_message = tk.Entry(window)

        label_ciphertext = tk.Label(window, text="Texte chiffré:")
        self.entry_ciphertext = tk.Entry(window)

        label_key = tk.Label(window, text="Clé de chiffrement:")
        self.entry_key = tk.Entry(window)

        button_encrypt = tk.Button(window, text="Chiffrer", command=self.encrypt_message)
        button_decrypt = tk.Button(window, text="Déchiffrer", command=self.decrypt_message)

        # Placement des widgets dans la fenêtre
        button_open_file.pack()
        label_message.pack()
        self.entry_message.pack()
        label_ciphertext.pack()
        self.entry_ciphertext.pack()
        label_key.pack()
        self.entry_key.pack()
        button_encrypt.pack()
        button_decrypt.pack()

        # Lancement de la boucle principale de l'interface graphique
        window.mainloop()
