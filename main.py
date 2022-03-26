# version 1.0.0

import os
import random
import time

import requests
import urllib3
from lxml import etree

import GedStudioRequests

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

urllib3.disable_warnings()
session = GedStudioRequests.GedSessionRequester(True)

#          username    password       uid
users = [('Spider_1', 'spider123', '344640'),
         ('Spider_2', 'spider123', '344641'),
         ('Spider_3', 'spider123', '344642'),
         ('Spider_4', 'spider123', '344643'),
         ('Spider_5', 'spider123', '344644')]


def download_updated(page, limit: int = -1):
    if int(page) == 0:
        downloading_page = 1
        while True:
            if limit != -1:
                if downloading_page > limit:
                    break
            print("===================================")
            print('开始下载第 ' + str(downloading_page) + ' 页')
            if not (os.path.exists(f'第 {downloading_page} 页') and os.path.isdir(f'第 {downloading_page} 页')):
                os.mkdir(f'第 {downloading_page} 页')
            response = session.get('https://www.tujidao.com/u/?action=gengxin&page=' + str(downloading_page))
            if response.status_code == 200:
                html = etree.HTML(response.content)
                articles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/a/img/@src")
                titles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/p[@class='biaoti']/a")
                if len(articles) == 0 or len(titles) == 0:
                    break
                for i in range(0, len(articles)):
                    article_link_prefix = str(articles[i]).rsplit('/', 1)[0] + '/'
                    title = titles[i].text
                    o = 0
                    if not (os.path.exists(f'第 {downloading_page} 页/' + title) and os.path.isdir(
                            f'第 {downloading_page} 页/' + title)):
                        os.mkdir(f'第 {downloading_page} 页/' + title)
                    print('-----------------------------------')
                    print('正在下载 ' + title)
                    while True:
                        picture_response = requests.get(article_link_prefix + str(o) + '.jpg', headers=headers,
                                                        verify=False, proxies={"http": None, "https": None},
                                                        stream=True)
                        if picture_response.status_code == 200:
                            if os.path.exists(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg') \
                                    and os.path.isfile(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg'):
                                print('你已下载过第' + str(o) + '张')
                                o += 1
                                continue
                            else:
                                with open(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg', 'wb') as f:
                                    f.write(picture_response.content)
                                o += 1
                                print('正在下载第 ' + str(o) + ' 张')
                            take_a_break()
                        else:
                            break
                    print('-----------------------------------')
            downloading_page += 1
            print("===================================")
    else:
        response = session.get('https://www.tujidao.com/u/?action=gengxin&page=' + page)
        if response.status_code == 200:
            html = etree.HTML(response.content)
            articles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/a/img/@src")
            titles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/p[@class='biaoti']/a")
            if len(articles) == 0 or len(titles) == 0:
                print('你输入的页数太大或太小了！')
                return False
            for i in range(0, len(articles)):
                article_link_prefix = str(articles[i]).rsplit('/', 1)[0] + '/'
                title = titles[i].text
                o = 0
                if not (os.path.exists(title) and os.path.isdir(title)):
                    os.mkdir(title)
                print('-----------------------------------')
                print('正在下载 ' + title)
                while True:
                    picture_response = requests.get(article_link_prefix + str(o) + '.jpg', headers=headers,
                                                    verify=False, proxies={"http": None, "https": None},
                                                    stream=True)
                    if picture_response.status_code == 200:
                        if os.path.exists(title + "/" + str(o) + '.jpg') and os.path.isfile(
                                title + "/" + str(o) + '.jpg'):
                            print('你已下载过第' + str(o) + '张')
                            o += 1
                            continue
                        else:
                            with open(title + "/" + str(o) + '.jpg', 'wb') as f:
                                f.write(picture_response.content)
                            o += 1
                            print('正在下载第 ' + str(o) + ' 张')
                        take_a_break()
                    else:
                        break
                print('-----------------------------------')
        else:
            print('获取失败')
            return False
    return True


def download_category(category_id, page, limit: int = -1):
    if int(page) == 0:
        downloading_page = 1
        while True:
            if limit != -1:
                if downloading_page > limit:
                    break
            print("===================================")
            print('开始下载第 ' + str(downloading_page) + ' 页')
            if not (os.path.exists(f'第 {downloading_page} 页') and os.path.isdir(f'第 {downloading_page} 页')):
                os.mkdir(f'第 {downloading_page} 页')
            response = session.get('https://www.tujidao.com/s/?id=' + category_id + '&page=' + str(downloading_page))
            if response.status_code == 200:
                html = etree.HTML(response.content)
                articles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/a/img/@src")
                titles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/p[@class='biaoti']/a")
                if len(articles) == 0 or len(titles) == 0:
                    break
                for i in range(0, len(articles)):
                    article_link_prefix = str(articles[i]).rsplit('/', 1)[0] + '/'
                    title = titles[i].text
                    o = 0
                    if not (os.path.exists(f'第 {downloading_page} 页/' + title) and os.path.isdir(
                            f'第 {downloading_page} 页/' + title)):
                        os.mkdir(f'第 {downloading_page} 页/' + title)
                    print('-----------------------------------')
                    print('正在下载 ' + title)
                    while True:
                        picture_response = requests.get(article_link_prefix + str(o) + '.jpg', headers=headers,
                                                        verify=False, proxies={"http": None, "https": None},
                                                        stream=True)
                        if picture_response.status_code == 200:
                            if os.path.exists(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg') \
                                    and os.path.isfile(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg'):
                                print('你已下载过第' + str(o) + '张')
                                o += 1
                                continue
                            else:
                                with open(f'第 {downloading_page} 页/' + title + "/" + str(o) + '.jpg', 'wb') as f:
                                    f.write(picture_response.content)
                                o += 1
                                print('正在下载第 ' + str(o) + ' 张')
                            take_a_break()
                        else:
                            break
                    print('-----------------------------------')
            downloading_page += 1
            print("===================================")
    else:
        response = session.get('https://www.tujidao.com/s/?id=' + category_id + '&page=' + page)
        if response.status_code == 200:
            html = etree.HTML(response.content)
            articles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/a/img/@src")
            titles = html.xpath("/html/body/div[@class='hezi']/ul/li[@id]/p[@class='biaoti']/a")
            if len(articles) == 0 or len(titles) == 0:
                print('你输入的页数太大或太小了！')
                return False
            for i in range(0, len(articles)):
                article_link_prefix = str(articles[i]).rsplit('/', 1)[0] + '/'
                title = titles[i].text
                o = 0
                if not (os.path.exists(title) and os.path.isdir(title)):
                    os.mkdir(title)
                print('-----------------------------------')
                print('正在下载 ' + title)
                while True:
                    picture_response = requests.get(article_link_prefix + str(o) + '.jpg', headers=headers,
                                                    verify=False, proxies={"http": None, "https": None},
                                                    stream=True)
                    if picture_response.status_code == 200:
                        if os.path.exists(title + "/" + str(o) + '.jpg') and os.path.isfile(
                                title + "/" + str(o) + '.jpg'):
                            print('你已下载过第' + str(o) + '张')
                            o += 1
                            continue
                        else:
                            with open(title + "/" + str(o) + '.jpg', 'wb') as f:
                                f.write(picture_response.content)
                            o += 1
                            print('正在下载第 ' + str(o) + ' 张')
                        take_a_break()
                    else:
                        break
                print('-----------------------------------')
        else:
            print('获取失败')
            return False
    return True


def main():
    print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    print('！！！本项目仅用于学习，下载图片间隔必须大于1s，下载后请在24小时内删除，请自行承担法律责任！！！')
    print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    input('按下回车开始使用')

    # Login a account first
    user_info = users[random.randint(0, len(users) - 1)]
    login_response = session.post('https://www.tujidao.com/',
                                  data={'action': 'save', 'way': 'login', 'username': user_info[0],
                                        'password': user_info[1]})
    if login_response.status_code == 200:
        session.session.cookies.set('uid', user_info[2])
        session.session.cookies.set('name', user_info[0])
        session.session.cookies.set('leixing', '0')
        print('------------ 爬取方式 ------------')
        print('0 - 全部')
        print('1 - 分类')
        print('2 - 全部 无限下载')
        print('3 - 分类 无限下载\n')
        sort_method = input('请输入你的爬取方式：')
        if sort_method == '0':

            page = input('请输入你要爬取的页数: ')
            if not is_int(page):
                print('请输入一个正确的整数！')
                return
            if int(page) < 1:
                print('请输入一个大于0的整数！')
                return
            if download_updated(page):
                print('下载完成！')
            else:
                print('下载失败')
            ...
        elif sort_method == '1':
            response = session.get('https://www.tujidao.com/u/?action=gengxin')
            if response.status_code == 200:
                html = etree.HTML(response.content)
                categories = html.xpath("/html/body/div[@id='caidian']/div[@class='caidan']/div[@class='layui-tab "
                                        "layui-tab-brief']/div[@class='layui-tab-content']/div[@class='layui-tab-item "
                                        "layui-show']/div[@class='tags']/a")
                links = html.xpath("/html/body/div[@id='caidian']/div[@class='caidan']/div[@class='layui-tab "
                                   "layui-tab-brief']/div[@class='layui-tab-content']/div[@class='layui-tab-item "
                                   "layui-show']/div[@class='tags']/a/@href")
                if len(categories) == 0 or len(links) == 0:
                    print('获取分类失败')
                    return
                print('------------ 分类 ------------')
                cate_link_map = list()
                for i in range(0, len(categories)):
                    just_map = dict()
                    just_map['name'] = categories[i].text
                    just_map['id'] = links[i].rsplit('=', 1)[1]
                    cate_link_map.append(just_map)
                    print(str(i) + ' - ' + just_map['name'])
                selected_category = input('请输入你要爬取的分类：')
                if not is_int(selected_category):
                    print('请输入一个正确的整数！')
                    return
                selected_category = int(selected_category)
                if selected_category < 0 or selected_category >= len(cate_link_map):
                    print('不存在该分类')
                    return

                page = input('请输入你要爬取的页数: ')
                if not is_int(page):
                    print('请输入一个正确的整数！')
                    return
                if int(page) < 1:
                    print('请输入一个大于0的整数！')
                    return
                if download_category(cate_link_map[selected_category]['id'], page):
                    print('下载完成！')
                else:
                    print('下载失败')
            else:
                print('获取失败')
            ...
        elif sort_method == '2':
            limit = input('请输入下载页数限制（输入0不设限制）：')

            if is_int(limit):
                if int(limit) < 0:
                    print('由于你整数小于0，因此认为你不设限制')
                    print('由于你输入并不是一个合法的整数，因此认为你不设限制')
                    input('按下回车确认')
                    if download_updated(0):
                        print('下载完成！')
                    else:
                        print('下载失败')
                else:
                    if int(limit) == 0:
                        if download_updated(0):
                            print('下载完成！')
                        else:
                            print('下载失败')
                    else:
                        if download_updated(0, int(limit)):
                            print('下载完成！')
                        else:
                            print('下载失败')
            else:
                print('由于你输入并不是一个合法的整数，因此认为你不设限制')
                input('按下回车确认')
                if download_updated(0):
                    print('下载完成！')
                else:
                    print('下载失败')
        elif sort_method == '3':
            response = session.get('https://www.tujidao.com/u/?action=gengxin')
            if response.status_code == 200:
                html = etree.HTML(response.content)
                categories = html.xpath("/html/body/div[@id='caidian']/div[@class='caidan']/div[@class='layui-tab "
                                        "layui-tab-brief']/div[@class='layui-tab-content']/div[@class='layui-tab-item "
                                        "layui-show']/div[@class='tags']/a")
                links = html.xpath("/html/body/div[@id='caidian']/div[@class='caidan']/div[@class='layui-tab "
                                   "layui-tab-brief']/div[@class='layui-tab-content']/div[@class='layui-tab-item "
                                   "layui-show']/div[@class='tags']/a/@href")
                if len(categories) == 0 or len(links) == 0:
                    print('获取分类失败')
                    return
                print('------------ 分类 ------------')
                cate_link_map = list()
                for i in range(0, len(categories)):
                    just_map = dict()
                    just_map['name'] = categories[i].text
                    just_map['id'] = links[i].rsplit('=', 1)[1]
                    cate_link_map.append(just_map)
                    print(str(i) + ' - ' + just_map['name'])
                selected_category = input('请输入你要爬取的分类：')
                if not is_int(selected_category):
                    print('请输入一个正确的整数！')
                    return
                selected_category = int(selected_category)
                if selected_category < 0 or selected_category >= len(cate_link_map):
                    print('不存在该分类')
                    return
                limit = input('请输入下载页数限制（输入0不设限制）：')

                if is_int(limit):
                    if int(limit) < 0:
                        print('由于你整数小于0，因此认为你不设限制')
                        print('由于你输入并不是一个合法的整数，因此认为你不设限制')
                        input('按下回车确认')
                        if download_category(cate_link_map[selected_category]['id'], 0):
                            print('下载完成！')
                        else:
                            print('下载失败')
                    else:
                        if int(limit) == 0:
                            if download_category(cate_link_map[selected_category]['id'], 0):
                                print('下载完成！')
                            else:
                                print('下载失败')
                        else:
                            if download_category(cate_link_map[selected_category]['id'], 0, int(limit)):
                                print('下载完成！')
                            else:
                                print('下载失败')
                else:
                    print('由于你输入并不是一个合法的整数，因此认为你不设限制')
                    input('按下回车确认')
                    if download_category(cate_link_map[selected_category]['id'], 0):
                        print('下载完成！')
                    else:
                        print('下载失败')
            else:
                print('获取失败')
            ...

        else:
            print('未知的方法')
        ...
    else:
        print('登录失败')
    ...


def is_int(sth) -> bool:
    try:
        int(sth)
        return True
    except TypeError:
        return False


def take_a_break():
    time.sleep(1)


if __name__ == '__main__':
    main()
