# Copyright 2016-2018 Apple, Inc.
# All Rights Reserved.

import base64
import requests
import uuid

from config import BIZ_ID, BUSINESS_CHAT_SERVER, IMESSAGE_EXTENSION_BID
from jwt_util import get_jwt_token


def send_list_picker_with_images(destination_id, image_file_path):
    message_id = str(uuid.uuid4())  # generate a unique message id

    # a unique request id that will be sent back with response
    request_id = str(uuid.uuid4())

    # read the image file data and encoded it as base 64
    with open(image_file_path, "rb") as image_file:
        image_data_encoded = base64.b64encode(image_file.read())

    payload = {
        "v": 1,
        "type": "interactive",
        "id": message_id,
        "sourceId": BIZ_ID,
        "destinationId": destination_id,
        "interactiveData": {
            "bid": IMESSAGE_EXTENSION_BID,
            "data": {
                "images": [
                    {
                        "data": image_data_encoded,
                        "identifier": "0"
                    }
                ],
                "listPicker": {
                    "sections": [
                        {
                            "items": [
                                {
                                    "identifier": "1",
                                    "imageIdentifier": "0",
                                    "order": 0,
                                    "style": "default",
                                    "subtitle": "Red and delicious",
                                    "title": "Apple"
                                }
                            ],
                            "order": 0,
                            "title": "Fruit",
                            "multipleSelection": True
                        },
                        {
                            "items": [
                                {
                                    "identifier": "2",
                                    "imageIdentifier": "0",
                                    "order": 0,
                                    "style": "default",
                                    "subtitle": "Crispy red",
                                    "title": "another apple"
                                }
                            ],
                            "order": 1,
                            "title": "Veggies",
                            "multipleSelection": True
                        }
                    ]
                },
                "mspVersion": "1.0",
                "requestIdentifier": request_id
            },
            "receivedMessage": {
                "imageIdentifier": "0",
                "style": "small",
                "subtitle": "Farm fresh to you",
                "title": "Select Produce"
            },
            "replyMessage": {
                "style": "small",
                "title": "Selected Produce",
                "subtitle": "Selected Produce"
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % get_jwt_token(),
        "id": message_id,
        "Source-Id": BIZ_ID,
        "Destination-Id": destination_id
    }

    r = requests.post("%s/message" % BUSINESS_CHAT_SERVER,
                      json=payload,
                      headers=headers, timeout=10)

    print "Business Chat server return code: %s" % r.status_code


if __name__ == "__main__":
    destination_id = "<source_id from previously received message>"
    image_file_path = "<filesystem path to list picker image>"

    send_list_picker_with_images(destination_id, image_file_path)

# Expected output:
# Business Chat server return code: 200
