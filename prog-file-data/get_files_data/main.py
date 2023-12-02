from cctp import CCTP
from helpers_general import get_path_from_user, read_folder

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
