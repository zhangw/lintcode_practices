# -*- coding: utf-8 -*-
"""
RandomOrgApi.py
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 02,2016
"""

import urllib
import urllib2

class RandomOrgApi:
    """use random.org api to generate random numbers"""
    def __init__(self):
        self.path = ""
        self.baseurl = 'https://www.random.org/'
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'

    def __getattr__(self, attr):
        self.path = attr + '/'
        return self

    def generate(self, **kwargs):
        params = []
        for k, v in kwargs.iteritems():
            params.append("%s=%s" % (k, urllib.quote(str(v))))
        if len(params) > 0:
            self.path += "?" + "&".join(params)
        url = self.baseurl + self.path
        print url
        req = urllib2.Request(url)
        req.add_header('User-Agent',self.ua)
        res = urllib2.urlopen(req)
        if res.code == 200:
            array = res.read().split("\n")
            return [int(s) for s in array[:-1]]
        else:
            return None

def main():
    org = RandomOrgApi()
    print org.integers.generate(num=20,min=-10,max=10,col=1,base=10,format='plain',rnd='new')

if __name__ == '__main__':
    main()
