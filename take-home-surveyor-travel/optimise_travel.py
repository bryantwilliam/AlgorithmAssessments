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

def nearest_neighbor_sort(coordinates, starting_index):
    n = len(coordinates)
    visited = [False] * n
    sorted_indices = [starting_index]
    visited[starting_index] = True

    while len(sorted_indices) < n:
        current_index = sorted_indices[-1]
        min_distance = float('inf')
        next_index = None

        for i in range(n):
            if not visited[i]:
                distance = calc_distance(coordinates[current_index], coordinates[i])
                if distance < min_distance:
                    min_distance = distance
                    next_index = i

        if next_index is not None:
            sorted_indices.append(next_index)
            visited[next_index] = True

    return sorted_indices

def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    
    smallest_distance = float('inf')
    best_sorted_indices = None

    for index in indices:
        sorted_indices = nearest_neighbor_sort(coordinates_xy, index)
        dist = calc_total_distance(coordinates_xy, sorted_indices)
        if dist < smallest_distance:
            smallest_distance = dist
            best_sorted_indices = sorted_indices

    return best_sorted_indices