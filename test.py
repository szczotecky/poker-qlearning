import csv
import hand_dictionary
import pickle

data ={}
sFile = "dane_matlab.txt" #matlab i matlab2

data =  pickle.load(open("dane.p","rb")) #dane_learn.p i dane.p
print sorted(data)

def zapisz(slownik):
    file1=open(sFile, "w")
    for el in slownik:
        element = slownik[el]
        linia = ",".join([str(el),str(element)])
        print >> file1, linia
    file1.close()

zapisz(data)