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
    # TODO Still not optimal
    indices = list(range(len(coordinates)))
    sorted_indices = []
    while True:
        indices.sort(key=lambda index : calc_distance(coordinates[starting_index], coordinates[index])) # sort coordinates by it's distance to starting_index
        sorted_indices += indices[:2] # add first 2 indices
        indices = indices[2 - len(indices):] # remove first 2 indices
        starting_index = sorted_indices[-1] # set to last index in sorted_indices
        if (len(sorted_indices) == len(coordinates)):
            break
    return sorted_indices


def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    optimal_start_index = 0

    ############ DEBUG ############
    print("####### BEFORE #######")
    print("Index starting at: ", optimal_start_index)
    debug(indices, coordinates, coordinates_xy, optimal_start_index)
    ###############################


    smallest_distance = -1
    for index in indices: # Tries every index for the best starting index to sort the list by.
        dist = calc_total_distance(coordinates_xy, sorted_indices(coordinates, index))
        if dist > smallest_distance:
            smallest_distance = dist
            optimal_start_index = index

    optimal_order_indices = sorted_indices(coordinates, optimal_start_index)

    ############ DEBUG ############
    print("####### AFTER #######")
    print("Optimal start index: ", optimal_start_index)
    debug(optimal_order_indices, coordinates, coordinates_xy, optimal_start_index)    
    ###############################  
        
    return optimal_order_indices

def debug(indices, coordinates, coordinates_xy, optimal_start_index):
    for index in indices:
        print("Index: ", index)
        print("Coordinates: ", coordinates[index])
    print("Total distance: ", calc_total_distance(coordinates_xy, sorted_indices(coordinates, optimal_start_index)))