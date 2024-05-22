# Finding locations to multiple places at the same time from single origin
# Used for finding locations to driving schools. Just for fun
import geopy.distance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://azdot.gov/mvd/services/driver-services/authorized-third-party-driver-license-locations')[0]
# refercen location on maps : https://adot.maps.arcgis.com/apps/View/index.html?appid=c8157fc5cef549a6b33833fad1e7d7c1
x = 0
# for i in table_MN:
# 	# print("x", x,":", i)
# 	x+=1
# 	print(i[1])
print(table_MN)

table_MN['distance'] = -1
distances = [-1,-1]
fout = open("out.csv","w")
for i in range(2,len(table_MN)):
	# print(table_MN.iloc[i])
	# Define the addresses
	address1 = str(table_MN.iloc[i][1])
	address2 = "1151 S Forest Ave, Tempe, AZ" # ASU address

	# Get the coordinates of the addresses
	print("address1" , address1)
	try:
		coordinates1 = geopy.geocoders.Nominatim(user_agent="http-ehavugi").geocode(address1).raw
		coordinates2 = geopy.geocoders.Nominatim(user_agent="http-ehavugi").geocode(address2).raw

		# Calculate the distance between the two addresses
		coordinates1  = (coordinates1['lat'],coordinates1['lon'])
		coordinates2  = (coordinates2['lat'],coordinates2['lon'])

		print(coordinates1, coordinates2)
		import geopy.distance


		print (geopy.distance.geodesic(coordinates1, coordinates2).miles)
		distance = geopy.distance.distance(coordinates1, coordinates2).miles

		# Print the distance
		table_MN.iloc[i]['distance'] = distance
		time.sleep(1)
		print(f"The distance between {address1} and {address2} is {distance} miles.")
		distances.append(distance)
		fout.write(f"{i},{distance}\n")

	except:
		pass
		table_MN.iloc[i]['distance'] = -1
		fout.write(f"{i},-1\n")

		distances.append(-1)

fout.close()


table_MN['distance2'] = distances
table_MN.to_csv("data.csv")