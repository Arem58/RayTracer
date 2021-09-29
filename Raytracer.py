from gl import Raytracer, V3, SetColor
from obj import Obj, Texture, EnvMap
from figures import *

width = 1024
height = 1024

#Materiales
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)
mirror = Material(spec = 128, matType = REFLECTIVE)
gold = Material(diffuse = (1, 0.8, 0 ), spec = 32, matType = REFLECTIVE)

rtx = Raytracer(width, height)
rtx.envmap = EnvMap('envmap_parqueo.bmp')
#RT2: Opaque, Reflections & Refractions--------------------------------------------------------------------------------------------------

rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))
#rtx.pointLights.append(PointLight(position=V3(5, -7, 0)))
rtx.scene.append( Sphere(V3(0,0,-8), 2, stone ))
rtx.scene.append( Sphere(V3(-1,1,-5), 0.5, mirror ))
rtx.scene.append( Sphere(V3(0.5,0.5,-5), 0.5, gold ))

#RT1: Spheres and Materials--------------------------------------------------------------------------------------------------
#material1 = Material(SetColor(0.945, 0.894, 0.792))
#material2 = Material(SetColor(0.023, 0.023, 0.031))
#material3 = Material(SetColor(0.980, 0.235, 0.133))
#material4 = Material(SetColor(0.384, 0.325, 0.305))
#material5 = Material(SetColor(0.862, 0.815, 0.835))
#material6 = Material(SetColor(0.125, 0.094, 0.113))
#Cuerpo 
#rtx.scene.append(Sphere(V3(0,-2,-10), 2, material1))
#rtx.scene.append(Sphere(V3(0,0.5,-10), 1.7, material1))
#rtx.scene.append(Sphere(V3(0,2.8,-10), 1.4, material1))

#Botones
#rtx.scene.append(Sphere(V3(0,-1.65,-8), 0.5, material2))
#rtx.scene.append(Sphere(V3(0,-0.3,-8), 0.3, material2))
#rtx.scene.append(Sphere(V3(0,0.85,-8), 0.3, material2))

#Nariz
#rtx.scene.append(Sphere(V3(0,2.25,-8), 0.3, material3))

#Boca
#rtx.scene.append(Sphere(V3(-0.2,1.68,-8), 0.1, material4))
#rtx.scene.append(Sphere(V3(0.2,1.68,-8), 0.1, material4))
#rtx.scene.append(Sphere(V3(-0.5,1.9,-8), 0.1, material4))
#rtx.scene.append(Sphere(V3(0.5,1.9,-8), 0.1, material4))

#Ojos
#rtx.scene.append(Sphere(V3(0.4,2.8,-8), 0.15, material5))
#rtx.scene.append(Sphere(V3(-0.4,2.8,-8), 0.15, material5))
#rtx.scene.append(Sphere(V3(-0.38,2.48,-7), 0.09, material6))
#rtx.scene.append(Sphere(V3(0.38,2.48,-7), 0.09, material6))

rtx.glREnder()
#rtx.glREnderTester()

rtx.glFinish('output.bmp')