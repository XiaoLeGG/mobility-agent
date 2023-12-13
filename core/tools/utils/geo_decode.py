import sqlite3
import pandas as pd


def decode(latitude : float, longitude : float) -> tuple:
    conn = sqlite3.connect('beijing_poi.db')

    cursor = conn.cursor()

    result = cursor.execute('select * from beijing_poi where latitude >= ' + str(latitude - 0.001) + ' and latitude <= ' + str(latitude + 0.001) + ' and longitude >= ' + str(longitude - 0.001) + ' and longitude <= ' + str(longitude + 0.001))
    
    min_distance = 999999999
    poi = None
    for row in result:
        distance = (row[3] - latitude) ** 2 + (row[4] - longitude) ** 2
        if distance < min_distance:
            min_distance = distance
            poi = row

    conn.close()

    return poi