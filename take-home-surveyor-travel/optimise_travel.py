import math
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)

# Take a list of lat/lon coords and extract out the easting and northing vectors (in m)
def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)
    return total_distance

def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    
    # TODO Devise an algorithm to optimise the order
    
    return indices
