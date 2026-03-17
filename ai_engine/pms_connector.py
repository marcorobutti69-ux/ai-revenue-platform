import requests

def send_price_to_pms(price):

    url = "https://api.yourpms.com/update_price"

    payload = {
        "room_type": "standard",
        "price": price
    }

    try:
        response = requests.post(url, json=payload)

        return {
            "status": response.status_code,
            "response": response.text
        }

    except:
        return {
            "status": "error",
            "response": "API not connected"
        }
