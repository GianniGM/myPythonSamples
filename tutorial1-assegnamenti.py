#esempi basilari python vol.1
#per gli operatori si veda
# http://www.html.it/pag/39742/numeri-e-operatori-logici-in-python/

#funzioni
def fun( arg1, arg2):
    return arg1 + arg2

s= "Hello World!"
print (s)
print(len(s))
print (s.find("World"))
print(s.replace ("World","Merda"))
print(s.upper())

#se inserisci come input il valore di una variabile questo viene preso
s = input("inserisci stringa 1 ")
d = input("inserisci stringa 2 ")

#niente segmentation fault
print(s[2:-1]+d[0:2]+"a" * 3)

#stringhe e formattazioni http://www.html.it/pag/39746/stringhe-in-python/
a = "merda"
s = eval(input("inserisci valore numerico1 "))
d = eval(input("inserisci valore numerico2 "))
risultato = "il risultato è %d, il tipo è %s" % (fun(s,d), type(s))
print(risultato, ". tipo di fun", type(fun(s, d)))

#scope
def fun2(x):
    x=8

s = input("[scope] inserisci valore ")
fun2(s)
print(s)

x=9/2         # la divisione tra due numeri interi restituisce un float
x=9%2         # operazione in modulo
x= 9//2       # divisione intera

x=2j * 2j     # moltiplicazione tra numeri complessi
print("complessi", x)

x=int(10.6)   # conversione esplicita dal tipo float al tipo int
print("conversione esplicita di 10.6 ", x)

y=float(20)   # conversione esplicita dal tipo int al tipo float
print("conversione esplicita di float ", y)
