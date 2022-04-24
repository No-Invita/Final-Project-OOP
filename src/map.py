import webbrowser
from services import Services
import pandas as pd


#data_xls = pd.read_excel('src/resources/data.xlsx')
#data = data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)
data = pd.read_csv('src/resources/csvfile.csv')
print(data.head(6))

# class Map(Services):
#     blocks = [""]

#     def __init__(self):
#         pass

#     def get_user_location(self):
#webbrowser.open(
    #'http://www.openstreetmap.org/?mlat=1101975&mlon=-7485094&zoom=12')

#     def get_blocks(self):
#         pass

# prubea = Map()
# prubea.get_user_location()
