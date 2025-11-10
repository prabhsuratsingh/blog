import json
import os
import requests

TOKEN = os.environ["GH_TOKEN"]

query = """
{
  user(login: "prabhsuratsingh") {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes {
        ... on Repository {
          name
          description
          url
        }
      }
    }
  }
}
"""

headers = {"Authorization": f"Bearer {TOKEN}"}
r = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)
data = r.json()

projects = []

for repo in data["data"]["user"]["pinnedItems"]["nodes"]:
    projects.append({
        "name": repo["name"],
        "description": repo["description"] if repo["description"] else "",
        "url": repo["url"]
    })

os.makedirs("prabhsuratsinghblog/data", exist_ok=True)

with open("prabhsuratsinghblog/data/projects.json", "w") as f:
    json.dump(projects, f, indent=2)


print("updated /data/projects.json ✅")
