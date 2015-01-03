#!/usr/bin/env python
# IRC Channel Chechker, written for ther Raspberry Pi Usr Guide by Tim Hudson

import sys, socket, time

RPL_NAMREPLY = '353'
RPL_ENDOFNAMES = '366'

irc = {
    'host' : 'chat.freenode.net',
    'port' : 6667,
    'channel' : '#raspiuserguide',
    'namesinterval' : 5
    }



