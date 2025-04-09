import os

class Txt_Reader:
    def __init__(self,file_name):
        ruta_acr = os.getcwd()
        self.txt_arr = []
        with open(f"{ruta_acr}/Python/EstructuraDatos/{file_name}","r") as file:
            self.txt = file.read()
            file.seek(0)
            for line in file:
                self.txt_arr.append(line.strip())

    def __str__(self):
        return(str(self.txt))
        
    def get_linearr(self):
        return(self.txt_arr)
    
    def get_line(self,index):
        line = self.txt_arr[index-1]
        return line
    
    def has_chars(self,mot):
        m = 0
        while(m < len(self.txt_arr)):
            i = 0
            while(i < len(self.txt_arr[m])-1):
                if self.txt_arr[m][i] == mot[0]:
                    j = 0
                    palabra = ""
                    while(j < len(mot) and j+i < len(self.txt_arr[m])):
                        palabra += self.txt_arr[m][i+j] 
                        j += 1

                    if(palabra == mot):
                        return m+1
                i += 1
            m += 1
        return -1
    
    def count_words(self):
        i = 0
        contador = 0
        temp = " "
        while(i < len(self.txt)):
            if ( (isinstance(temp, str))  and temp != " " and temp != "\n")  and ( self.txt[i] == " "  or self.txt[i]  == '\n')  :
                contador += 1
            temp = self.txt[i]
            i += 1  
        
        if (isinstance(self.txt[len(self.txt)-1], str))  and self.txt[len(self.txt)-1] != " ":
            contador += 1

        return contador 
    


                    

file_name = "Example txt for Data Structures.txt"
#Cargar nombre del txt
txt_reader = Txt_Reader(file_name)


#Imprimir todo el txt
print(txt_reader)
#Obtener las líneas como arrays
print(txt_reader.get_linearr())



#Obtener una línea específica (\n cuentan como una línea)
print(txt_reader.get_line(5))

#Contar palabras
print(txt_reader.count_words())

#Buscar una palabra dentro del txt y si se encuentra devolver en que línea se encuentra de otro modo devuelve -1
print(txt_reader.has_chars("fifth"))




