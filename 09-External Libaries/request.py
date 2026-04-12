import requests

a = requests.get('https://api.github.com/users/octocat')
print(a.text)