#!/usr/bin/env python3
"""
A BasicCache class module.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a basic caching system that does not have a limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If either `key` or `item` is None,
        this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Returns None if the key is not in the cache.
        """
        return self.cache_data.get(key, None)
