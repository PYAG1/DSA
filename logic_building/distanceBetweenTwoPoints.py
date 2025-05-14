import math

def find_distance_between_two_points(x1,x2,y1,y2):
    squared_diff= math.pow(x2-x1,2) + math.pow(y2-y1,2)
    distance = math.sqrt(squared_diff)
    print(f"{distance:.6f}")

find_distance_between_two_points(3,4,7,7)