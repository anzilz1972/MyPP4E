#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-25 14:23:30
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$
"""
  测试使用logging模块
"""
import logging

#两种格式化字符串，style分别对应'%'和'{'
formatstr1 = '%(asctime)s - %(name)s - %(levelno)s - %(levelname)s - %(message)s'
formatstr2 = '{asctime} - {name} - {levelno} - {levelname} - {message}'


logging.basicConfig(level = logging.DEBUG,format = formatstr2,style = '{')
logger = logging.getLogger(__name__)

logger.info('Start print log')
logger.debug('Do something')
logger.warning('Something maybe fail.')
logger.info('Finish')

