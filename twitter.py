import re
url=input("URL: ").strip()
matches=re.search(r"^(?:https?://)?(?:www\.)?x\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f"username: {matches.group(1)}")