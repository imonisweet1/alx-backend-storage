#!/usr/bin/env python3
"""Helper function for pagination index calculation."""

from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Returns start and end indices for items on a specified page."""
    start_index = (page - 1) * page_size
    end_index = page + page_size
    return (start_index, end_index)
