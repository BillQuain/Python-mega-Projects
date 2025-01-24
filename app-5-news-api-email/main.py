import requests
from send_email import send_email
topic = "tesla"

api_key = "4c70aaf24eaf419cb840f5cb327425eb"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&from=2023-12-15"\
      "&sortBy=publishedAt&"\
      "apiKey=4c70aaf24eaf419cb840f5cb327425eb&"\
      "language=en"

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
body = " "
for article in content["articles"][:20]:
    body = "Subject: Today's news" \
           + "\n" + body + article["title"] \
           + "\n" + str(article["description"]) + "\n" \
           + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body, receiver="billyq151515@gmail.com")
