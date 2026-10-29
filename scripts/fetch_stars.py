import os
import urllib.request
import json

USERNAME = "meliss4m4rie"
API_URL = f"https://api.github.com/users/{USERNAME}/starred?per_page=100"

def get_starred_repos():
    req = urllib.request.Request(
        API_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "Python-Script"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching stars: {e}")
        return []

def update_markdown(repos):
    md_content = "# ⭐ Starred Repositories\n\nAutomated list of starred GitHub repositories.\n\n"
    
    for repo in repos:
        name = repo.get("full_name")
        html_url = repo.get("html_url")
        description = repo.get("description") or "No description provided."
        
        md_content += f"* **[{name}]({html_url})** - {description}\n"

    with open("starred-repos.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("Successfully updated starred-repos.md!")

if __name__ == "__main__":
    repos = get_starred_repos()
    if repos:
        update_markdown(repos)