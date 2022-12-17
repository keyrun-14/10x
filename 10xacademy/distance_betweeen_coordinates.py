# # # Import math Library
# # import math 

# # p = [3] 
# # q = [1] 

# # # Calculate Euclidean distance
# # print (math.dist(p, q))

# # p = [17.6868, 83.2185] 
# # q = [,  77.1025] 

# # # Calculate Euclidean distance
# # print (math.dist(p, q))
# import mpu

# # Point one
# lat1 = 17.6868
# lon1 =  83.2185

# # Point two
# lat2 = 28.7041
# lon2 = 77.1025

# # What you were looking for
# dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
# print(dist)  # gives 278.45817507541943.
# from math import sin, cos, sqrt, atan2, radians

# # approximate radius of earth in km
# R = 6373.0

# # lat1 = radians(52.2296756)
# # lon1 = radians(21.0122287)
# # lat2 = radians(52.406374)
# # lon2 = radians(16.9251681)
# # Point one
# lat1 = radians(28.6139)
# lon1 =  radians(77.2090)

# # Point two
# lat2 = radians(17.6868)
# lon2 = radians(83.2185)

# dlon = lon2 - lon1
# dlat = lat2 - lat1

# a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
# c = 2 * atan2(sqrt(a), sqrt(1 - a))

# distance = R * c

# print("Result:", distance)
# print("Should be:", 278.546, "km")
a=int("15.9879")
print(a)