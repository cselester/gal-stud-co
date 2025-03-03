import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# WhatsApp API Configuration
WHATSAPP_API_VERSION = "v17.0"
BASE_URL = f"https://graph.facebook.com/{WHATSAPP_API_VERSION}"
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
BUSINESS_ACCOUNT_ID = os.getenv("BUSINESS_ACCOUNT_ID")

# Message Configuration
BATCH_SIZE = 100
DELAY_BETWEEN_MESSAGES = 1  # seconds
DELAY_BETWEEN_BATCHES = 60  # seconds

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'logs/whatsapp_sender.log' 