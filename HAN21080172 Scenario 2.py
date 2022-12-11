# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:27:53 2022

@author: Harry
"""
#create a list for every possible route
deliver_routes_list = []

#main function
def Shortest_path(waypoint, destinations, route, distance):
    route.append(waypoint)

    #Calculation for the length from current to last waypoint
    if len(route) > 1:
        distance = distance + destinations[route[-2]][waypoint]

    if (len(destinations) == len(route)) and (route[0] in destinations[route[-1]]):
        route.append(route[0])
        distance = distance + destinations[route[-2]][route[0]]
        print (route, distance)
        deliver_routes_list.append([distance, route])
        return

    for a in destinations:
        if (a not in route) and (waypoint in destinations[a]):
            Shortest_path(a, dict(destinations), list(route), distance)

#ROUTE INPUT
if __name__ == '__main__':
    destinations = {
        'A': {'B': 10, 'C': 15, 'D': 20, 'E': 30},
        'B': {'A': 10, 'C': 25, 'D': 30, 'E': 35},
        'C': {'A': 15, 'B': 25, 'D': 20, 'E': 10},
        'D': {'A': 20, 'B': 30, 'C': 20, 'E': 15},
        'E': {'A': 30, 'B': 35, 'C': 10, 'D': 15},   
    }

#Sort and Output Final schedule
    Shortest_path('A', destinations, [], 0)
    deliver_routes_list.sort()
    if len(deliver_routes_list) != 0:
        print ("Optimum route is: %s" % deliver_routes_list[0])
