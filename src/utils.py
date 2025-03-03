import pandas as pd
import logging
from typing import List

logger = logging.getLogger(__name__)

def load_phone_numbers(file_path: str) -> List[str]:
    """Load phone numbers from CSV file"""
    try:
        df = pd.read_csv(file_path)
        phone_numbers = df['phone_number'].astype(str).tolist()
        return validate_phone_numbers(phone_numbers)
    except Exception as e:
        logger.error(f"Error loading phone numbers: {str(e)}")
        return []

def validate_phone_numbers(phone_numbers: List[str]) -> List[str]:
    """Validate and format phone numbers"""
    validated = []
    for phone in phone_numbers:
        # Remove any spaces or special characters
        cleaned = ''.join(filter(str.isdigit, phone))
        
        # Ensure proper format
        if len(cleaned) >= 10:
            if not cleaned.startswith('+'):
                cleaned = '+' + cleaned
            validated.append(cleaned)
        else:
            logger.warning(f"Invalid phone number: {phone}")
    
    return validated 