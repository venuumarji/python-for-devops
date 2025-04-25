import git
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

total_pulls = response.json()

for i in range(len(total_pulls)):
  print(total_pulls[i]["requested_reviewers"][0]["login"])
