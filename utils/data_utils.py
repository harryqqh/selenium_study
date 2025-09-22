import csv
import os
from typing import List

class DataUtils:
    """Utility class for handling test data operations."""
    
    @staticmethod
    def read_test_data_from_csv(csv_filename: str, base_path: str = None) -> List[str]:
        if base_path is None:
            # Default path: go up two levels from current file to find data directory
            current_dir = os.path.dirname(__file__)
            base_path = os.path.dirname(current_dir)
        
        csv_path = os.path.join(base_path, 'data', csv_filename)
        
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        test_data = []
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if 'keyword' not in row:
                        raise KeyError("'keyword' column not found in CSV file")
                    test_data.append(row['keyword'])
        except Exception as e:
            raise Exception(f"Error reading CSV file {csv_path}: {str(e)}")
        
        return test_data

# Convenience functions for backward compatibility
def read_test_data(csv_filename: str = 'test_data.csv') -> List[str]:
    return DataUtils.read_test_data_from_csv(csv_filename)
