from mailjet_rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


mailjet_sender_email = os.getenv("MAILJET_SENDER_EMAIL")
api_key = os.getenv("MAILJET_API_KEY")
api_secret = os.getenv("MAILJET_API_SECRET")

mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def send_mailjet_email(to_email, to_name):
    """
    Send an email using Mailjet API.
    
    Args:
        to_email (str): Recipient email address
        to_name (str): Recipient name
    """
    data = {
        'Messages': [
            {
                "From": {
                    "Email": mailjet_sender_email,  # replace with your Mailjet verified sender
                    "Name": "Automated System"
                },
                "To": [
                    {
                        "Email": to_email,
                        "Name": to_name
                    },
                ],
                "Subject": "Purchase Report",
                "TextPart": "Thank you for buying from us.",
                "HTMLPart": """
                    <h3>Thank you for buying from us.</h3>
                """
            }
        ]
    }

    try:
        result = mailjet.send.create(data=data)
        print("Status:", result.status_code)
        print("Response:", result.json())
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
