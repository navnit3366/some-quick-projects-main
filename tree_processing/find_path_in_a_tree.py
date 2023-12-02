###########################################################
#### project: find path between two points of any tree ####
################# Author: Hermann Agossou #################
###########################################################

############# functions to adapt #############

def get_all_foreigners(tree, point) -> list:
    '''retourne pour un point, la liste de ses voisins'''
    return tree.get(point) or []

def foundEltInList(point, list_points:list) -> bool:
    '''verifier si un point est bien dans la liste de points'''
    return point in list_points

def check_equality(point1, point2) -> bool:
    '''verifier si deux points sont égaux'''
    return point1==point2

def remove_duplicates(list_foreigners:list) -> list:
    '''enlever les points qui se répètent'''
    return list(set(list_foreigners))

def remove_used_point(list_foreigners:list, points_to_remove:list) -> list:
    '''enlever les points déjà parcourus'''
    return list(set(list_foreigners) - set(points_to_remove))

############# fin #############



############# fonction without adaptation #############

def get_selected_foreigners(tree, current_point, used_points):
    '''pour un point, trouver les voisins et trier'''
    list_foreigners = get_all_foreigners(tree, current_point)
    list_foreigners = remove_duplicates(list_foreigners)
    list_foreigners = remove_used_point(list_foreigners, used_points) #curentpoint aussi car il est dans usedpoint
    return list_foreigners

def initialisation(path, current_point, used_points) -> tuple[list, list]:
    print("\ncurrent_point = ",current_point)
    print("   path = ",path)
    if path is None: path = [current_point]
    if used_points is None: used_points = []
    used_points.append(current_point)
    return path, used_points

def recursive_call(tree, list_foreigners, destination, used_points, path):
    '''call find_first_path_to_destination'''
    for foreigner in list_foreigners:
        pathFound = find_first_path_to_destination(tree=tree, current_point=foreigner, 
                                                  destination=destination, path=path + [foreigner], 
                                                  used_points=used_points
                                                  )
        #le premier chemin trouvé est retourné
        if pathFound: return pathFound


def find_first_path_to_destination(tree, current_point, destination, path:list=None, used_points:list=None):
    '''
    Exemple
    >>> tree = {1:[2,3,5,8], 2:[7,6,8,2,1], 7:[20,10], 6:[10,1]}
    >>> deb, fin = 1, 20
    >>> find_first_path_to_destination(tree, deb, fin)
    >>> [1, 2, 7, 20]
    '''
    #initialisation de l'algo
    path, used_points = initialisation(path, current_point, used_points)

    #si la destination est trouvée
    if check_equality(current_point, destination): 
        return path 
    
    #trouver les voisins et enlever ceux déjà parcourus
    list_foreigners = get_selected_foreigners(tree, current_point, used_points)    
    print("   list_foreigners = ",list_foreigners)
    
    #si il n'y a pas de voisins viables, on sort
    if not list_foreigners:
        print('   not found')
        return None
    
    # si la destination est trouvée, on sort
    if foundEltInList(destination, list_foreigners):
        print('   found')
        path.append(destination)
        return path
    
    #parcours du voisinage pour répéter l'opération
    print('   browse list_foreigners')
    return recursive_call(tree, list_foreigners, destination, used_points, path)


############# fin #############




if __name__=='__main__':
    tree = {1:[2,3,5,8], 2:[7,6,8,2,1], 7:[20,10], 6:[10,1]}
    deb, fin = 1, 20
    print(f"{deb} -> {fin}")
    path = find_first_path_to_destination(tree, deb, fin)
    print('\npath = ',' -> '.join(map(str, path)))
