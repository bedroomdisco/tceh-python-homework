# -*- coding: utf-8 -*-

import datetime
import json

__author__ = 'sobolevn'


class Storage(object):
    posts = None
    views = None
    _obj = None


    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.views = []
            cls.posts = []
            try:
                with open('blog.json', 'r') as f:
                    cls.posts = json.load(f)
            except Exception as ex:
                print(ex)
        return cls._obj

    @classmethod
    def appending(cls, model):
        cls.posts.append(model)
        with open('blog.json', 'w+') as f:
            json.dump(cls.posts, f)
        return cls.posts


class BlogPostModel(object):
    def __init__(self, form_data):
        self.title = form_data['title']
        self.text = form_data['text']
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.author = form_data['author']

    def model_to_dict(self):
        return {
            'title': self.title,
            'text': self.text,
            'author': self.author,
        }


class PageViewModel(object):
    def __init__(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
