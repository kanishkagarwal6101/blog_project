import requests
import json
# import pymongo



def get_tags():
    response = requests.get('https://dev.to/api/tags?per_page=20')
    tags = response.json()
    return [{"id":tag['id'],"tag":tag['name']} for tag in tags]


def get_articles(tags):
    final_articles = []
    for tag in tags:
        articles = requests.get(f'https://dev.to/api/articles?tag={tag["tag"]}')
        for article in articles.json():
            article_response = requests.get(f'https://dev.to/api/articles/{article["id"]}')

            full_article = article_response.json()
            res = {
                "title" : full_article['title'],
                "content": full_article['body_html'],
                "image":full_article['cover_image'],
                "tags":full_article["tags"]
            }

            final_articles.append(res)
    return final_articles

tags = get_tags()

articles = get_articles(tags)

with open("tags.json","w") as tags_f:
    json.dump(tags,tags_f)

with open("articles.json","w") as articles_f:
    json.dump(articles,articles_f)