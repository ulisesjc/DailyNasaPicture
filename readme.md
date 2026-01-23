readme_content = f"""
# 🌌 NASA Astronomy Picture of the Day

## {data['title']}

![NASA APOD](apod/images/latest.jpg)

{data['explanation']}

*Image credit: NASA APOD*
"""

with open("README.md", "w") as f:
    f.write(readme_content)
