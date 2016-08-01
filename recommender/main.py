from pymongo import MongoClient
from dataservice import DataService
from helper import calculate_top_5

def main():
      try:
          #get MongoDB client and set it in DataService
          client = MongoClient('localhost', 27017)
          DataService.init(client)
          #work flow
          user_download_history = DataService.retrieve_user_download_history()
          app_info = DataService.retrieve_app_info()
          for app in app_info.keys():
              calculate_top_5(app, user_download_history.values())
      except Exception as e:
          print(e)
      finally:
          #clean up work
          if 'client' in locals():
              client.close()

if __name__ == "__main__":
      main()
