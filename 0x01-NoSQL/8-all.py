#!/usr/bin/env python3
"""Python function that lists all documents in a collection."""


def list_all(mongo_collection):
    """Function that lists all documents in a collection:"""
    docs = []
    for document in mongo_collection.find():
        docs.append(document)
    return docs
