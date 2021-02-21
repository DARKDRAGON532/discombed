import requests


def hex_to_decimal(hex: str) -> int:
    """
    converts hex code to decimal for colours in embeds
    """
    return int(hex.removeprefix("#").strip(), 16)


class Embed:
    """
    title = title for embed\n
    colour = decimal value of colour (use dischook.hex_to_decimal for it)\n
    description = description for embed\n
    timestamp = timestamp, must be in datetime.datetime format
    """

    def __init__(self, title: str = None, colour: str = None, url: str = None, description: str = None, timestamp: str = None) -> None:
        self.fields = []
        self.title = title
        self.colour = colour
        self.url = url
        self.description = description
        self.timestamp = str(timestamp) if timestamp else None
        self.author = None
        self.image = None
        self.thumbnail_image = None
        self.footer = None

    def set_author(self, name: str = None, url: str = None, icon_url: str = None) -> None:
        """
        Sets author of embed\n
        name = authors name\n
        icon_url = icon url\n
        url =  href url
        """
        self.author = {
            "name": name,
            "url": url,
            "icon_url": icon_url
        }

    def add_field(self, *, name: str, value: str, inline=False) -> None:
        """
        adds field to embed\n
        name = title of field\n
        value = value of fielf\n
        inline = defaults to false
        """
        self.fields.append({
            "name": name,
            "value": value,
            "inline": inline
        })

    def set_image(self, url: str):
        """
        sets embed image\n
        url = string
        """
        self.image = {"url": url}

    def set_thumbnail(self, url: str):
        """
        sets thumbnail image\n
        url = string
        """
        self.thumbnail_image = {"url": url}

    def set_footer(self, *, text: str = None, icon_url: str = None):
        self.footer = {
            "text": text,
            "icon_url": icon_url
        }


class Hook:
    """
    url = URL of webhook\n
    username = url (defaults to the one specified in discord\n
    avatar_url =  url for avatar (defaults to the one specidied in discord)\n
    tts = defaults to false
    embed = Embed object
    file = bytes
    """

    def __init__(self, *, url: str, content: str = None, username: str = None, avatar_url: str = None, tts: bool = False) -> None:
        self.url = url
        self.params = {
            "content": content,
            "username": username,
            "avatar_url": avatar_url,
            "tts": tts,
            "embeds": []
        }

    def add_embed(self, embed: Embed) -> None:
        self.params["embeds"].append({
            "title": embed.title,
            "url": embed.url,
            "description": embed.description,
            "color": embed.colour,
            "timestamp": embed.timestamp,
            "author": embed.author,
            "fields": embed.fields,
            "image": embed.image,
            "thumbnail": embed.thumbnail_image,
            "footer": embed.footer
        })

    def send(self, silent=False):
        """
        Sends embed
        \n
        silent = if true no status code is returned
        """
        r = requests.post(self.url, json=self.params)
        if not silent:
            print(r.status_code)
            content = str(r.content).replace("'", "").removeprefix('b')
            if content != "":
                raise Exception(content)
