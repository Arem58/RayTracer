from math import dist
from gl import White
from mathLib import *

class Material(object):
    def __init__(self, diffuse = White):
        self.diffuse = diffuse

class Intersect(object):
    def __init__(self, distance):
        self.distance = distance

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        
        # P = O + t * D

        L = sub(self.center, orig)

        tca = dot(L, dir)
        l = length(L)
        d = (l**2 - tca**2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius**2 - d**2)**0.5
        t0 = tca - thc
        t1 = tca + thc

        #La esfera esta completamente detras de la camara
        
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        # La camara esta dentro de la esfera 
        
        return Intersect( distance = t0 )

