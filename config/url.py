#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

##URL匹配可以使用正则
urls = (
        
    '^/$',                                          'redirect /seleniumdoc/index', 
    '^/seleniumdoc/$',                               'redirect /seleniumdoc/index', 
    '^/seleniumdoc/([^/]+)$',                        pre_fix + 'selenium.index',  
    '^/pythonapi/$',                               'redirect /pythonapi/index',  
    '^/pythonapi/([^/]+)$',                        pre_fix + 'pythonapi.%s', 
    
)
