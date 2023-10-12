import requests


def shorten_link(full_link, link_name):
    api_key = "21412c9a2487d51707121126d44394de93935"
    base_url = " https://cutt.ly/api/api.php"

    payload = {'key': api_key, 'short': full_link, 'name': link_name}
    request = requests.get(base_url, params=payload)
    data = request.json()
    print("www")
    print(data)


shorten_link("https://cutt.ly/api-documentation/regular-api", "code123")