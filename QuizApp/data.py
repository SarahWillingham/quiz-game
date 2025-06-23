import requests

def fetch_questions(settings):
    base_url = "https://opentdb.com/api.php"
    url = f"{base_url}?amount={settings['amount']}&category={settings['category']}&type={settings['type']}"
    response = requests.get(url)
    data = response.json()
    return data["results"]
