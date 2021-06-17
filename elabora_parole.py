# Dando in input in file con delle parole crea un .py con una lista di parole
import os

sorgente = open("1000_parole_italiane_comuni.txt", "r")
dest = ((os.path.splitext(sorgente.name)[0])+'_elaborato.txt',"w+")

if os.path.exists(dest[0]):
    os.remove(dest[0]) # Cancello il file se esiste già

fdest = open(str(dest[0]),"w+")

fdest.write('parole = ["'+sorgente.readline().strip('\r\n'))
while True:
    riga = sorgente.readline()
    if not riga:
        break
    fdest.write(',"'+sorgente.readline().strip('\r\n')+'"')
fdest.write(']')

# Chiudo i file usati
sorgente.close
fdest.close
