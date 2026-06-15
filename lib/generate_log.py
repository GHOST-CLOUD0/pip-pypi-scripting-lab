from datetime import datetime
import requests


def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be list")

    filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)

    post = fetch_data()
    print("Fetch Post Title:", post.get("title", "No title found"))