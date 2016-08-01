# -*- coding: utf-8 -*-
import redis
import os
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generateStartUrls(host):
    homepage_url = ["http://appstore.huawei.com/"]
    # more_urls
    more_urls = ["http://appstore.huawei.com/more/", "http://appstore.huawei.com/more/all/", "http://appstore.huawei.com/more/recommend/",
                 "http://appstore.huawei.com/more/soft/", "http://appstore.huawei.com/more/game/", "http://appstore.huawei.com/more/newPo", "http://appstore.huawei.com/more/newUp"]
    # topics_url
    topics_url = ["http://appstore.huawei.com/topics/"]
    # search_urls
    search_urls = ["http://appstore.huawei.com/search/" +
                   str(i) for i in range(0, 10)]
    search_urls.extend(["http://appstore.huawei.com/search/" + chr(i)
                        for i in range(ord('a'), ord('z') + 1)])
    search_urls.extend(["http://appstore.huawei.com/search/app",
                        "http://appstore.huawei.com/search/game"])
    start_urls = homepage_url + more_urls + topics_url + search_urls
    r = redis.Redis(host=host, port=6379)
    for i in start_urls:
        r.lpush('huawei:start_urls', i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', action='store', dest='host', default='localhost',
                        help='The host address for Redis, default is localhost')
    parser.add_argument('-master', action='store', dest='master', default='0',
                        help='This defines master machine. By defalut(master=0),it is slave. Otherwise(master=1), it is the master where Redis is configured')
    args = parser.parse_args()
    if args.master == '1':
        generateStartUrls(args.host)
    # run spider
    os.system('scrapy crawl huawei')
