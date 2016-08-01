from pymongo import MongoClient
import random

# about data
class DataService(object):
    @classmethod
    def init(cls, client):
        cls.client = client
        cls.db = client.appstore
        cls.user_download_history = cls.db.user_download_history
        cls.app_info = cls.db.app_info

    @classmethod
    def retrieve_user_download_history(cls, filter_dict={}):
        #return a dict {user_id: download_history} containing user download history data
        #return all data in the collection if no filter is specified
        result = {}
        cursor = cls.user_download_history.find(filter_dict)
        for user_download_history in cursor:
            result[user_download_history['user_id']] = user_download_history['download_history']
        return result

    @classmethod
    def retrieve_app_info(cls, filter_dict={}):
        #return a dict {app_id: {app_name, top_5_app}} containing user download history data
        #return all data in the collection if no filter is specified
        result = {}
        cursor = cls.app_info.find(filter_dict)
        for app_info in cursor:
            app_id = app_info['app_id']
            title = app_info['title']
            result[app_id] = {'title': title}
        return result

    @classmethod
    def update_app_info(cls, filter_dict, update):
        cls.app_info.update_one(filter_dict, update, True)
