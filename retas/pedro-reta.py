import numpy 
import matplotlib.pyplot as plt

def grafico(a,b,xF,yF):
    result = []
    for x in range (xF,yF+1):
        result.append((a*x)+b)
    return result

r = grafico(2,-3,0,2)
print(r)

plt.plot(grafico(2,-3,0,2))
plt.axhline(0,color='pink', linewidth = 2)
plt.axvline(0,color='pink', linewidth = 2)
plt.show()

