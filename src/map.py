import webbrowser
from services import Services
import pandas as pd
import geocoder

g = geocoder.ip('me')
print(g.latlng)






# class Map(Services):
#     blocks = [""]

#     def __init__(self):
#         pass

#def get_user_location(self):
   
#     def get_blocks(self):
#         pass

# prubea = Map()
# prubea.get_user_location()
