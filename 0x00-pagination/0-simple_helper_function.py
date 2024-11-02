#!/usr/bin/env python3
"""
An index_range function module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start
    and end indexes for a page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
