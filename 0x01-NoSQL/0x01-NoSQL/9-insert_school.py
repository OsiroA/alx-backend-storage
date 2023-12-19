<<<<<<< HEAD
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    document_id = mongo_collection.insert(kwargs)
    return document_id
=======
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    document_id = mongo_collection.insert(kwargs)
    return document_id
>>>>>>> d89c46a6f6788846c614d5eb576a9ddd2ffaa0b0
