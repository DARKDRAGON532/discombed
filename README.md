# Discombed
Discombed is a very bad wrapper for discord embeds
It is made in python and can support python 3.6 and above (hopefully)

# Quickstart

```python
import discombed

webhook = discombed.Hook(
    url = "https://discord.com/api/webhooks/id/token",
    content = "Hello, World!"
)

webhook.send()
```

# Functions and Classes

## ```discombed.Hook(url, content=None, username=None, avatar_url=None, tts=False)```
```
URL : str for discord webhook
Username : str defaults to the one specified in webhook creation
avatar_url : str defaults to the one specified in webhook creation
tts : bool defaults to false.
```

## ```.add_embed(Embed)```
Takes an embed object to add to the webhook (Max 10)

## ```.send(silent=True)```
Sends the webhook to discord

if silent is false it will return status code

## ```dicombed.Embed(title=None, colour=None, url=None, description=None, timestamp=None)```

```
title = title for embed
colour = decimal value of colour (use dischook.hex_to_decimal for converting hex to decimal)
description = description for embed
url = redirection url
timestamp = timestamp, must be in datetime.datetime format
```

## ```set.author(name, icon_url, url)```
Sets author for embed

name = author name

icon_url = icon url

url =  redirect url

## ```set_image(url)```
sets embed image

url = url for image

## ```set_thumbnail(url)```
sets embed thumbnail

url = url for thumbnail

## ```set_footer(text, icon_url)```
sets embed footer

text = text for footer

icon_url = icon for footer

## ```add_field(name, value, inline=False)```
adds field for webhook, supports markdown

name = name of field

value = value of field

inline=False, set to true if you want inline

## ```dicombed.hex_to_decimal(hex)```
param = hex

returns decimal value of hex (useful for embed colours)