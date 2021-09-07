from gl import Raytracer, V3, SetColor
from obj import Obj, Texture

from figures import Sphere, Material

width = 1920
height = 1080

material1 = Material(SetColor(0.945, 0.894, 0.792))
material2 = Material(SetColor(0.023, 0.023, 0.031))
material3 = Material(SetColor(0.980, 0.235, 0.133))
material4 = Material(SetColor(0.384, 0.325, 0.305))
material5 = Material(SetColor(0.862, 0.815, 0.835))
material6 = Material(SetColor(0.125, 0.094, 0.113))

rtx = Raytracer(width, height)

#Cuerpo 
rtx.scene.append(Sphere(V3(0,-2,-10), 2, material1))
rtx.scene.append(Sphere(V3(0,0.5,-10), 1.7, material1))
rtx.scene.append(Sphere(V3(0,2.8,-10), 1.4, material1))

#Botones
rtx.scene.append(Sphere(V3(0,-1.65,-8), 0.5, material2))
rtx.scene.append(Sphere(V3(0,-0.3,-8), 0.3, material2))
rtx.scene.append(Sphere(V3(0,0.85,-8), 0.3, material2))

#Nariz
rtx.scene.append(Sphere(V3(0,2.25,-8), 0.3, material3))

#Boca
rtx.scene.append(Sphere(V3(-0.2,1.68,-8), 0.1, material4))
rtx.scene.append(Sphere(V3(0.2,1.68,-8), 0.1, material4))
rtx.scene.append(Sphere(V3(-0.5,1.9,-8), 0.1, material4))
rtx.scene.append(Sphere(V3(0.5,1.9,-8), 0.1, material4))

#Ojos
rtx.scene.append(Sphere(V3(0.4,2.8,-8), 0.15, material5))
rtx.scene.append(Sphere(V3(-0.4,2.8,-8), 0.15, material5))
rtx.scene.append(Sphere(V3(-0.38,2.48,-7), 0.09, material6))
rtx.scene.append(Sphere(V3(0.38,2.48,-7), 0.09, material6))

rtx.glREnder()
#rtx.glREnderTester()

rtx.glFinish('output.bmp')