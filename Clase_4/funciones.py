import numpy as np

A = 2
k = 800
m = 2

def posicion(A,k,m,t):
    '''
    Esta función retorna la posición, x, en un tiempo de de una masa m atada a un
    resorte de constante de fuerza k que inicialmente es desplazada A unidades de
    su posición de equilibrio. Esta función devuelve el resultado de 

    $A\sin (\omega t)$ donde $\omega = \sqrt{\frac{k}{m}}$

    Parámetros
    ----------
    A: float
        La amplitud o desplazamiento inicial de la masa.
    k: float
        La constante de fuerza del resorte.
    m: float
        La masa del objeto.
    t: float
        El tiempo en el cual se quiere calcular la posición.
    '''
    omega = np.sqrt(k/m)
    return A*np.sin(omega*t)

def periodo ():
    
    m = 2
    k = 800
    pi = np.pi
    
    T = 2*pi*np.sqrt(m/k)
    
    return T
T = periodo()

#t = np.linspace(-T/2,T/2)
#h = t[1]-t[0]

#print(t)

def derivada_progresiva (A,k,m,t,h):
    
    derivada = (posicion(A,k,m,t+h)-posicion(A,k,m,t))/(h)
    
    return derivada

def derivada_regresiva(A,k,m,t,h):
    
    y=t-h
    
    der = (posicion(A,k,m,t)-posicion(A,k,m,y))/(h)
    
    return der

def derivada_central(A,k,m,t,h):
    
    cen = (posicion(A,k,m,(t+h))-posicion(A,k,m,(t-h))/(2*h))
    
    return cen

    
def teorica(A,k,m,t):
    
    omega = np.sqrt(k/m)
    
    return  A*omega*np.cos(omega*t)