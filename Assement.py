import requests
from bs4 import BeautifulSoup

def trending_rep():
    #set to store the languages
    result = set()
    curr_size = 1
    # Dictionary the key value is the language and the value is Number of repos using this language and The list of repos using the language
    languages = {}
    #date for last 30 days
    date = "2021-05-04"
    # first page
    url = f"https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc"
    response=requests.get(url)
    data = response.json()
    for repository in data["items"]:
        name = repository["full_name"]
        language = repository["language"]
        result.add(language)
        if len(result) != curr_size:
            curr_size = curr_size + 1
            languages[language] = list()
            languages[language].append(name)
        else:
            if (language not in languages.keys()):
                languages[language] = list()
                languages[language].append(name)
    for i in languages.keys():
        number_rep=len(languages[i])
        name=languages[i]
        languages[i] = list()
        languages[i].append([number_rep,name])
    print(languages)
if __name__=="__main__":
    trending_rep()