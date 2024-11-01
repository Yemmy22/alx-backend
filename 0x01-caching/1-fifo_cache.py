#!/usr/bin/env python3
"""
A FIFOCache module.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a cache with a FIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache and keep track of the order of keys.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item into the cache using FIFO.
        If the cache exceeds its limit, the oldest item is removed.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item by key.
        Returns None if the key is not in the cache.
        """
        return self.cache_data.get(key, None)
