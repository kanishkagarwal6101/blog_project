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
            if full_article['cover_image']==None:
                article_image = full_article["social_image"]
            else:
                article_image = full_article["cover_image"]
            res = {
                "title" : full_article['title'],
                "content": full_article['body_html'],
                "image": article_image,
                "tags":full_article["tags"],
                "readtime": full_article["reading_time_minutes"]
            }

            final_articles.append(res)
    return final_articles

tags = get_tags()

articles = get_articles(tags)

for article in articles:
    url = "http://localhost:5000/story/addstory"
    payload = json.dumps(article)
    print(payload)
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1NzE1ZGE3MmQ2YmNlZTdlOWVmNTI3ZSIsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsImlhdCI6MTcwMTkzMjAwMCwiZXhwIjoxNzAxOTM1NjAwfQ.UgyKLnf_czvY3fS4gvi-prwVwDRMsyEtJaNgYayOuyc',
        'Content-Type': 'application/json'
    }   
    response = requests.request("POST", url=url, headers=headers, data=payload)

with open("tags.json","w") as tags_f:
    json.dump(tags,tags_f)

with open("articles.json","w") as articles_f:
    json.dump(articles,articles_f)