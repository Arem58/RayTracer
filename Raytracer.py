from gl import Raytracer, V3, SetColor
from obj import Obj, Texture, EnvMap
from figures import *

# Dimensiones
width = 1920
height = 1080

# Materiales
wood = Material(diffuse = (0.6,0.2,0.2), spec = 64)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)

gold = Material(diffuse = (1, 0.8, 0 ),spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
portal = Material(diffuse = (75/255,0,130/255), spec = 264, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 600, ior = 1.5, matType = TRANSPARENT)
diamond = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)

earth = Material(texture = Texture('earthDay.bmp'))
box = Material(texture = Texture('box.bmp'))
obsidian = Material(texture = Texture('obsidian.bmp'))
doorUp = Material(spec = 264, texture = Texture('door.bmp'))
doorDown = Material(spec = 264, texture = Texture('door2.bmp'))
fondoDelPortal = Material(spec = 264, texture = Texture('envmap_parqueo.bmp'))


# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('fondo3.bmp')

# Luces
#rtx.ambLight = AmbientLight(strength = 1)
#rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
#rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))
rtx.ambLight = AmbientLight(strength = 0.5)
rtx.dirLight = DirectionalLight(direction = V3(0, 0, -1), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 8, 0), intensity = 0.5))
#rtx.pointLights.append( PointLight(position = V3(0, 0, -32), intensity = 0.5))

#tx.scene.append( Sphere(V3(0,0,-8), 2, stone ))
#rtx.scene.append( Sphere(V3(-1,1,-5), 0.5, mirror ))
#rtx.scene.append( Sphere(V3(0.5,0.5,-5), 0.5, gold ))

# Objetos
#Gold
rtx.scene.append( AABB(V3(0.058,-0.04,-0.1), V3(0.024,0.0065,0.008), gold) )
rtx.scene.append( AABB(V3(0.058,-0.04,-0.09), V3(0.024,0.0065,0.008), gold) )
rtx.scene.append( AABB(V3(0.058,-0.0318,-0.095), V3(0.024,0.0065,0.008), gold) )
#rtx.scene.append( Sphere(V3(0.073,-0.0318,-0.085), 0.01, glass) )
rtx.scene.append( Sphere(V3(0.04,-0.0312,-0.066), 0.003, diamond) )
rtx.scene.append( Sphere(V3(0.05,-0.0312,-0.066), 0.003, diamond) )

#Casa de cristal
rtx.scene.append( AABB(V3(-6,-8,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,-5,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,-2,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,1,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,4,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(-9,-8,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-9,-5,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-9,-2,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-9,1,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-9,4,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-9,7,-26), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(-6,-8,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,-5,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,-2,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,1,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,4,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,7,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,7,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-6,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(-3,-8,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,-5,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,-2,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,1,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,4,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,7,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,7,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,7,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(-3,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(0,-8,-20), V3(3,3,1), doorDown) )
rtx.scene.append( AABB(V3(0,-5,-20), V3(3,3,1), doorUp) )
rtx.scene.append( AABB(V3(0,-2,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,1,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,4,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,7,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,7,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,7,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(0,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(3,-8,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,-5,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,-2,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,1,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,4,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,7,-20), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,7,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,7,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(3,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(6,-8,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,-5,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,-2,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,1,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,4,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,7,-23), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,7,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,7,-29), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(9,-8,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(9,-5,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(9,-2,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(9,1,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(9,4,-26), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(9,7,-26), V3(3,3,3), glass) )

rtx.scene.append( AABB(V3(6,-8,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,-5,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,-2,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,1,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,4,-29), V3(3,3,3), glass) )
rtx.scene.append( AABB(V3(6,7,-29), V3(3,3,3), glass) )

#Portal
rtx.scene.append( AABB(V3(-1.5,-6,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(-1.5,-3,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(-1.5,0,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,-6,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,-3,-26), V3(3,3,1), portal) )
rtx.scene.append( AABB(V3(1.5,0,-26), V3(3,3,1), portal) )

#Fila abajo
rtx.scene.append( AABB(V3(-1.5,-9,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,-9,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(1.5,-9,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,-9,-26), V3(3,3,3), obsidian) )
#Fila izquierda
rtx.scene.append( AABB(V3(-4.5,-6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,-3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,0,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(-4.5,3,-26), V3(3,3,3), obsidian) )
#Fila derecha
rtx.scene.append( AABB(V3(4.5,-6,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,-3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,0,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(4.5,3,-26), V3(3,3,3), obsidian) )
#Fila arriba
rtx.scene.append( AABB(V3(-1.5,3,-26), V3(3,3,3), obsidian) )
rtx.scene.append( AABB(V3(1.5,3,-26), V3(3,3,3), obsidian) )

#rtx.scene.append( AABB(V3(0, 0,-32), V3(15,16,1), fondoDelPortal) )

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