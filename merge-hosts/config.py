#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: jaogoy (jaogoy@gmail.com)
import os


ROOT_PATH = os.path.abspath("%s/.." % os.path.dirname(os.path.abspath(__file__)))


# Dest hosts path
HOSTS_PATH_WIN = "C:\Windows\System32\drivers\etc\hosts"
HOSTS_PATH = "/etc/hosts"


# My own hosts
MY_HOSTS = "%s/hosts-files/hosts.my" % ROOT_PATH
# Some other open source hosts files
OPEN_SOURCE_HOSTS = [
    ".../hosts/googlehosts/hosts/hosts-files/hosts"
]


# Whether backup old hosts file
BACKUP_OLD_HOSTS = True
BACKUP_HOSTS_DIR = "%s/hosts-files/backup/" % ROOT_PATH


# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
