import math
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)

# Take a list of lat/lon coords and extract out the easting and northing vectors (in m)
# NOTE: For the purposes of this exercise we can ignore differing zone letters and numbers
def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)
    return total_distance

def calc_distance(coordinate1, coordinate2):
    dx = coordinate2[0] - coordinate1[0]
    dy = coordinate2[1] - coordinate1[1]
    return math.sqrt(dx*dx + dy*dy)

def sorted_indices(coordinates, starting_index):
    def sorted_coords(coordinates, starting_index):
        temp_coords = coordinates.copy()
        # Sorts the list by it's distance to the provided starting index
        temp_coords.sort(key=lambda coord : calc_distance(coordinates[starting_index], coord)) 
        return temp_coords
    sorted_indices = []
    for coord in sorted_coords(coordinates, starting_index):
        # TODO add each index of a duplicate (can't simply remove them because there are len() tests).
        #      Remember for each duplicate coord, this for loop will repeat
        sorted_indices.append(coordinates.index(coord))
    return sorted_indices


def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))

    ############ DEBUG ############
    for index in indices:
        print("Coordinates: ", coordinates[index])
        print("Distance to start-point (index 0): ", calc_distance(coordinates[0], coordinates[index]))
    ###############################

    optimal_start_index = 0
    smallest_distance = -1
    for index in indices: # Tries every index for the best starting index to sort the list by.
        dist = calc_total_distance(coordinates_xy, sorted_indices(coordinates, index))
        if dist > smallest_distance:
            smallest_distance = dist
            optimal_start_index = index

    optimal_order_indices = sorted_indices(coordinates, optimal_start_index)

    ############ DEBUG ############
    print("-----------------")
    print("Optimal start index: ", optimal_start_index)
    for index in optimal_order_indices:
        print("Index: ", index)
        print("Sorted coordinates: ", coordinates[index])
        print("Distance to start-point: ", calc_distance(coordinates[optimal_start_index], coordinates[index]))
    ###############################  
        
    return optimal_order_indices