from eve import Eve
from eve.auth import BasicAuth
import requests
import pymongo
from dotenv import load_dotenv, find_dotenv
from os import environ
load_dotenv(find_dotenv())

client = pymongo.MongoClient(
    environ.get("MONGO_HOST"),
    int(environ.get("MONGO_PORT")),
    socketTimeoutMS=200
)
db = client[environ.get("MONGO_DBNAME")]
# db.authenticate(
#     environ.get("MONGO_USER"),
#     environ.get("MONGO_PASS"),
#     source='admin')

endpoints = ['stashes', 'items']

for i in endpoints:
    if i not in db.collection_names():
        db.create_collection(i)

stash_collection = db['stashes']
item_collection = db['items']


def updatedb():
    url = 'http://www.pathofexile.com/api/public-stash-tabs'
    data = requests.get(url).json()
    next_change_id = data.get('next_change_id')
    page = 1
    while next_change_id != '':
        print(len(data['stashes']))
        print(next_change_id)
        for stash in data['stashes']:
            stash_collection.update(
                {'_id': stash['id']}, dict(stash), upsert=True)
            for item in stash['items']:
                item_collection.update(
                    {'_id': item['id']}, dict(item), upsert=True)
        data = requests.get(url + '?id=' + next_change_id).json()
        next_change_id = data.get('next_change_id')
        page += 1
        if page > 3:
            break
    print('db updated')


class MyBasicAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == environ.get("MONGO_USER") and password == environ.get("MONGO_PASS")

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    #updatedb()
    app.run()
