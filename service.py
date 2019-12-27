import repository
import mocrepository

class Service:
    def __init__(self, usersrep : repository.UsersRepository, groupsrep : repository.GroupsRepository):
        self.usersrep = usersrep
        self.groupsrep = groupsrep
    
    def find_the_most_popular_friends_group(self, user_id, token):
        res = dict()
        friends_ids = self.usersrep.getUserFriends(user_id, token)
        for friend in friends_ids:
            groups_ids = self.usersrep.getUserGroups(friend, token)
            for group in groups_ids:
                if group in res:
                    res[group] += 1
                else:
                    res[group] = 1
        max = 1
        groups = []
        for i in res.keys():
            if res[i] > max:
                groups = [i]
                max = res[i]
            elif res[i] == max:
                groups.append(i)
        strgrps = ''
        for g in groups:
            strgrps += str(g) + ','
        strgrps = strgrps[0:-1]
        res = self.groupsrep.getGroup(strgrps, token)
        return res