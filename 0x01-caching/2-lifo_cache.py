#!/usr/bin/env python3
"""
A LIFOCache class module.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a cache with a LIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache and keep
        track of the most recent key.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache using LIFO.
        If the cache exceeds its limit, the last added item is removed.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Get an item by key.
        Returns None if the key is not in the cache.
        """
        return self.cache_data.get(key, None)
