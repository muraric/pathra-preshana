"""
File reading functionality for HTML templates and CSV email lists
"""

import csv
from pathlib import Path
from typing import List, Dict


class FileReader:
    """Class to read HTML templates and CSV email lists"""
    
    @staticmethod
    def read_html_template(file_path: str) -> str:
        """
        Read HTML template file
        
        Args:
            file_path: Path to HTML file
            
        Returns:
            HTML content as string
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"HTML template file not found: {file_path}")
            
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        
        except Exception as e:
            raise Exception(f"Error reading HTML template: {str(e)}")
    
    @staticmethod
    def read_csv_recipients(file_path: str) -> List[Dict[str, str]]:
        """
        Read CSV file with email recipients
        
        Expected CSV format:
        name,email
        John Doe,john@example.com
        Jane Smith,jane@example.com
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            List of dictionaries with 'name' and 'email' keys
        """
        recipients = []
        
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"CSV file not found: {file_path}")
            
            with open(path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                # Validate headers
                if "email" not in reader.fieldnames:
                    raise ValueError("CSV file must contain 'email' column")
                
                # Read rows
                for row in reader:
                    email = row.get("email", "").strip()
                    name = row.get("name", "").strip()
                    
                    if not email:
                        print(f"Warning: Skipping row with empty email: {row}")
                        continue
                    
                    recipients.append({
                        "name": name if name else email.split("@")[0],
                        "email": email
                    })
            
            print(f"✓ Successfully loaded {len(recipients)} recipients from CSV")
            return recipients
        
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")

