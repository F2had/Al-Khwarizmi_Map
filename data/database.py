from data.database_builder import get_latlon
from data.graph import GraphPoint, connect_points, MODE_BUS, MODE_WALKING, MODE_TRAIN, MODE_CAR, ConnectionCacheHolder
from os import path

points_names = [
    'Sunway Pyramid',
    'UM CENTRAL',
    'Mid Valley Megamall',
    'KL Sentral',
    'National Mosque of Malaysia',
    'Kuala Lumpur City Centre',
    'Menara Kuala Lumpur',
    'Kuala Lumpur International Airport',

    'Masjid Al-Husna',
    'Asia Jaya Station',
    'Ppum Federal',
    'KL 1102 Masjid Ar-Rahman UM',
    'Lrt Station Universiti',
    'LRT Kerinchi',
    'Pantai Hill Park',
    'LRT Abdullah Hukum',
    'Kuala Lumpur Station',

]

points = {}

# load cache
if path.isfile('cache_points'):
    with open('cache_points', 'r') as cache_file:
        for line in cache_file:
            point = eval(line)
            if point.name in points_names:
                points[point.name] = point

# build the real points data collection
# only build points that are not present in the cache
with open('cache_points', 'w') as cache_file:
    for point_n in points_names:
        if point_n not in points:
            latlon = list(get_latlon(point_n))
            points[point_n] = GraphPoint(point_n, latlon[0], latlon[1])
            print(f'geocode: {point_n}')
        print(points[point_n], file=cache_file)

# Connections building

# initialize connection cache holder:
cache = ConnectionCacheHolder('cache_connections')

# walking

connect_points(points['Sunway Pyramid'], points['Masjid Al-Husna'], MODE_WALKING, cache)
connect_points(points['KL 1102 Masjid Ar-Rahman UM'], points['UM CENTRAL'], MODE_WALKING, cache)

connect_points(points['KL 1102 Masjid Ar-Rahman UM'], points['Lrt Station Universiti'], MODE_WALKING, cache)
connect_points(points['Lrt Station Universiti'], points['LRT Kerinchi'], MODE_WALKING, cache)
connect_points(points['LRT Abdullah Hukum'], points['Mid Valley Megamall'], MODE_WALKING, cache)
connect_points(points['Kuala Lumpur Station'], points['National Mosque of Malaysia'], MODE_WALKING, cache)
connect_points(points['National Mosque of Malaysia'], points['Kuala Lumpur City Centre'], MODE_WALKING, cache)

# bus
connect_points(points['Masjid Al-Husna'], points['Asia Jaya Station'], MODE_BUS, cache)
connect_points(points['Asia Jaya Station'], points['Ppum Federal'], MODE_BUS, cache)
connect_points(points['Ppum Federal'], points['KL 1102 Masjid Ar-Rahman UM'], MODE_BUS, cache)

connect_points(points['UM CENTRAL'], points['Lrt Station Universiti'], MODE_BUS, cache)
connect_points(points['Lrt Station Universiti'], points['Mid Valley Megamall'], MODE_BUS, cache)
connect_points(points['UM CENTRAL'], points['Pantai Hill Park'], MODE_BUS, cache)
connect_points(points['Pantai Hill Park'], points['LRT Abdullah Hukum'], MODE_BUS, cache)

connect_points(points['Ppum Federal'], points['Mid Valley Megamall'], MODE_BUS, cache)
connect_points(points['Mid Valley Megamall'], points['KL Sentral'], MODE_BUS, cache)
connect_points(points['KL Sentral'], points['Kuala Lumpur Station'], MODE_BUS, cache)
connect_points(points['Kuala Lumpur City Centre'], points['Menara Kuala Lumpur'], MODE_BUS, cache)

# car
connect_points(points['Masjid Al-Husna'], points['Asia Jaya Station'], MODE_CAR, cache)
connect_points(points['Asia Jaya Station'], points['Ppum Federal'], MODE_CAR, cache)
connect_points(points['Ppum Federal'], points['KL 1102 Masjid Ar-Rahman UM'], MODE_CAR, cache)

connect_points(points['UM CENTRAL'], points['Lrt Station Universiti'], MODE_CAR, cache)
connect_points(points['Lrt Station Universiti'], points['Mid Valley Megamall'], MODE_CAR, cache)
connect_points(points['UM CENTRAL'], points['Pantai Hill Park'], MODE_CAR, cache)
connect_points(points['Pantai Hill Park'], points['LRT Abdullah Hukum'], MODE_CAR, cache)

connect_points(points['Ppum Federal'], points['Mid Valley Megamall'], MODE_CAR, cache)
connect_points(points['Mid Valley Megamall'], points['KL Sentral'], MODE_CAR, cache)
connect_points(points['KL Sentral'], points['Kuala Lumpur Station'], MODE_CAR, cache)
connect_points(points['Kuala Lumpur City Centre'], points['Menara Kuala Lumpur'], MODE_CAR, cache)

# LRT train
connect_points(points['Asia Jaya Station'], points['Lrt Station Universiti'], MODE_TRAIN, cache)
connect_points(points['Lrt Station Universiti'], points['LRT Kerinchi'], MODE_TRAIN, cache)
connect_points(points['LRT Kerinchi'], points['LRT Abdullah Hukum'], MODE_TRAIN, cache)
connect_points(points['LRT Abdullah Hukum'], points['KL Sentral'], MODE_TRAIN, cache)
connect_points(points['KL Sentral'], points['Kuala Lumpur City Centre'], MODE_TRAIN, cache)
connect_points(points['KL Sentral'], points['Kuala Lumpur International Airport'], MODE_TRAIN, cache)

# save the cache in the file
# do it after all connections has been recorded
cache.save_cache()
