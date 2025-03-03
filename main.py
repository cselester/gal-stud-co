import logging
from src.message_sender import WhatsAppMessageSender
from src.utils import load_phone_numbers
from config.config import *
import time

def main():
    # Initialize logger
    logging.basicConfig(
        format=LOG_FORMAT,
        level=logging.INFO,
        filename=LOG_FILE
    )
    logger = logging.getLogger(__name__)

    # Initialize message sender
    sender = WhatsAppMessageSender()

    # Load phone numbers
    phone_numbers = load_phone_numbers('data/phone_numbers.csv')
    
    if not phone_numbers:
        logger.error("No valid phone numbers found")
        return

    # Your promotional message
    message = """Hello! Check out our latest promotion:
🌟 Special Offer: [Details]
Valid until: [Date]
Contact us for more information!"""

    # Process in batches
    total = len(phone_numbers)
    success_count = 0
    failure_count = 0

    for i in range(0, total, BATCH_SIZE):
        batch = phone_numbers[i:i + BATCH_SIZE]
        logger.info(f"Processing batch {i//BATCH_SIZE + 1}")
        
        for phone in batch:
            if sender.send_message(phone, message):
                success_count += 1
            else:
                failure_count += 1
            time.sleep(DELAY_BETWEEN_MESSAGES)
        
        # Delay between batches
        if i + BATCH_SIZE < total:
            time.sleep(DELAY_BETWEEN_BATCHES)

    logger.info(f"Campaign completed. Successful: {success_count}, Failed: {failure_count}")

if __name__ == "__main__":
    main() 