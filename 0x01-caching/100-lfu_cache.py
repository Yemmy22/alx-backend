#!/usr/bin/env python3
"""
A LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and
    implements a LFU caching system
    """

    def __init__(self):
        """
        Initialize LFUCache with parent attributes
        and an extra frequency dictionary
        """
        super().__init__()
        self.frequency = {}  # Track access frequency of each key
        self.usage_order = []  # Track access order of keys

    def put(self, key, item):
        """
        Add an item to the cache, with LFU eviction
        if limit is reached
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_freq_keys = [
                        k for k, v in self.frequency.items() if v == least_freq
                        ]
                lfu_key = next(
                        k for k in self.usage_order if k in least_freq_keys
                        )
                self.cache_data.pop(lfu_key)
                self.frequency.pop(lfu_key)
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve item from cache
        and update its frequency and usage order
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
