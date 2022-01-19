##checks if a page exists based on Wikidata ID

import requests

def checkwikidata(wikidata):
    url = 'https://schularchive.bbf.dipf.de/api.php?action=ask&query=[[Wikidata%20ID::' + wikidata + ']]&format=json'
    response = requests.post(url)
    if response.json()['query']['results']:
        return True
    else:
        return False

if __name__ == "__main__":
    check = checkwikidata("Q15261457")
    print(check)