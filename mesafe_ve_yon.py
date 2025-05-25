#iki nokta arasindaki mesafe ve bu noktalar arasindaki kuzeye gore olan aci
#Dünya’nın yarıçapı (6371 km veya 6.371.000 m)
#Radyan ↔ Derece dönüşümü
#Haversine formülü (iki konum arası mesafe)
#Bearing açısı formülü

import math 

R = 6371e3 #metre cinsinden 

def distance_bearing(homeLatitude,homeLongitude,destinationLatitude,destinationLongitude): #latitude:enlem longitude:boylam
    #derece cinsinden gelen enlem ve boylam radyana cevrilir
    rlat1 = homeLatitude * (math.pi/180) 
    rlat2 = destinationLatitude * (math.pi/180) 
    rlon1 = homeLongitude * (math.pi/180) 
    rlon2 = destinationLongitude * (math.pi/180) 

    #iki konum arasindaki farklar(radyan cinsinden)
    dlat = (destinationLatitude - homeLatitude) * (math.pi/180)
    dlon = (destinationLongitude - homeLongitude) * (math.pi/180)

    #haversine formulu(mesafe hesabi)
    a = (math.sin(dlat/2) * math.sin(dlat/2)) + (math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon/2) * math.sin(dlon/2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    #Bearing (Yön) Açısı Hesabı
    y = math.sin(rlon2 - rlon1) * math.cos(rlat2)
    x = math.cos(rlat1) * math.sin(rlat2) - math.sin(rlat1) * math.cos(rlat2) * math.cos(rlon2 - rlon1)
    bearing = math.atan2(y, x)
    bearingDegrees = bearing * (180/math.pi)

    out = [distance,bearingDegrees]
    return out

def main():
    distance_brng = []

    #kullanicidan degerleri alma
    print ("+++++++++++++ Please Enter the values in decimals +++++++++++++")
    print ("Enter the Latitude of Current location: ")
    lat1 = float(input())
    print ("Enter the Longitude of Current location: ")
    lon1 = float(input())
    print ("Enter the Latitude of Destination: ")
    lat2 = float(input())
    print ("Enter the Longitude of Destination: ")
    lon2 = float(input())


    dist_brng = distance_bearing(lat1, lon1, lat2, lon2)


    print ('Distance between the home and destination is ', dist_brng[0], 'm')
    print ('Bearing angle between home and destination is ', dist_brng[1], 'degree')

main()