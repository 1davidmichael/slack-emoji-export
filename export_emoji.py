from slacker import Slacker
import os
import requests
import shutil

slack = Slacker(os.environ['SLACK_API_TOKEN'])

emojis = slack.emoji.list()

for emoji_name, emoji_url in emojis.body['emoji'].items():
    if "alias" not in emoji_url:
        file_extension = emoji_url.split(".")[-1]
        r = requests.get(emoji_url, stream=True)
        if r.status_code == 200:
            with open('%s.%s' % (emoji_name, file_extension), 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
            del r
