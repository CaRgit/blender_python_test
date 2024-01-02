import bpy
import bmesh
import os

f = open(r"C:\Users\carlos\Estudios\Ingeniería Industrial\MIERA\51600013-Robotica_Movil_y_de_Servicios\Trabajo\obstacle.csv", "w")

me = bpy.data.meshes['Room Primitive']

bm = bmesh.new()
bm.from_mesh(me)

faces = bm.faces

for face in faces:
    print(face.calc_center_median())
    f.write(str(face.calc_center_median()[0]))
    f.write(";")
    f.write(str(face.calc_center_median()[1]))
    f.write(";")
    f.write(str(face.calc_center_median()[2]))
    f.write(";")
    print(face.calc_area())
    f.write(str(face.calc_area()))
    f.write(";")
    print(face.normal)
    f.write(str(face.normal[0]))
    f.write(";")
    f.write(str(face.normal[1]))
    f.write(";")
    f.write(str(face.normal[2]))
    f.write("\n")

bm.free()

f.close()