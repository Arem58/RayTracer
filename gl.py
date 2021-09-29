import struct
from collections import namedtuple
from obj import Obj, SetColor
from math import sin, tan
from mathLib import *

OPAQUE = 0  
REFLECTIVE = 1
TRANSPARENT = 2

MAX_RECURSION_DEPTH = 3

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes 
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def reflectVector(normal, dirVector):
    reflect = 2 * dot(normal, dirVector)
    reflect = norm(sub(mul(normal, reflect), dirVector))
    return reflect

def refractVector(normal, dirVector, ior):
    #Snell's Law
    
    cosi = max(-1, min(1, dot(dirVector, normal)))
    etai = 1 
    etat = ior 

    if cosi < 0:
        cosi = -cosi
    else:
        etai, etat = etat, etai
        normal = mul(normal, -1)
    eta = etai / etat
    k = 1 - eta * eta * (1 - (cosi * cosi))
    if k < 0: #Total Internal Reflection
        return None
    R = norm(add(mul(dirVector, eta), mul(normal, (eta * cosi - k**0.5))))
    return R

def fresnel(normal, dirVector, ior):
    cosi = max(-1, min(1, dot(dirVector, normal)))
    etai = 1 
    etat = ior 

    if cosi > 0:
        etai, etat = etat, etai
    sint = etai / etat * (max(0, 1 - cosi * cosi)) ** 0.5
    if sint >= 1: #Total internal reflection
        return 1

    cost = max(0, 1 - sint * sint) ** 0.5
    cosi = abs(cosi)
    Rs = ((etat * cosi) - (etai * cost)) / ((etat * cosi) + (etai * cost))
    Rp = ((etai * cosi) - (etat * cost)) / ((etai * cosi) + (etat * cost))

    return (Rs * Rs + Rp * Rp) / 2

Black = (0,0,0)
White = (1,1,1)

