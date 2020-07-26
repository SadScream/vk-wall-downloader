import re
import requests


class Parser:

    def __init__(self):
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, sdch, br',
            'accept-language': 'ru,en;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }

        self.session = requests.Session()
        self.template = r'"cache\d\d\d":"[^\?]+'
    
    def parse(self, url):
        content = self.session.get(url, headers=self.headers).content

        caches = re.findall(self.template, str(content))
        template_for_url = r"https:.+\.mp4"
        urls = Urls({
            '144': None,
            '240': None,
            '360': None,
            '480': None,
            '720': None,
            '1080': None
        })

        for cache in caches:
            url:str = re.findall(template_for_url, cache)[0]
            url = url.replace("\\\\", "")
            
            for k, _ in urls.items():
                if f'.{k}.mp4' in url:
                    urls[k] = url

        return urls


class Urls(dict):

    def __init__(self, d):
        self.__dict__ = d

    def best_q(self):
        better:str = None
        quality:str = None

        for k, v in self.__dict__.items():
            if v != None:
                better = v
                quality = k
            
        return quality, better

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__dict__.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)


if __name__ == "__main__":
    parser = Parser()
    u = parser.parse("https://vk.com/video_ext.php?oid=248996068&id=456240000&hash=ce6effb5c6b43977&__ref=vk.api&api_hash=1595737181c902f059db0b512e14_GMZDGNRVHA4TQNA")
    print(u.best_q())
