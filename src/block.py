from services import Services
import pandas as pd

data = pd.read_csv('src/resources/csvfile.csv')
print(data.head(6))
class Block:
    name = ""
    latitude = ""
    longitude = ""
    description = ""
    pictures = [""]

    def dispaly()->str:
        pass
    
    def get_location()->list:
        pass
