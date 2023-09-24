import requests, json, os

headers = {"Authorization":os.environ.get("DOCKERTOKEN")}
def main():
    result = requests.get("https://registry.hub.docker.com/v2/namespaces/koishijs/repositories/koishi/tags/latest", headers=headers)
    text = result.text
    text = json.loads(text)
    for image in text["images"]:
        if (image['architecture']=='amd64'):
            return image['last_pushed']

print(main())
