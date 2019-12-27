import requests
import json

class Repository:
    def __init__(self, url, port=80):
        self.url = url
        self.port = port

    def get(self, id):
        pass

class UsersRepository(Repository):
    def get(self, id):
        pass

class GroupsRepository(Repository):
    def get(self, id):
        pass