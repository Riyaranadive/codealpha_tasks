import requests
import re

# Fixed webpage URL
url = "https://example.com"

# Fetch HTML content
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    # Use regex to extract <title>...</title>
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()

        # Save to file
        with open("page_title.txt", "w", encoding="utf-8") as file:
            file.write(title)

        print(f"✅ Title extracted and saved: {title}")
    else:
        print("❌ Title tag not found.")
else:
    print(f"❌ Failed to fetch page. Status code: {response.status_code}")
