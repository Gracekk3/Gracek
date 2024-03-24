import math


polomer_zeme_km = 6371

# Objem Země
objem_zeme_km3 = (4/3) * math.pi * (polomer_zeme_km ** 3)
print("Objem Země:", objem_zeme_km3, "km^3")

# Povrch Země
povrch_zeme_km2 = 4 * math.pi * (polomer_zeme_km ** 2)
print("Povrch Země:", povrch_zeme_km2, "km^2")
