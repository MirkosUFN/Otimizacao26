import matplotlib.pyplot as plt

x = [1,3,6,10]
y = [2,1,5,4]

def desenhar(lx,ly):
    plt.scatter(x,y)
    plt.grid(True)
    plt.show()

desenhar(x,y)