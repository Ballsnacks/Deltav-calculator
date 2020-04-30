import math
#For All Your Ballistic Needs* 

m0 = int(input("Launch mass: "))
mf = int(input("Dry mass: "))
Ve = int(input("Exaust Velocity: "))
Isp = int(input("Specific Impulse: "))
fuelMass = m0 - mf
Δv = Isp*9.8*math.log(float(m0/mf))
print(Δv)


#  *Hohmann Transfer Calculator Not Included