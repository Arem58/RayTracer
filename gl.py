import struct
from collections import namedtuple
from obj import Obj
import random
import numpy as np
from math import cos, sin, tan
from mathLib import *

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

def SetColor(r, g, b):
    # Acepta valores de 0 a 1
    return bytes( [int(b * 255), int(g * 255), int(r * 255)] )

Black = SetColor(0,0,0)
White = SetColor(1,1,1)

class Raytracer(object):
    def __init__(self, width, height):
        self.clear_color = Black
        self.curr_color = White
        self.glCreateWindow(width, height)

        self.camPosition = V3(0,0,0)
        self.fov = 60

        self.background = None

        self.scene = []

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0, 0, width, height)

    def glViewport(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height

    def glVertex(self, x, y):
        Xw = round((x + 1) * (self.vpWidth * 0.5) + self.vpX)
        Yw = round((y + 1) * (self.vpHeight * 0.5) + self.vpY)
        if (Xw == self.vpWidth):
            Xw -= 1
        if (Yw == self.vpHeight):
            Yw -= 1
        #print(Xw, Yw)
        self.pixels[int(Xw)][int(Yw)] = self.curr_color

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
        if (0 < x < self.width) and (0 < y < self.height): 
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
                    file.write(self.pixels[x][y])

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

    def cast_ray(self, orig, dir):

        material = self.scene_intersect(orig, dir)

        if material == None:
            return self.clear_color
        else:
            return material.diffuse


    def scene_intersect(self, orig, dir):
        depth = float('inf')
        material = None
        
        for obj in self.scene:
            intersect = obj.ray_intersect(orig,dir)
            if intersect != None:
                if intersect.distance < depth:
                    depth = intersect.distance
                    material = obj.material

        return material

