#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class paginates a database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server with dataset and
        indexed dataset set to None.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        Returns: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the indexed dataset,
        ensuring deletion resilience.
        Returns A dictionary containing the index,
        data, page size, and next index.
        """
        assert 0 <= index < len(self.__indexed_dataset), "Index out of range"

        # Create the response dictionary
        response = {
            'index': index,
            'page_size': page_size,
            'data': [],
            'next_index': index + page_size
        }

        # Collect data for the requested page
        for i in range(index, index + page_size):
            # Find the next valid index
            while i not in self.__indexed_dataset:
                i += 1
            response['data'].append(self.__indexed_dataset[i])

        return response
