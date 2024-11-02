#!/usr/bin/env python3
"""
A MRUCache class module.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Defines a caching system with MRU eviction policy.
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds MAX_ITEMS,
        remove the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recent_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """
        Get an item by key from the cache.
        Updates the usage order if the key exists.
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
