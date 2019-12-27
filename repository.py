import requests
import json

class Repository:
    def __init__(self, url, port=80):
        self.url = url
        self.port = port

    def get(self, rurl):
        try:
            response = requests.get(rurl)
            js = json.loads(response.text)
            return js
        except:
            return None

class UsersRepository(Repository):
    def getUserFriends(self, user_id, token):
        rurl = self.url + 'method/friends.get?user_id=' + str(user_id) + '&v=5.61&access_token=' + token
        res = self.get(rurl)
        try:
            return res['response']['items']
        except:
            return None
    
    def getUserGroups(self, user_id, token):
        rurl = self.url + 'method/groups.get?user_id=' + str(user_id) + '&v=5.61&access_token=' + token
        res = self.get(rurl)
        try:
            return res['response']['items']
        except:
            return None

class GroupsRepository(Repository):
    def getGroup(self, group_id, token):
        rurl = self.url + 'method/groups.getById?group_id=' + str(group_id) + '&v=5.61&access_token=' + token
        res = self.get(rurl)
        try:
            return res['response']
        except:
            return None