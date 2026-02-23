import numpy as np

def main():
    lista = np.random.randint(0, 100, 50)
    media = np.mean(lista)
    
    abaixo = lista[lista <= media]
    acima = lista[lista >= media]
    
    print(f'Lista original: {lista}') 
    print(f'Média Calculada: {media:.2f}') 

    if abaixo.size > 0:
        print(f'Número mais próximo da média abaixo: {np.max(abaixo)}')
        
    if acima.size > 0:
        print(f'Número mais próximo da média acima: {np.min(acima)}')

if __name__ == '__main__':
    main()