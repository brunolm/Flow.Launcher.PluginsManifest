import requests

from _utils import *



def update_hook(webhook_url: str, info: dict, latest_ver: str, release: dict) -> None:
    embed = {
        "content": None,
        "embeds": [
            {
            "title": info[plugin_name],
            "description": f"Updated to v{latest_ver}!",
            "url": release['html_url'],
            "color": None,
            "fields": [
                {
                "name": "Plugin Description",
                "value": info[description]
                },
                {
                "name": "Plugin Language",
                "value": info[language_name]
                }
            ],
            "author": {
                "name": info[author]
            },
            "thumbnail": {
                "url": info[icon_path]
            }
            }
        ]
        }
    if 'github.com' in info[url_sourcecode].lower():
        github_username = info[url_sourcecode].split('/')[3]
        embed['embeds'][0]['author']['name'] = github_username
        embed['embeds'][0]['author']['url'] = f"{github_url}/{github_username}"
        embed['embeds'][0]["author"]["icon_url"] = f"{github_url}/{github_username}.png?size=40"
    release_notes = release.get('body')
    if release_notes and release_notes.strip():
        embed['embeds'][0]['fields'].append({"name": "Release Notes", "value": release.get('body', "")})
    requests.post(webhook_url, json=embed)