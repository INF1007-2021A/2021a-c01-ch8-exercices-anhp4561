#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}
## Moi
# # TODO: Importez vos modules ici
# import pickle
# from recettes import*
#
# # TODO: Définissez vos fonction ici
# def fonction_1():
#     with open("exemple.txt","r", encoding="utf-8") as f:
#         text1=(f.read())
#         with open("exemple2.txt", "r", encoding="utf-8") as g:
#             text2 = (g.read())
#             for i in range(len(text1)):
#                 if text1[i]!= text2[i]:
#                     print(f"Il y a une difference au {i+1}eme caractere : {text1[i]} != {text2[i]}")
#
# def fonction_2():
#     with open("exemple _test.txt", "r+", encoding="utf-8") as f:
#         text = f.read()
#         text_split = text.split()
#         print (text_split)
#         "   ".join(text_split)
#         print(text_split)
#
# def fonction_recette(cook_book):
#     choix = input("""Choississez une option:
#                         a) Ajouter une recette
#                         b) Modifier une recette
#                         c) Supprimer une recette
#                         d) Afficher une recette
#                         e) Quitter le programme
#         Votre option : \n""")
#
#     if choix == "a":
#         add_recipes(cook_book)
#         pickle.dump(cook_book,open("recette.p","wb"))
#         return fonction_recette(cook_book)
#     elif choix == "b":
#         recipe_name = input("Entrez le nom de la recette que vous voulez modifier : ")
#         ingredients_v2 = input("Entrez à nouveau la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ',' : ")
#         cook_book[recipe_name] = ingredients_v2
#         pickle.dump(cook_book, open("recette.p", "wb"))
#         return fonction_recette(cook_book)
#     elif choix == "c":
#         del_recipe_name = input("Entrez le nom de la recette que vous voulez supprimer : ")
#         del cook_book[del_recipe_name]
#         pickle.dump(cook_book, open("recette.p", "wb"))
#         return fonction_recette(cook_book)
#     elif choix == "d":
#         livre_de_recette = pickle.load(open("recette.p", "rb"))
#         print_recipe(livre_de_recette)
#         return fonction_recette(cook_book)
#     elif choix == "e":
#         return cook_book
#     else :
#         print ("Cette option n'existe pas. Essayez encore.")
#         return fonction_recette(cook_book)
#
# def fonction_5():
#     with open("exemple.txt","r", encoding="utf-8") as f:
#         text1=(f.read())
#         print (text1)
#         number_counter = {}
#         for i in text1: # tres inefficace, devrait trouver une meilleur facon
#             if i.isnumeric():
#                 number_counter[i] = 0
#         for i in text1:
#             if i.isnumeric():
#                 number_counter[i] += 1
#     return number_counter

## version prof
def exercice1(file_path1,file_path2):
    with open(file_path1,encoding="utf-8") as f1, open(file_path2,encoding="utf-8") as f2:
        if len(f1.readlines()) != len(f2.readlines()):
            print("The files don't have the same length")
        else:
            f1.seek(0)
            f2.seek(0)
            for count, line_f1 in enumerate (f1):
                line_f2=f2.readline()
                if line_f1 != line_f2:
                    print ("The files are not identical ...")
                    return
    print ("The files are identical")
    return
def exercice2(file_path1,file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2,"w", encoding="utf-8") as f2:
        f2.write(f1.read().replace("","   "))

def exercice3(note_path,result_path):
    with open(note_path, encoding="utf-8") as note_file:
        notes_percent = note_file.readlines()
    with open(result_path,"w",encoding="utf-8") as result_file:
        for note in notes_percent:
            for key,value in PERCENTAGE_TO_LETTER.items():
                if value[0]<= int(note.strip()) < value[1]:
                    result_file.write(note.strip()+""+key+"\n")
                    break

def exercice5(file_path):
    with open(file_path,encoding="utf-8")as f:
        words = f.read().strip().split()
        numbers = [int(w) for w in words if w.isnumeric()]

    return sorted(numbers)

def exercice6(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        for index, line in enumerate(f1):
            if not index %2 :
                f2.write(line)


if __name__ == '__main__':
    ## moi
    # # TODO: Appelez vos fonctions ici
    # fonction_1()
    # fonction_2()
    # # Exercice 4
    # cook_book = pickle.load(open("recette.p", "rb"))
    # fonction_recette(cook_book)
    # print(fonction_5())

    ## version prof
    exercice1("./exemple.txt", "./exemple.txt") # ./ veut dire du repertoire courant chercher ...
    exercice2("./exemple.txt", "./exemple3.txt")
    exercice3("./notes.txt","./result.txt")
    print (exercice5("./exemple.txt"))
    exercice6("./exemple.txt", "./exemple4.txt")