<<<<<<< HEAD
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """

    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
=======
// Regex filter
db.school.find({name: /^Holberton/ })
>>>>>>> d89c46a6f6788846c614d5eb576a9ddd2ffaa0b0
