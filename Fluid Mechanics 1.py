import math
import numpy
from matplotlib import pyplot

def uniformnaStruja(Uinf, beta, X, Y):
    cosBeta = math.cos(beta*math.pi/180)
    sinBeta = math.sin(beta*math.pi/180)
    u = Uinf*cosBeta
    v = Uinf*sinBeta
    phi = Uinf*(X*cosBeta + Y*sinBeta)
    psi = Uinf*(Y*cosBeta - X*sinBeta)
    return phi, psi, u, v

def izvor(izdasnost, x0, y0, X, Y):
    u = izdasnost/(2*numpy.pi)*(X-x0)/((X-x0)**2+(Y-y0)**2)
    v = izdasnost/(2*numpy.pi)*(Y-y0)/((X-x0)**2+(Y-y0)**2)
    phi = izdasnost/(2*numpy.pi)*numpy.log(numpy.sqrt((X-x0)**2 + (Y-y0)**2))
    psi = izdasnost/(2*numpy.pi)*numpy.arctan2((Y-y0), (X-x0))
    return phi, psi, u, v

def ponor(izdasnost, x0, y0, X, Y):
    u = -izdasnost/(2*numpy.pi)*(X-x0)/((X-x0)**2+(Y-y0)**2)
    v = -izdasnost/(2*numpy.pi)*(Y-y0)/((X-x0)**2+(Y-y0)**2)    
    phi = -izdasnost/(2*numpy.pi)*numpy.log(numpy.sqrt((X-x0)**2 + (Y-y0)**2))
    psi = -izdasnost/(2*numpy.pi)*numpy.arctan2((Y-y0), (X-x0))
    return phi, psi, u, v

def vrtlog(Gamma, x0, y0, X, Y):
    u = -Gamma/(2*math.pi) * (Y-y0)/((X-x0)**2 + (Y-y0)**2)
    v = Gamma/(2*math.pi) * (X-x0)/((X-x0)**2 + (Y-y0)**2)
    phi = Gamma/(2*numpy.pi)*numpy.arctan2((Y-y0), (X-x0))
    psi = -Gamma/(2*numpy.pi)*numpy.log(numpy.sqrt((X-x0)**2 + (Y-y0)**2))
    return phi, psi, u, v

def dvopol(M, x0, y0, X, Y):
    u = - M/(2*math.pi)*((X-x0)**2-(Y-y0)**2)/((X-x0)**2+(Y-y0)**2)**2
    v = - M/(2*math.pi)*2*(X-x0)*(Y-y0)/((X-x0)**2+(Y-y0)**2)**2
    psi =  -M/(2*math.pi)*(Y-y0)/((X-x0)**2+(Y-y0)**2)
    phi = M/(2*math.pi)*(X-x0)/((X-x0)**2+(Y-y0)**2)
    return phi, psi, u, v

N = 800                                  # broj tacaka u x i y pravcu
x_start, x_end = -2.0, 2.0               # xmin i xmax
y_start, y_end = -2.0, 2.0               # ymin i yman
x = numpy.linspace(x_start, x_end, N)    # 1D niz x koordinata
y = numpy.linspace(y_start, y_end, N)    # 1D niy y koordinata


X, Y = numpy.meshgrid(x, y)      
