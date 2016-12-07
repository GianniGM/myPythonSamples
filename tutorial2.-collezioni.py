#passaggio di funzione, trasforma i parametri in tupla
#le tuple sono immutabili
def trantupla(*tupla):
    print(tupla)
    print(type(tupla))

t=trantupla("uno", "due", "tre")
print(t)

#dizionario usando doppio asterisco trasforma i parametri in dizionari
def trandizionario(** dizionario):
    print(dizionario)
    print(type(dizionario))

v=trandizionario(terzo = 3, secondo = 2, primo = 1)
print(v)

#liste in python sono elementi eterogenei gli operatori sono simili come per le stringhe
io = ["Gianni", 26, ["Giovanni", "Graziano"], [17, "maggio"], 2016-1989 ]
print(io[0])
print(io[-1])
print(io[-2])
print(io[-2][0])

#ripetizione di elementi in una lista
a = io * 3

#concatenazione di elementi in una lista
b = [1, 2, 3]
print(a+b)

#cancella le celle 2 e 3
#per cancellare un solo elemento io[i:i+1] = [] l'i+1esimo rimane integro
#la funzione sort([lista]) ordina in modo crescente
io[2:4] = []
print(io)


#le HashMap di java sono rappresentate dai dizionari in python
#i dizionari si rappresentano con le parentesi graffe {} hanno una chiave e un contenuto
#se la chiave è uguale il valore viene sovrascritto con l'ultimo (più aggiornato)
dizionario = {"Gianni":1, "Giacomo":200, "Giuseppe":2, "Gianni":45}
print(dizionario["Gianni"])
print(dizionario.values())


# print(dizionario.keys().sort()) vecchio metodo, non funziona più con python 3
#convertiamo in lista

keysList=list(dizionario.keys())
keysList.sort()
for i in keysList: print(i, dizionario[i])

#ricapitolando:
#le liste usano le parentesi []
#i dizionari usano le parentesi graffe{key:value, key:value} e hanno valori univoci in base alla chiave
#le tuple usano le parentesi tonde()
#le tuple a differenza delle liste non sono mutabili (operano sullo stack, non sullo heap)
#supportano somma, ripetizione e slicing usando le quadre

tupla = (1,2,3,3,4)

print(tupla)
print(tupla[2])
#[1:2] = [1]
print(tupla[1:3])
print(tupla[1:2])
print(tupla[1])   #notare come viene rappresentato il singoletto in ambedue i casi
