# coding: utf-8

import itertools
import json
import csv
from typing import List, Iterator, Any, Optional
from pathlib import Path


class CartesianProductError(Exception):
    """Error related to Cartesian product calculation"""
    pass


class CartesianProduct:
    MAX_ARRAYS = 20
    
    def __init__(self):
        """Initialize CartesianProduct calculator"""
        pass

    def _validate_input(self, arrays: List[List[Any]]) -> None:
        """Validate input arrays

        Args:
            arrays (List[List[Any]]): List of input arrays

        Raises:
            CartesianProductError: When validation fails
        """
        if not arrays:
            raise CartesianProductError("Input arrays are empty")
        
        if len(arrays) > self.MAX_ARRAYS:
            raise CartesianProductError(f"Number of arrays exceeds limit ({self.MAX_ARRAYS})")
        
        if any(not arr for arr in arrays):
            raise CartesianProductError("Empty array found in input")

        # Basic size validation
        total_combinations = 1
        for arr in arrays:
            total_combinations *= len(arr)
            if total_combinations > 10**8:  # Arbitrary limit to prevent memory issues
                raise CartesianProductError("Estimated result size is too large")

    def iterate(self, arrays: List[List[Any]]) -> Iterator[List[Any]]:
        """Generate Cartesian product as a memory-efficient iterator

        Args:
            arrays (List[List[Any]]): List of input arrays

        Yields:
            Iterator[List[Any]]: Each combination in the Cartesian product
        """
        self._validate_input(arrays)
        yield from itertools.product(*arrays)

    def execute(self, arrays: List[List[Any]]) -> List[List[Any]]:
        """Calculate Cartesian product

        Args:
            arrays (List[List[Any]]): List of input arrays

        Returns:
            List[List[Any]]: Result of Cartesian product
        """
        self._validate_input(arrays)
        return list(self.iterate(arrays))

    def to_csv(self, result: List[List[Any]], output_path: str) -> None:
        """Export result to CSV file

        Args:
            result (List[List[Any]]): Cartesian product result
            output_path (str): Output file path
        """
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for i, row in enumerate(result):
                writer.writerow([i] + list(row))

    def to_json(self, result: List[List[Any]], output_path: str) -> None:
        """Export result to JSON file

        Args:
            result (List[List[Any]]): Cartesian product result
            output_path (str): Output file path
        """
        indexed_result = {str(i): list(row) for i, row in enumerate(result)}
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(indexed_result, f, ensure_ascii=False, indent=2)

    def display(self, result: List[List[Any]], limit: int = None) -> None:
        """Display results to console

        Args:
            result (List[List[Any]]): Cartesian product result
            limit (int, optional): Maximum number of results to display
        """
        for i, combination in enumerate(result):
            if limit is not None and i >= limit:
                print("...")
                break
            print(f"{i}: {combination}")
