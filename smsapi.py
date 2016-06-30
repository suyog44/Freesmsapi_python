# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://freesms8.p.mashape.com/index.php?msg=message&phone=9xxxxxxx%3B9xxxxxxx&pwd=password&uid=username",
  headers={
    "X-Mashape-Key": "Pt9AwaSdaBmsh1JeqEfZhoit1x0Bp15Mq7UjsnOlg9UnqWjrAv"
  }
)