class Raytracer(object):
    def __init__(self, width, height):
        self.clear_color = Black
        self.curr_color = White
        self.glCreateWindow(width, height)

        self.camPosition = V3(0,0,0)
        self.fov = 60

        self.background = None

        self.scene = []

        self.pointLights = []
        self.ambLight = None
        self.dirLight = None

        self.envmap = None

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0, 0, width, height)

    def glViewport(self, x, y, width, height):
        self.vpX = int(x)
        self.vpY = int(y)
        self.vpWidth = int(width)
        self.vpHeight = int(height)

    def glClearColor(self, r, g, b):
        self.clear_color = SetColor(r, g, b)
    
    def glClear(self):
        #Crea una lista 2D de pixeles y a cada valor le asigna 3 bytes de color
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]

    def glClearBackground(self):
        if self.background:
            for x in range(self.vpX, self.vpX + self.vpWidth):
                for y in range(self.vpY, self.vpY  + self.vpHeight):
                    
                    tx = (x - self.vpX)/self.vpWidth
                    ty = (y - self.vpY)/self.vpHeight

                    self.glPoint(x, y, self.background.getColor(tx, ty))

    def glColor(self, r, g, b):
        self.curr_color = SetColor(r, g, b)

    def glPoint(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return
        if (0 <= x < self.width) and (0 <= y < self.height): 
            self.pixels[int(x)][int(y)] = color or self.curr_color
    
    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color Table
            for y in range(self.height):
                for x in range(self.width):
                    file.write( SetColor(self.pixels[x][y][0],
                                         self.pixels[x][y][1],
                                         self.pixels[x][y][2]))

    def glREnder(self):
        for y in range(self.height):
            for x in range(self.width):
                # pasar de coordenadas de ventana a coordenadas NDC (-1 a 1)
                Px = 2 * (x + 0.5) / self.width - 1    
                Py = 2 * (y + 0.5) / self.height - 1   

                #Angulo de vision, asumiendo que el near plane a 1 unidad de la camara
                t = tan( (self.fov * pi / 180) / 2)
                r = t * self.width / self.height

                Px *= r
                Py *= t

                #La camara siempre esta viendo hacia -z
                direction = norm(V3(Px, Py, -1))
                self.glPoint(x, y, self.cast_ray(self.camPosition, direction))

    def glREnderTester(self):
        for y in range(0, self.height, 2):
            for x in range(0, self.width, 2):
                # pasar de coordenadas de ventana a coordenadas NDC (-1 a 1)
                Px = 2 * (x + 0.5) / self.width - 1    
                Py = 2 * (y + 0.5) / self.height - 1   

                #Angulo de vision, asumiendo que el near plane a 1 unidad de la camara
                t = tan( (self.fov * pi / 180) / 2)
                r = t * self.width / self.height

                Px *= r
                Py *= t

                #La camara siempre esta viendo hacia -z
                direction = norm(V3(Px, Py, -1))
                self.glPoint(x, y, self.cast_ray(self.camPosition, direction))

    def cast_ray(self, orig, dir, origObj = None, recursion = 0):

        intersect = self.scene_intersect(orig, dir, origObj)

        if intersect == None or recursion >= MAX_RECURSION_DEPTH:
            if self.envmap:
                return self.envmap.getColor(dir)
            return self.clear_color

        material = intersect.sceneObject.material 

        #Colors
        finalColor = V3(0,0,0)
        objectColor = V3(material.diffuse[0],
                         material.diffuse[1],
                         material.diffuse[2])

        ambientColor = V3(0,0,0)
        dirLightColor = V3(0,0,0)
        pLightColor = V3(0,0,0)
        finalSpecColor = V3(0,0,0)
        reflectColor = V3(0,0,0)
        refractColor = V3(0,0,0)

        # direccion de la vista
        view_dir = norm(sub(self.camPosition, intersect.point))

        
        if self.ambLight:
            ambientColor = self.ambLight.getColor()

        if self.dirLight:
            diffuseColor = V3(0,0,0)
            specColor = V3(0,0,0)
            shadow_intensity = 0

            # Iluminacion difusa
            light_dir = mul(self.dirLight.direction, -1)
            intensity = max(0, dot(intersect.normal, light_dir)) * self.dirLight.intensity
            diffuseColor = V3(intensity * self.dirLight.color[0],
                              intensity * self.dirLight.color[1],
                              intensity * self.dirLight.color[2])

            # Iluminacion especular 
            reflect = reflectVector(intersect.normal, light_dir)
            spec_Intensity = self.dirLight.intensity * max(0, dot(view_dir, reflect)) **  material.spec
            specColor = V3(spec_Intensity * self.dirLight.color[0],
                           spec_Intensity * self.dirLight.color[1],
                           spec_Intensity * self.dirLight.color[2])

            #Shadow
            shadInter = self.scene_intersect(intersect.point, light_dir, intersect.sceneObject)
            if shadInter:
                shadow_intensity = 1

            shadow_intensity = 1 - shadow_intensity 
            dirLightColor = mul(diffuseColor, shadow_intensity)
            finalSpecColor = add(finalSpecColor, mul(specColor, shadow_intensity))

        for pointLight in self.pointLights:
            diffuseColor = V3(0,0,0)
            specColor = V3(0,0,0)
            shadow_intensity = 0

            # Iluminacion difusa 
            light_dir = norm(sub(pointLight.position, intersect.point))
            intensity = max(0, dot(intersect.normal, light_dir)) * pointLight.intensity
            diffuseColor = V3(intensity * pointLight.color[0],
                              intensity * pointLight.color[1],
                              intensity * pointLight.color[2])

            # Iluminacion especular 
            reflect = reflectVector(intersect.normal, light_dir)
            spec_Intensity = pointLight.intensity * max(0, dot(view_dir, reflect)) ** material.spec
            specColor = V3(spec_Intensity * pointLight.color[0],
                           spec_Intensity * pointLight.color[1],
                           spec_Intensity * pointLight.color[2])
            #Shadow
            shadInter = self.scene_intersect(intersect.point, light_dir, intersect.sceneObject)
            lightDistance = length(sub(pointLight.position, intersect.point))
            if shadInter and shadInter.distance < lightDistance:
                shadow_intensity = 1

            shadow_intensity = 1 - shadow_intensity 
            pLightColor = add(pLightColor,  mul(diffuseColor, shadow_intensity))
            finalSpecColor = add(finalSpecColor, mul(specColor, shadow_intensity))

        
        if material.matType == OPAQUE:
            finalColor = add(pLightColor, ambientColor)
            finalColor = add(finalColor, dirLightColor)
            finalColor = add(finalColor, finalSpecColor)
        elif material.matType == REFLECTIVE:
            reflect = reflectVector(intersect.normal, mul(dir,-1))
            reflectColor = self.cast_ray(intersect.point, reflect, intersect.sceneObject, recursion + 1)
            reflectColor = V3(reflectColor[0],
                              reflectColor[1],
                              reflectColor[2],)
            finalColor = add(reflectColor, finalSpecColor)
        elif material.matType == TRANSPARENT:
            outside = dot(dir, intersect.normal) < 0
            bias = mul(intersect.normal, 0.0001)
            kr = fresnel(intersect.normal, dir, material.ior)

            reflect = reflectVector(intersect.normal, mul(dir,-1))
            reflctOrig = add(intersect.point, bias) if outside else sub(intersect.point, bias)
            reflectColor = self.cast_ray(reflctOrig, reflect, None, recursion + 1)
            reflectColor = V3(reflectColor[0], 
                              reflectColor[1], 
                              reflectColor[2])


            if kr < 1:
                refract = refractVector(intersect.normal, dir, material.ior)
                refractOrig = sub(intersect.point, bias) if outside else add(intersect.point, bias)
                refractColor = self.cast_ray(refractOrig, refract, None, recursion + 1)
                refractColor = V3(refractColor[0], 
                                  refractColor[1], 
                                  refractColor[2])
            finalColor = add(mul(reflectColor, kr), mul(refractColor, (1-kr)))
            finalColor = add(finalColor, finalSpecColor)

        # Le aplicamos el color del objeto
        finalColor = vectMul(objectColor, finalColor)

        #Nos aseguramos que no suba el valor de color de 1
        r = min(1, finalColor[0])
        g = min(1, finalColor[1])
        b = min(1, finalColor[2])

        return (r,g,b)

    def scene_intersect(self, orig, dir, oriObj = None):
        depth = float('inf')
        intersect = None
        
        for obj in self.scene:
            if obj is not oriObj:
                hit = obj.ray_intersect(orig,dir)
                if hit != None:
                    if hit.distance < depth:
                        depth = hit.distance
                        intersect  = hit

        return intersect

