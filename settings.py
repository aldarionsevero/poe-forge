# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
from dotenv import load_dotenv, find_dotenv
from os import environ
load_dotenv(find_dotenv())

MONGO_HOST = environ.get("MONGO_HOST")
MONGO_PORT = int(environ.get("MONGO_PORT"))

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = environ.get("MONGO_USER")
MONGO_PASSWORD = environ.get("MONGO_PASS")
MONGO_AUTH_SOURCE = environ.get("MONGO_USER")

XML = False
JSON = True
X_DOMAINS = '*'

MONGO_DBNAME = environ.get("MONGO_DBNAME")
CACHE_EXPIRES = 10
PAGINATION_LIMIT = 1000
PAGINATION_DEFAULT = 200

forge_schema = {
    'accountName': {'type': 'string'},
    'id': {'type': 'objectid'},
    'items': {
        'type': 'list',
        'schema': {
            'additionalProperties': {'type': 'list'},
            'artFilename': {'type': 'string'},
            'corrupted': {'type': 'boolean'},
            'craftedMods': {'type': 'string'},
            'descrText': {'type': 'string'},
            'duplicated': {'type': 'boolean'},
            'explicitMods': {'type': 'list'},
            'flavourText': {'type': 'list'},
            'frameType': {'type': 'integer'},
            'h': {'type': 'integer'},
            'icon': {'type': 'string'},
            'id': {'type': 'string'},
            'identified': {'type': 'boolean'},
            'ilvl': {'type': 'integer'},
            'implicitMods': {'type': 'list'},
            'inventoryId': {'type': 'string'},
            'league': {'type': 'string'},
            'lockedToCharacter': {'type': 'boolean'},
            'maxStackSize': {'type': 'integer'},
            'name': {'type': 'string'},
            'note': {'type': 'string'},
            'properties': {'type': 'list'},
            'requirements': {'type': 'list'},
        },
    },
    'lastCharacterName': {'type': 'string'},
    'public': {'type': 'boolean'},
    'stash': {'type': 'string'},
    'stashType': {'type': 'string'},
}


stash = {
    'schema': forge_schema,
    # 'id_field': 'accountName'
    # 'url': 'stash'

}

item = {

    'schema': forge_schema.get('items', {}).get('schema', {}),
    # 'id_field': 'accountName'
    # 'url': 'item'

}


DOMAIN = {
    'stashes': stash,
    'items': item,
}
