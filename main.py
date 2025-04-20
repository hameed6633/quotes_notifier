import random

def get_random_quote(filename="quotes.txt"):
    try:
        with open(filename, "r") as file:
            quotes = file.readlines()
            return random.choice(quotes).strip()
    except FileNotFoundError:
        return "Quotes file not found. Add some quotes to quotes.txt"

def main():
    quote = get_random_quote()
    print("\n🌟 Your Quote for Today:")
    print(f"👉 {quote}\n")

if __name__ == "__main__":
    main()
