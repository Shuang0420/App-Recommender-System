import operator
from dataservice import DataService
import math

class Helper(object):
    @classmethod
    def cosine_similarity(cls, app_list1, app_list2):
        match_count = cls.__count_match(app_list1, app_list2)
        return float(match_count) / math.sqrt( len(app_list1) * len(app_list2))

    @classmethod
    def __count_match(cls, list1, list2):
        count = 0
        for element in list1:
            if element in list2:
                count += 1
        return count

def calculate_top_5(app, user_download_history):
    '''
    cosine_similarity between an App and user's history
    '''
    #create a dict to store each other app and its similarity to this app
    app_similarity = {}#{app_id: similarity}
    for apps in user_download_history:
        #calculate the similarity
        similarity = Helper.cosine_similarity([app], apps)
        # accumluate similarity
        for other_app in apps:
            if app_similarity.has_key(other_app):
                app_similarity[other_app] = app_similarity[other_app] + similarity
            else:
                app_similarity[other_app] = similarity

    # There could be app without related apps (not in any download history)
    if not app_similarity.has_key(app):
        return

    #sort app_similarity dict by value and get the top 5 as recommendation
    app_similarity.pop(app)
    sorted_tups = sorted(app_similarity.items(), key=operator.itemgetter(1), reverse=True)#sort by similarity
    top_5_app = [sorted_tups[0][0], sorted_tups[1][0], sorted_tups[2][0], sorted_tups[3][0], sorted_tups[4][0]]
    #print("top_5_app for " + str(app) + ":\t" + str(top_5_app))

    #store the top 5
    DataService.update_app_info({'app_id': app}, {'$set': {'top_5_app': top_5_app}})
