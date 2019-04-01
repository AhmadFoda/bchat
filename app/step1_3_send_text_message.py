# Copyright 2016-2018 Apple, Inc.
# All Rights Reserved.

import requests
import uuid

from config import BIZ_ID, BUSINESS_CHAT_SERVER
from jwt_util import get_jwt_token


def send_text_message(destination_id, message_text):
    message_id = str(uuid.uuid4())  # generate unique message id

    # print ("destination_id "% destination_id)

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % get_jwt_token(),
        "id": message_id,
        "Source-Id": BIZ_ID,
        "Destination-Id": destination_id
    }

    print (headers)

    payload = {

        'body': message_text,
        'sourceId': BIZ_ID,
        'locale': 'en_US',
        'destinationId': destination_id,
        'v': 1,
        'type': 'text',
        'id': message_id
    }
    print  message_text
    print BIZ_ID
    print destination_id
    print message_id

    r = requests.post("%s/message" % BUSINESS_CHAT_SERVER,
                      json=payload,
                      headers=headers,
                      timeout=10)
    print "Business Chat server return code: %s" % r.status_code
    print "Business Chat server return code: %s" % r.reason


if __name__ == "__main__":
    destination_id = "urn:mbid:AQAAY63/TIJe/3nF4EvsJeiA+WeopPR92ycuqyjDzc/14u/PdDhLVjieuzb5nPPwFB9u8jXUS/um2flw2Jr5SKGpDHHGstPdM9TyV0Ml5lldZ/nanUpHWMbBn5AwD3FpoqWhOP0t+5oCWvZaMCtdIPNsgFIaZEA="
    send_text_message(destination_id, "Greetings from your CSP!")

# Expected output:
# Business Chat server return code: 200
