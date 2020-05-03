import math

#T H E   S P I C E   M U S T   F L O W

m0 = int(input("\n \n Launch mass: "))
mf = int(input("Dry mass: "))
Ve = int(input("Exaust Velocity: "))
Isp  = int(input("Specific Impulse: "))
fuelMass = m0 - mf
Δv = Isp*9.8*math.log(float(m0/mf))
print("Δv:")
print(Δv)
print("Fuel Mass:")
print(fuelMass)
staging = input("is that your only stage [Y/N]: ")

if staging == "n":
    print("Δv Calculation for Stage 2")
    m0 = int(input("Launch mass of second stage: "))
    mf = int(input("Dry mass of second stage: "))
    Ve = int(input("Exaust Velocity of second stage: "))
    Isp  = int(input("Specific Impulse of second stage: "))
    fuelMass = m0 - mf
    Δv2 = Isp*9.8*math.log(float(m0/mf))
    tΔv = Δv2 + Δv
    print("Δv:")
    print(Δv2)
    print("Fuel Mass:")
    print(fuelMass)
    print("total Δv:")
    print(tΔv)
    print("\n ________________________________________________________________________________________________________")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("██Low Earth Orbit█████Moon█████Venus█████Mars█████Jupiter█████Saturn█████Uranus█████Neptune█████Mercury██")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("██Δv-█████████████.	    .	     . 	    .. . . . .|. . . . .      .	      .	       .████████████Δv+██")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("█.        *    .                         .                               *       .  .                .  █")
    print("█   .                                                   .                         .                     █")
    print("█           .          *           .         .                 *         .                       .      █")
    print("█            .                    .                  .               .               .                  █")
    print("█              .      .          .           .                              .            *          .   █")
    print("█                                                   .           .                   .           .       █")
    print("█    .                     *               .                                                            █")
    print("█                                                 *                      .                   .          █")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    gloc = input("\n Where would you wish to travel, Captain?: ")
    if gloc == "moon":
        if tΔv > 13340:
            print("\n You're all set for a 100km orbit around the Moon, Captain. Safe Travels!")
        if tΔv < 13340:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "mars":
        if tΔv > 15110:
            print("\n You're all set for a 200km orbit around Mars, Captain. Safe Travels!")
        if tΔv < 15110:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "low earth orbit":
        if tΔv > 9400:
            print("\n You're all set for a 250km orbit around Earth, Captain. Safe Travels!")
        if tΔv < 9400:
            print("\n Sorry Captain, not with that lil thing")
            
    if gloc == "venus":
        if tΔv > 16190:
            print("\n You're all set for a 400km orbit around Venus, Captain. Safe Travels!")
        if tΔv < 16190:
            print("\n Sorry Captain, not with that lil thing") 

    if gloc == "Jupiter":
        if tΔv > 33170:
            print("\n You're all set for a 2000km orbit around Jupiter, Captain. Safe Travels!")
        if tΔv < 33170:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "saturn":
        if tΔv > 27340:
            print("\n You're all set for a 2000km orbit around Saturn, Captain. Safe Travels!")
        if tΔv < 27340:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "Uranus":
        if tΔv > 24010:
            print("\n You're all set for a 1000km orbit around Uranus, Captain. Safe Travels!")
        if tΔv < 24010:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "neptune":
        if tΔv > 24750:
            print("\n You're all set for a 1000km orbit around Neptune, Captain. Safe Travels!")
        if tΔv < 24750:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "mercury":
        if tΔv > 22480:
            print("\n You're all set for a 100km orbit around Mercury, Captain. Safe Travels!")
        if tΔv < 22480:
            print("\n Sorry Captain, not with that lil thing")
            
if staging == "y":
    print("\n ________________________________________________________________________________________________________")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("██Low Earth Orbit█████Moon█████Venus█████Mars█████Jupiter█████Saturn█████Uranus█████Neptune█████Mercury██")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("██Δv-█████████████.	    .	     . 	    .. . . . .|. . . . .      .	      .	       .████████████Δv+██")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("█.        *    .                         .                               *       .  .                .  █")
    print("█   .                                                   .                         .                     █")
    print("█           .          *           .         .                 *         .                       .      █")
    print("█            .                    .                  .               .               .                  █")
    print("█              .      .          .           .                              .            *          .   █")
    print("█                                                   .           .                   .           .       █")
    print("█    .                     *               .                                                            █")
    print("█                                                 *                      .                   .          █")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    gloc = input("Where would you wish to travel, Captain?: ")
    if gloc == "moon":
        if Δv > 13340:
            print("\n You're all set for a 100km orbit around the Moon, Captain. Safe Travels!")
        if Δv < 13340:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "mars":
        if Δv > 15110:
            print("\n You're all set for a 200km orbit around Mars, Captain. Safe Travels!")
        if Δv < 15110:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "low earth orbit":
        if Δv > 9400:
            print("\n You're all set for a 250km orbit around Earth, Captain. Safe Travels!")
        if Δv < 9400:
            print("\n Sorry Captain, not with that lil thing")
            
    if gloc == "venus":
        if Δv > 16190:
            print("\n You're all set for a 400km orbit around Venus, Captain. Safe Travels!")
        if Δv < 16190:
            print("\n Sorry Captain, not with that lil thing")
            
    if gloc == "jupiter":
        if Δv > 33170:
            print("\n You're all set for a 2000km orbit around Jupiter, Captain. Safe Travels!")
        if Δv < 33170:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "saturn":
        if Δv > 27340:
            print("\n You're all set for a 2000km orbit around Saturn, Captain. Safe Travels!")
        if Δv < 27340:
            print("\n Sorry Captain, not with that lil thing")
        
    if gloc == "uranus":
        if Δv > 24010:
            print("\n You're all set for a 1000km orbit around Uranus, Captain. Safe Travels!")
        if Δv < 24010:
            print("\n Sorry Captain, not with that lil thing")

    if gloc == "neptune":
        if Δv > 24750:
            print("\n You're all set for a 1000km orbit around Neptune, Captain. Safe Travels!")
        if Δv < 24750:
            print("\n Sorry Captain, not with that lil thing")
            
    if gloc == "mercury":
        if Δv > 22480:
            print("\n You're all set for a 100km orbit around Mercury, Captain. Safe Travels!")
        if Δv < 22480:
            print("\n Sorry Captain, not with that lil thing")


#T H E   S P I C E   M U S T   F L O W

