import requests
import json

class MocRepository:
    def __init__(self, url, port=80):
        self.url = url
        self.port = port

    def get(self, rurl):
        return None

class MocUsersRepository(MocRepository):
    def getUserFriends(self, user_id, token):
        js = []
        if user_id == 0:
            js = [2, 3, 10]
        else:
            return None
        return js
    
    def getUserGroups(self, user_id, token):
        js = []
        if user_id == 0:
            js = [101, 102, 103]
        elif user_id == 2:
            js = [110, 112, 133, 146]
        elif user_id == 3:
            js = [111, 114, 133, 164]
        elif user_id == 10:
            js = [103, 102, 110, 133, 146]
        else:
            return None
        return js

class MocGroupsRepository(MocRepository):
    def getGroup(self, group_id, token):
        js = {}
        if group_id == 133:
            js = [{
                    'id' : 133,
                    'name' : 'Best Group EVER'
                }]
        else:
            return None
        return js