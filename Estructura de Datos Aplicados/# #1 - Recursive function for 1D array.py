# Recursive function to print all Personas in a 3D array
def print_personas(personas, i=0, j=0, k=0):
    if i < len(personas):  
        if j < len(personas[i]):  
            if k < len(personas[i][j]):  
                print(personas[i][j][k])  
                print_personas(personas, i, j, k + 1)  
            else:
                print_personas(personas, i, j + 1, 0)  
        else:
            print_personas(personas, i + 1, 0, 0)  

# Personas grouped by Arcana and Strength level
personas = [
    [["Orpheus", "Legion"], ["Odin", "Surt"]],  # Fool and Magician
    [["Sarasvati", "Ganga"], ["King Frost", "Oberon"]]  # Priestess and Emperor
]
print_personas(personas)  