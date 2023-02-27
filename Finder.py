import requests

def list_languages_on_repos(username):
    url = f"https://api.github.com/users/{username}/repos?type=public"
    response = requests.get(url)
    repos = response.json()

    languages = set()
    for repo in repos:
        repo_languages_url = repo["languages_url"]
        repo_languages_response = requests.get(repo_languages_url)
        repo_languages = repo_languages_response.json()
        languages.update(repo_languages.keys())

    markdown_list = "- " + "\n- ".join(sorted(languages))
    return f"## Languages Used\n{markdown_list}"
    