import os
import requests
import shutil
from datetime import date, datetime

NASA_API_KEY = os.environ.get("NASA_API_KEY")
BASE_DIR = "apod"

def main():
    today = datetime.now().strftime('%Y-%m-%d')

    metadata_path = f"{BASE_DIR}/metadata/{today}.json"
    image_dir = f"{BASE_DIR}/images/{today}"

    if os.path.exists(metadata_path):
        print("APOD already fetched for today.")
        return

    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(f"{BASE_DIR}/metadata", exist_ok=True)

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": NASA_API_KEY,
        "date": today
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    if data.get("media_type") == "image":
        img = requests.get(data["url"])
        img.raise_for_status()

        with open(f"{image_dir}/apod.jpg", "wb") as f:
            f.write(img.content)

    today = datetime.now().strftime('%Y-%m-%d')

    readme_content = f"""
    # 🌌 NASA Astronomy Picture of the Day

    **Date: {today}**

    ## {data['title']}

    ![NASA APOD](apod/images/{today}/apod.jpg)
    {data['explanation']}

    *Image credit: NASA APOD*
        """

    with open("README.md", "w") as f:
        f.write(readme_content)

    print("APOD fetched successfully!")

if __name__ == "__main__":
    main()
