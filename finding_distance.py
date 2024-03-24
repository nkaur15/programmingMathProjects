#Code to find the distnace between 2 cities on the map
#Use dot product and length formulas
import math 

def dot_product(v,w):
    total = 0
    if (len(v) == len(w)):
        for a,b in zip(v,w):
            total += a * b
        return total
    else:
        return None

def find_length(u):
    u_new = dot_product(u,u)

    sum_of_squared_elements = 0
    for i in u:
        sum_of_squared_elements += i

    return math.sqrt(sum_of_squared_elements)

#print(dot_product([1,1,1],[3,3,3]))
#print(find_length([0,1,0]))

def spherical_coordinates(lat,lon):
    return [(20000/math.pi)*(math.cos(lat)*math.cos(lon)),(-20000/math.pi)*(math.sin(lon)*math.cos(lat)),(20000/math.pi)*(math.sin(lat))]

print(spherical_coordinates(40.7,74))

#Part 3
def find_distance(loc1_lat,loc1_lon,loc2_lat,loc2_lon):
    location1_coord = spherical_coordinates(loc1_lat,loc1_lon)
    location2_coord = spherical_coordinates(loc2_lat,loc2_lon)

    angle = math.acos(dot_product(location1_coord,location2_coord)/(find_length(location1_coord)*find_length(location2_coord)))

    angle_rad = math.radians(angle)

    return angle_rad * (20000/math.pi)

print("New York and London: " + find_distance(40.7,74,51.5,0))
