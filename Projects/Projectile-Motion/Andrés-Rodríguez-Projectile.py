import math

Gunname = ("Ak-101")
Cartridgecalibre = ("5.56x45mm NATO")
Round = ("5.56x45mm HP")
Projectilespeed = 947

Building = ("Lotte world tower")
Buildingheight = 555
gravity = 9.8

time = (math.sqrt(2 * Buildingheight/gravity))
deltaX = (Projectilespeed * time)