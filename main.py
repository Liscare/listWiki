from bs4 import BeautifulSoup
import requests
import json


def fetch_wiki():
    """
    Fetch all available wiki by scraping the Web site: https://wikistats.wmcloud.org/display.php?t=wp

    :return: A dict with the wiki code (key) and the language name (value)
    """
    page = requests.get("https://wikistats.wmcloud.org/display.php?t=wp")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.body.find(id='table')
    wikis = dict()
    for row in table.select('tr')[2:]:
        lang = row.select('td')[1].a.text
        code = row.select('td')[3].a.text
        wikis.update({code: lang})
    return wikis


def write_wikis(wikis, file_name="wiki_list.json"):
    """
    Create or overwrite a file to write the wikis object as JSON

    :param wikis: A dict to write in JSON
    :param file_name: File name the
    :return: None
    """
    wiki_list = json.dumps(wikis, indent=4)
    with open(file_name, 'w+') as f:
        f.write(wiki_list)
        f.close()


if __name__ == "__main__":
    write_wikis(fetch_wiki())
