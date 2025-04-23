import git
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

total_pulls = response.json()

print(total_pulls[0]["requested_reviewers"][2]["login"])
