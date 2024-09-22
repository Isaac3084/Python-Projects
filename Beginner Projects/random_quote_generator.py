import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data.get("content")
        author = quote_data.get("author")
        print(f'"{quote}" - {author}')
    else:
        print(f"Failed to fetch a quote. Status code: {response.status_code}")

if __name__ == "__main__":
    get_random_quote()
    