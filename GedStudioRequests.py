import requests

headers = {"Content-Type": "application/json", 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                             'Chrome/94.0.4606.114 Safari/537.36',
           'accept': 'application/json, text/plain, */*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8,zh-Hans;q=0.7,en;q=0.6',
           'cache-control': 'max-age=0',
           'dnt': '1',
           'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'X-Real-IP': '211.161.244.70'
           }


class GedRequester:
    safe_mode: bool

    def __init__(self, safe_mode: bool = False):
        self.safe_mode = safe_mode
        ...

    def post(self, url: str, data: dict = None, json: dict = None) -> requests.Response:
        if self.safe_mode:
            return requests.post(url, data=data, json=json, headers=headers, verify=False,
                                 proxies={"http": None, "https": None})
        else:
            return requests.post(url, data=data, json=json, headers=headers)

    def get(self, url: str, data: dict = None, json: dict = None) -> requests.Response:
        if self.safe_mode:
            return requests.get(url, data=data, json=json, headers=headers, verify=False,
                                proxies={"http": None, "https": None})
        else:
            return requests.get(url, data=data, json=json, headers=headers)


class GedSessionRequester:
    safe_mode: bool
    session: requests.Session = requests.session()

    def __init__(self, safe_mode: bool = False):
        self.safe_mode = safe_mode
        ...

    def post(self, url: str, data: dict = None, json: dict = None) -> requests.Response:
        if self.safe_mode:
            return self.session.post(url, data=data, json=json, headers=headers, verify=False,
                                     proxies={"http": None, "https": None})
        else:
            return self.session.post(url, data=data, json=json, headers=headers)

    def get(self, url: str, data: dict = None, json: dict = None) -> requests.Response:
        if self.safe_mode:
            return self.session.get(url, data=data, json=json, headers=headers, verify=False,
                                    proxies={"http": None, "https": None})
        else:
            return self.session.get(url, data=data, json=json, headers=headers)
