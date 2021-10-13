from gl import Raytracer, V3, SetColor
from obj import Obj, Texture, EnvMap
from figures import *

# Dimensiones
width = 128
height = 128

# Materiales
wood = Material(diffuse = (0.6,0.2,0.2), spec = 64)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)

gold = Material(diffuse = (1, 0.8, 0 ),spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
portal = Material(diffuse = (75/255,0,130/255), spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)

earth = Material(texture = Texture('earthDay.bmp'))
box = Material(texture = Texture('box.bmp'))
obsidian = Material(texture = Texture('obsidian.bmp'))
doorUp = Material(texture = Texture('door.bmp'))
doorDown = Material(texture = Texture('door2.bmp'))


# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('envmap_parqueo.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))
#rtx.ambLight = AmbientLight(strength = 0.1)
#rtx.dirLight = DirectionalLight(direction = V3(0, 0, -1), intensity = 0.5)
#rtx.pointLights.append( PointLight(position = V3(0, 8, 0), intensity = 0.5))
#rtx.pointLights.append( PointLight(position = V3(0, -8, 0), intensity = 0.5))

#tx.scene.append( Sphere(V3(0,0,-8), 2, stone ))
#rtx.scene.append( Sphere(V3(-1,1,-5), 0.5, mirror ))
#rtx.scene.append( Sphere(V3(0.5,0.5,-5), 0.5, gold ))

# Objetos
#rtx.scene.append( Sphere(V3(0,0,-8), 2, earth) )

#Casa de cristal
#tx.scene.append( AABB(V3(-6,-6,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,-3,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,0,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,3,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,6,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,9,-29), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(-9,-6,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-9,-3,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-9,0,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-9,3,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-9,6,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-9,9,-26), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(-6,-6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,-3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,0,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-6,9,-23), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(-3,-6,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-3,-3,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-3,0,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-3,3,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-3,6,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(-3,9,-20), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(0,-6,-20), V3(3,3,1), doorDown) )
#tx.scene.append( AABB(V3(0,-3,-20), V3(3,3,1), doorUp) )
#tx.scene.append( AABB(V3(0,0,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,3,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,6,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,9,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,9,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,9,-26), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(0,9,-29), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(3,-6,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(3,-3,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(3,0,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(3,3,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(3,6,-20), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(3,9,-20), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(6,-6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,-3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,0,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,9,-23), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(9,-6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(9,-3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(9,0,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(9,3,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(9,6,-23), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(9,9,-23), V3(3,3,3), glass) )
#
#tx.scene.append( AABB(V3(6,-6,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,-3,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,0,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,3,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,6,-29), V3(3,3,3), glass) )
#tx.scene.append( AABB(V3(6,9,-29), V3(3,3,3), glass) )

#Portal
rtx.scene.append( AABB(V3(-1.5,-3,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(-1.5,0,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(-1.5,3,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,-3,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,0,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,3,-26), V3(3,3,1), portal) )

#Fila abajo
rtx.scene.append( AABB(V3(-4.5,-6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-1.5,-6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(1.5,-6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,-6,-26), V3(3,3,3), obsidian) )
#Fila izquierda
rtx.scene.append( AABB(V3(-4.5,-3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,0,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,6,-26), V3(3,3,3), obsidian) )
#Fila derecha
rtx.scene.append( AABB(V3(4.5,-3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,0,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,6,-26), V3(3,3,3), obsidian) )
#Fila arriba
rtx.scene.append( AABB(V3(-1.5,6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(1.5,6,-26), V3(3,3,3), obsidian) )

#rtx.scene.append( Sphere(V3(0, 2.5,-10), 3, mirror ))

#RT2: Opaque, Reflections & Refractions--------------------------------------------------------------------------------------------------
#Materials
#violette = Material(diffuse = (75/255,0,130/255), spec = 1)
#blue = Material(diffuse = (0, 0, 1), spec = 64, ior = 1.33, matType = TRANSPARENT)
#greenMirror = Material(diffuse = (0, 1, 0),spec = 32, matType = REFLECTIVE)
#WhiteMirror = Material(diffuse = (1, 1, 1),spec = 20, matType = REFLECTIVE)
#rubi = Material(diffuse = (224/255, 17/255, 95/255), spec = 64, ior = 1.77, matType = TRANSPARENT)
#yellow = Material(diffuse = (1,1,0), spec = 10)
#Light
#rtx.ambLight = AmbientLight(strength = 0.1)
#rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
#rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))

#Objects
#rtx.scene.append( Sphere(V3(-3,0,-8), 1, violette ))
#rtx.scene.append( Sphere(V3(-1,-1.5,-5), 0.5, blue ))
#rtx.scene.append( Sphere(V3(0, -1,-8), 1, greenMirror ))
#rtx.scene.append( Sphere(V3(0, 2.5,-10), 3, WhiteMirror ))
#rtx.scene.append( Sphere(V3(1,-1.5,-5), 0.5, yellow ))
#rtx.scene.append( Sphere(V3(3,0,-8), 1, rubi ))
#rtx.scene.append( Sphere(V3(-1,1,-5), 0.5, mirror ))
#rtx.scene.append( Sphere(V3(0.5,0.5,-5), 0.5, gold ))

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