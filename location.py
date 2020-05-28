import csv
from geopy.geocoders import Nominatim
import pandas as pd
from geopy.point import Point
geolocator = Nominatim(timeout=5)
with open('location123.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        lat=row[1]
        long=row[2]
        user_id=row[0]
        str1='"'+ lat + ',' + long + '"'
        location = geolocator.reverse(Point(lat, long))
        address=location.address
        print(location)
        df = pd.DataFrame({'id': [user_id],
                    'lat': [lat],
                    'long': [long],
                    'address':[address]
                    })
        df.to_csv('updatedlocation.csv',index=False,sep=',',header=None,mode='a+')
        # break