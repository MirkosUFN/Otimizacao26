import random as rd

lista_num = []

def gerar_lista():
    for i in range(50):
        numero = rd.randint(1, 100)
        lista_num.append(numero)
    print("LISTA:", lista_num)

def calcular_media():
    return sum(lista_num) / len(lista_num)

def buscar_mais_proximo():
    media_atual = calcular_media()
    mais_proximo = lista_num[0]
    
    for x in lista_num:
        dif_atual = abs(x - media_atual)
        dif_mais_proximo = abs(mais_proximo - media_atual)
        
        if dif_atual < dif_mais_proximo:
            mais_proximo = x
            
    return mais_proximo

def mostrar_mais_proximos():
    mais_proximo = buscar_mais_proximo()
    for i in range(len(lista_num)):
        if abs(lista_num[i] - mais_proximo) <= 3:
            print(lista_num[i])

gerar_lista()
print("MÉDIA:", calcular_media())
print("MAIS PRÓXIMOS:")
mostrar_mais_proximos()
