import requests
import json
import time
import logging
from typing import List, Tuple, Dict
from config.config import *

logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    filename=LOG_FILE
)

logger = logging.getLogger(__name__)

class WhatsAppMessageSender:
    def __init__(self):
        self.base_url = f"{BASE_URL}/{BUSINESS_ACCOUNT_ID}/messages"
        self.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

    def send_message(self, phone_number: str, message: str) -> bool:
        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "text",
            "text": {"body": message}
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            if response.status_code == 200:
                logger.info(f"Message sent successfully to {phone_number}")
                return True
            else:
                logger.error(f"Failed to send message to {phone_number}: {response.text}")
                return False
        except Exception as e:
            logger.error(f"Error sending message to {phone_number}: {str(e)}")
            return False

    def send_template_message(self, phone_number: str, template_name: str, 
                            template_params: List[Dict]) -> bool:
        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": "en"},
                "components": [
                    {
                        "type": "body",
                        "parameters": template_params
                    }
                ]
            }
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error sending template message: {str(e)}")
            return False 