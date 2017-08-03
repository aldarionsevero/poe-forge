from eve import Eve
from eve.auth import BasicAuth
import requests
import pymongo

connection = pymongo.MongoClient(
    'localhost',
    27017,
    socketTimeoutMS=200
)
db = connection['forge']
stash_collection = db['stashes']


def updatedb():
    url = 'http://www.pathofexile.com/api/public-stash-tabs'
    data = requests.get(url).json()
    next_change_id = data.get('next_change_id')
    page = 1
    while next_change_id != '':
        print(len(data['stashes']))
        print(next_change_id)
        for stash in data['stashes']:
            stash_collection.update({'_id': stash['id']}, dict(stash), upsert=True)
        data = requests.get(url + '?id=' + next_change_id).json()
        next_change_id = data.get('next_change_id')
        page += 1
        if page > 10:
            break
    print('db updated')


class MyBasicAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin' and password == 'admin'

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    # updatedb()
    app.run()
