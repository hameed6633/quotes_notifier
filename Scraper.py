import requests

def get_quote_from_web():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} – {data[0]['a']}"
    except Exception as e:
        print(f"[API Error] {e}")

    return None
