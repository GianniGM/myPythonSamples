x = input("bamba!!!");
lista = ["gianni", 27, [17, "maggio", 1989]]
#la lista sopra non va bene, devono essere tutte stringhe
#e devono avere tutte il limitatore di carattere sennò scrive tutto inline
#e fa casino alla lettura
#possono essere solo liste
lista2 = ["gianni\n", "modica\n", "maggio\n" ]

lista 

miofile = open("prova.txt","w")
#miofile.write("cacca") #stampa senza andare a capo
#miofile.write(lista[0])
miofile.writelines(lista2) #è come una write iterata in una lista
miofile.close()

miofile = open("prova.txt", "r")
#gianni = miofile.readline() #come write solo in lettura
lista = miofile.readlines()  #come writelines solo in lettura
print(lista)
miofile.close()


#CICLI E CONDIZIONI

a= 0
b = 10
while a < b:
    a=a+1
    print(a)
    if a == 5:
        print("a ha raggiunto il ciclo")
else:
    print("sono uscito dal ciclo")

#il for è più come un foreach di java anche se può essere usato
#anche normalmente con for i in range(10): [comando]

for lettera in 'HTML.it':
    if lettera == '.':
        pass                     #è uno skip in piena regola
    else:
        print('Lettera attuale: ',lettera)


#COMPRENSHION - in ML ricordano le foldr e le map

euro = [2.5, 3.7, 20.9]

# LISTA = [BLOCCO for [indice] in [ALTRA LISTA]]
dollaro = [x*1.3 for x in euro]
dollarofiltrato = [x*1.3 for x in euro if x < 5 ]
dollaromappato = {x: x*1.3 for x in euro if x < 5}
print(euro)
print(dollaro)
print(dollarofiltrato)
print(dollaromappato)


#next http://www.html.it/pag/15619/moduli/
