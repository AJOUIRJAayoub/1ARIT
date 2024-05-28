import random

class Chiffrement:
    @staticmethod
    def Chaine_alphabet():
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(alphabet)
        return ''.join(alphabet)

    @staticmethod
    def generate_random_lines(filename, num_lines):
        with open(filename, 'w') as file:
            for _ in range(num_lines):
                random_line = Chiffrement.Chaine_alphabet()
                file.write(random_line + '\n')

    @staticmethod
    def read_file_and_create_dictionary(filename):
        dictionary = {}
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)

            for i in range(num_lines):
                line = lines[i].strip()
                dictionary[i + 1] = line

        return dictionary

    @staticmethod
    def is_permutation(lst=None, n=None):
        if lst is None:
            lst = list(range(1, n + 1))
        else:
            n = len(lst)
        expected_set = set(range(1, n + 1))
        lst_set = set(lst)
        return len(lst) == len(expected_set) and lst_set == expected_set

    @staticmethod
    def generate_new_key(n):
        permutation = list(range(1, n + 1))
        random.shuffle(permutation)
        return permutation

    @staticmethod
    def check_and_generate_key(lst):
        if Chiffrement.is_permutation(lst):
            n = len(lst)
            new_key = Chiffrement.generate_new_key(n)
            return new_key
        else:
            return None

    @staticmethod
    def jefferson_encrypt(message, test, key):
        ciphertext = ""
        i = 0
        for char in message:
            liste = ""
            if char.isalpha():
                liste = test[i]
                for index, char1 in enumerate(liste):
                    if char1 == char:
                        position = index + 1 + int(key[i])
                        encrypted_char = liste[position % 26]
                        ciphertext += encrypted_char
                        break
            else:
                ciphertext += char
            i = (i + 1) % len(test)
        return ciphertext

    @staticmethod
    def jefferson_decrypt(ciphertext, test, key):
        plaintext = ""
        i = 0
        for char in ciphertext:
            if char.isalpha():
                liste = test[i]
                for index, char1 in enumerate(liste):
                    if char1 == char:
                        position = index - key[i] - 1
                        decrypted_char = liste[position % 26]
                        plaintext += decrypted_char
                        break
            else:
                plaintext += char
            i = (i + 1) % len(test)
        return plaintext
