import uuid
import requests
import base64
from auth_util import generate_pair, generate_nonce
from config import BIZ_ID, BUSINESS_CHAT_SERVER, IMESSAGE_EXTENSION_BID
from jwt_util import get_jwt_token
def authenticate_user(opaque_id):
    """Form an authenticate JSON payload using the parameters for the service
and send the request
    to the customer."""
    # Set all of the parameters specific to this particular Auth provider
    # For this example, we use LinkedIn OAuth2 API
    # # LinkedIn authentication parameters
    # Manage your application here: https://www.linkedin.com/developers/apps
    #
    # OAUTH URL in Register = https://www.linkedin.com/oauth/v2/authorization
    # TOKEN URL in Register = https://www.linkedin.com/oauth/v2/accessToken
    # CLIENT IDENTIFIER in Register = <client-identifier-from-your-linkedin-app>process
    title_to_user = "LinkedIn"
    response_type = "token" # LinkedIn is peculiar here since it is a token
# but requires this field be set to code
    scope = ["r_basicprofile"]
    client_secret ="MMqypotJqn07fCNI"
    message_id = str(uuid.uuid4())
    request_id = str(uuid.uuid4())
    # Generate a private and public key, save them to the database with request_id as the
    # index, keep the public key to use in the payload
    (response_encryption_key, privkey_b64) = generate_pair()
    print ("Save private key for use later, base 64: %s" % privkey_b64)
    # Also generate a nonce for this request
    state = generate_nonce()
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % get_jwt_token(),
        "id": message_id,
        "Source-Id": BIZ_ID,
        "Destination-Id": destination_id
        }
    image_file = open("57999517321__00A55C1D-9C7F-46D5-8CD0-867F7EB99072.jpeg", "rb")
    image_data_encoded = base64.b64encode(image_file.read())
    interactive_data = {
        "data": {
            "version": "1.0",
            "requestIdentifier": request_id,
            "authenticate" : {
                "oauth2": {
                    "responseType": response_type,
                    "scope": scope,
                    "clientSecret": client_secret,
                    "state": state,
                    "responseEncryptionKey": response_encryption_key
                    } },
            "images":[]
        },
        "bid": IMESSAGE_EXTENSION_BID,
        "receivedMessage": {
            "title": ("Sign In to %s" % title_to_user),
            "style":"icon"
        },
        "replyMessage": {
            "title": "You Signed In",
            "style":"icon"
        }
}
    payload = {
        "type": "interactive",
        "interactiveData": interactive_data,
        "sourceId": BIZ_ID,
        "destinationId": opaque_id,
        "v": 1,
        "id": message_id
    }
    print(payload)
    r = requests.post("%s/authenticate" % BUSINESS_CHAT_SERVER, json=payload,
                      headers=headers,
                      timeout=30)
    print ("Business Chat server return code: %s" % r.status_code)
    print ("Business Chat server return code: %s" % r.text)
    print ("Send authentication request with parameters")
    print ("request_id: %s" % request_id)
    print ("responseEncryptionKey: %s" % response_encryption_key)
    print ("nonce (aka state): %s" % state)
    print ("private key, base64: %s" % privkey_b64)
    return "ok"
if __name__ == "__main__":
 destination_id = "urn:mbid:AQAAY/XNCBgTsfntER8UH0N1CgOSee3IwaMP6P6umt7Ji2cvPUlwC8kAnqAwXoBt9WKbUy5y4dCSGAP/d2tGii82bBMSiSqBw0ogQ/Xo0qzzrykVT0b0mIpXVpFv9SRhYo280TRpmo5yTfuLQg74wiCdzAvBMP4="
 authenticate_user(destination_id)
