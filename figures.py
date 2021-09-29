from math import dist
from mathLib import *

OPAQUE = 0  
REFLECTIVE = 1
TRANSPARENT = 2

White = (1,1,1)
class DirectionalLight(object):
    def __init__(self, direction=V3(0,-1,0), intensity = 1,color = White):
        self.direction = norm(direction)
        self.intensity = intensity
        self.color = color

class AmbientLight(object):
    def __init__(self, strength = 0, color = White):
        self.strength = strength
        self.color = color
    
    def getColor(self):
        return (V3(self.strength * self.color[0],
                   self.strength * self.color[1],
                   self.strength * self.color[2]))

class PointLight(object):
    # Luz con putno de origen que va en todas direcciones
    def __init__(self, position = V3(0,0,0), intensity = 1, color = White):
        self.position = position
        self.intensity = intensity
        self.color = color

class Material(object):
    def __init__(self, diffuse = White, spec = 1, ior = 1,matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.matType = matType

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObject):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject

class Sphere(object):
    def __init__(self, center, radius, material = Material()):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        
        L = sub(self.center, orig)
        l = length(L)

        tca = dot(L, dir)

        d = (l**2 - tca**2) 

        if d > self.radius ** 2:
            return None

        thc = (self.radius**2 - d)**0.5
        t0 = tca - thc
        t1 = tca + thc

        #La esfera esta completamente detras de la camara
        
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        # La camara esta dentro de la esfera 
        # P = O + t * D

        hit = add(orig, mul(dir, t0))
        normal = norm(sub(hit, self.center))

        return Intersect( distance = t0,
                          point = hit, 
                          normal = normal, 
                          sceneObject = self)

