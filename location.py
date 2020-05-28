import csv
from geopy.geocoders import Nominatim
import pandas as pd
from geopy.point import Point
geolocator = Nominatim(timeout=5)
count=0
with open('updatedlocation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        count=count+1
        print(count)
        lat=row[1]
        long=row[2]
        user_id=row[0]
        str1='"'+ lat + ',' + long + '"'
        location = geolocator.reverse(Point(lat, long))
        address=location.address
        print(location.raw)
        try:
            city=location.raw['address']['city']
        except:
            city=''
        df = pd.DataFrame({'id': [user_id],
                    'lat': [lat],
                    'long': [long],
                    'address':[address],
                    'city':[city]

                    })
        df.to_csv('updatedlocation12.csv',index=False,sep=',',header=None,mode='a+')
        # break
