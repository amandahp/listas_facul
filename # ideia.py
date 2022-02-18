import math

# # a = base x = log e b = logaritmando 

# import math

# def closet_to_average(lst, valor):
#     n = valor
#     diffs = {value: abs(value - n) for value in lst}

#     return min(diffs, key=diffs.get)


# def log_fun(b):
#   valores = list([])
#   lista_log = list([])
#   for i in range(2, b):
#     valores.append(i)
#   for a in valores:
#     if int(b) > 0:
#       x = math.log(b,a)
#       lista_log.append(x)
#   # print(valores)
#   # print(lista_log)
#   product = [x**y for x,y in zip(valores,lista_log)]
#   # pegar valor mais proximo de b
#   valor_mais_proximo = closet_to_average(product, b)
#   #print(valor_mais_proximo)
#   # buscar indice do valor mais proximo
#   indice = product.index(valor_mais_proximo)
#   # buscar valor da base e x que esta no mesmo indice
#   indice_base = valores[indice]
#   indice_x = lista_log[indice]
#   print(indice_base)
#   print(indice_x)
#   resultado = indice_base**indice_x
#   #resultado_proximo = round(resultado, 1)
#   print(resultado)
  
 

# log_fun(13)

def teste(n):
    x = len(str(n))
    num = [int(_) for _ in str(n)]
    conta = 1/(num[0]**x)*num[1]**1*num[1]**(x-1)+num[2]**x*num[2]**(x-1)*1/(num[2]**x)
    print(num[0])
    print(num[1])
    print(num[2])
    print(conta)
    valor = math.pow(conta, 1/2.585133709197507)
    print(valor)

print(teste(153))