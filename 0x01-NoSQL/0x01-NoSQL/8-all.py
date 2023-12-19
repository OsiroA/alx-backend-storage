<<<<<<< HEAD
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def list_all(mongo_collection):
    """ List all documents in Python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
=======
#!/usr/bin/env python3
"""
List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all doc in a collection
    """
    if mongo_collection is not None:
        return list(mongo_collection.find())
    else:
        return []
>>>>>>> d89c46a6f6788846c614d5eb576a9ddd2ffaa0b0
