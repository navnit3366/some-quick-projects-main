import os

from helpers_general import get_basic_file_data, get_path_from_user, read_folder, get_pdf_data

import sys

sys.path.append('./')


def test_size_min(size: int, size_min: int):
    if size > size_min:
        return 1
    else:
        return 0


def test_size_max(size: int, size_max: int):
    if size < size_max:
        return 1
    else:
        return 0


def test_special_chars(filename: str, liste_chars: list):
    score = 0
    for char in liste_chars:
        if char.lower() in filename.lower():
            score += 1
    return score / len(liste_chars)


def test_nb_page_max(nb_pages: int, nb_pages_max: int):
    if nb_pages < nb_pages_max:
        return 1
    else:
        return 0


def test_nb_page_min(nb_pages: int, nb_pages_min: int):
    if nb_pages < nb_pages_min:
        return 1
    else:
        return 0


def test_extension(extension: str, liste_ext: list):
    '''
    input 
        - extension: str
            - examples: "pdf", "pptx", ....
        - liste_ext:list<str>
            - examples: ["pdf", "pptx"]
    '''
    if extension in liste_ext:
        return 1
    else:
        return 0


def CCTP(path,
         taille_fichier_min=None,
         taille_fichier_max=None,
         nb_page_min=None,
         nb_page_max=None,
         mots_cles=["tp", "cc"],
         extensions_possibles=['pdf', 'docx', 'docm']):

    print("\n>>>>>>file_path = ", path)

    criterion_data = {}

    # get all data about the file without opening it
    basic_data = get_basic_file_data(filepath=path)

    # store these data into variables
    filepath = basic_data["filepath"]
    filename = basic_data["filename"]
    extension = basic_data["extension"]
    kb_size = int(basic_data["kb_size"])
    last_modification_date = basic_data["last_modification_date"]
    creation_date = basic_data["creation_date"]

    print("data found = ", basic_data)

    # change format for filepath
    #print(f"\n changing filepath from {path} to {filepath}")
    path = filepath

    # add score to criterion data
    # test extention
    if extensions_possibles:
        criterion_data["extension"] = test_extension(
            extension=extension, liste_ext=extensions_possibles)
        # test_size_min
    if taille_fichier_min != None:
        criterion_data["size_min"] = test_size_min(size=kb_size,
                                                   size_min=taille_fichier_min)
        # test_size_max
    if taille_fichier_max != None:
        criterion_data["size_max"] = test_size_max(size=kb_size,
                                                   size_max=taille_fichier_max)
    if mots_cles:
        criterion_data["special_chars"] = test_special_chars(
            filename=filename, liste_chars=mots_cles)

    print(f"\n criterion_data v1 = {criterion_data}")

    if "pdf" in extension:
        pdf_data = get_pdf_data(path)
        nb_pages = pdf_data["nb_pages"]
        raw_txt = pdf_data["raw_txt"]

        if nb_page_min:
            criterion_data["nb_page_min"] = test_nb_page_min(
                nb_pages=nb_pages, nb_pages_min=nb_page_min)
        if nb_page_max:
            criterion_data["nb_page_max"] = test_nb_page_max(
                nb_pages=nb_pages, nb_pages_max=nb_page_max)

        print(f"\n criterion_data v2 = {criterion_data}")

    return criterion_data


if __name__ == '__main__':
    print("\n>>> test criterion_data")
    folder = get_path_from_user()
    liste_path = read_folder(folder)
    for path in liste_path:
        criterion_data = CCTP(path,
                              taille_fichier_min=20,
                              taille_fichier_max=300,
                              nb_page_min=3,
                              nb_page_max=17,
                              mots_cles=["tp", "cc"],
                              extensions_possibles=['pdf', 'docx', 'docm'])
