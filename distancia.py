from haversine import haversine

lyon = (34.05216, 4.8422)  # (lat, lon)
paris = (48.8567, 2.3508)

print(haversine(lyon, paris))
