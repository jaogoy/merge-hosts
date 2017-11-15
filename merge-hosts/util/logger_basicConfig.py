#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: jaogoy (jaogoy@gmail.com)
import logging


"""Use basic logging"""

LOG_LEVEL = logging.DEBUG

format_string = '[%(levelname)s] %(asctime)s %(filename)s[%(lineno)d] %(message)s'
logging.basicConfig(level=LOG_LEVEL,
                    format=format_string,
                    datefmt='%Y-%m-%d %H:%M:%S')


# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
