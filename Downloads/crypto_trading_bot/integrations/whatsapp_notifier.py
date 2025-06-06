import requests

def send_whatsapp_message(phone, message):
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={message}&apikey=free"
    response = requests.get(url)
    return response.status_code == 200
