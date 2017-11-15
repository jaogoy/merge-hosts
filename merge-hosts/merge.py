#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: jaogoy (jaogoy@gmail.com)
import datetime
import logging
import os
import shutil
import tempfile

import config
import util.logger_basicConfig


HEADER = """#
# Modified on %s
#
# All src files are:
#    """ % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

SRC_FILE_SEP_INFO = """
################################################################################
# Copy of content from:
#    %s
################################################################################
"""
SRC_FILE_SEP_INFO = SRC_FILE_SEP_INFO[1:]  # Remove the first \n


def main():
    """Make new hosts file, backup old hosts file,
    then take effect new merged hosts file"""
    new_path = merge_files()
    if config.BACKUP_OLD_HOSTS:
        backup_hosts()
    take_effect(new_path)


def merge_files():
    """Merge all hosts file together as one hosts file"""
    new_path = tempfile.mktemp(suffix=".hosts")
    new_file = open(new_path, 'w')

    src_file_paths = config.OPEN_SOURCE_HOSTS + [config.MY_HOSTS]

    new_file.write(HEADER)
    new_file.write("\n#    ".join(src_file_paths))
    new_file.write("\n\n\n")

    for src_path in src_file_paths:
        if not os.path.exists(src_path):
            logging.warn(u"Hosts file %s not exist.", src_path)
            continue

        new_file.write(SRC_FILE_SEP_INFO % src_path)
        for line in open(src_path, 'r'):
            new_file.write(line)
        new_file.write("\n\n")

    new_file.close()

    logging.debug(u"Make merged file:%s", new_path)

    return new_path


def backup_hosts():
    """Backup old hosts file for safe."""
    if not os.path.exists(config.HOSTS_PATH):
        logging.warn(u"Hosts file %s not exist." % config.HOSTS_PATH)
        return
    if not os.path.exists(config.BACKUP_HOSTS_DIR):
        os.makedirs(config.BACKUP_HOSTS_DIR)

    backup_name = "hosts.%s" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = config.BACKUP_HOSTS_DIR + os.path.sep + backup_name
    shutil.copy(config.HOSTS_PATH, backup_path)
    logging.info(u"Backup hosts file from %s to %s", config.HOSTS_PATH, backup_path)


def take_effect(new_hosts_path):
    shutil.copy(new_hosts_path, config.HOSTS_PATH)
    logging.info(u"Take hosts file effect by copy %s to %s.", new_hosts_path,
                 config.HOSTS_PATH)


if __name__ == "__main__":
    main()


# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
