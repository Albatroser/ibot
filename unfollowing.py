#!/usr/bin/python3

import sys
from ibot import Bot
import config


b = Bot()
b.my_name = config.my_name
b.passwd = config.passwd

if not b.login():
	sys.exit(1)

# отписка
b.unfollowing()
