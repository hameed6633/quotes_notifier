import random
from plyer import notification
from Scraper import get_quote_from_web

def get_quote_from_file(filename="quotes.txt"):
    try:
        with open(filename, "r") as file:
            quotes = file.readlines()
            return random.choice(quotes).strip()
    except FileNotFoundError:
        return "No quotes found. Please add some to quotes.txt"

def show_notification(quote):
    notification.notify(
        title="🌟 Daily Motivation",
        message=quote,
        timeout=10
    )

def main():
    quote = get_quote_from_web()
    if not quote:
        quote = get_quote_from_file()

    print(f"\n👉 {quote}\n")
    show_notification(quote)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")  # <-- Keeps window open for testing

