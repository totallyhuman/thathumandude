# -*- coding: utf-8 -*-

from random import *
from basebot import *

def inbox(match, meta):
	meta['self'].set_nickname(nick_sans)
	meta['self'].send_chat('Here you go:', meta['msgid'])
	meta['self'].set_nickname(bot_nick)

def facepalm(match, meta):
	if randint(1, 20) == 1:
		meta['self'].send_chat('Stop hitting yourself!', meta['msgid'])

def uptime(match, meta):
	meta['self'].send_chat('/me is up since %s (%s).' % (
		format_datetime(meta['self'].started),
		format_delta(time.time() - meta['self'].started)), meta['msgid'])
	
def kill(match, meta):
	meta['self'].send_chat('/me is exiting.', meta['msgid'])
	meta['self'].close()

nick_sans = u'totally\U0001D5C1\U0001D5CE\U0001D5C6\U0001D5BA\U0001D5C7'
nick_mono = u'totally\U0001D691\U0001D69E\U0001D696\U0001D68A\U0001D697'
bot_nick = 'thathumandude'
short_help = '/me is a bot to make pinging ' + nick_mono + ' easier.'
long_help = 'I am a bot made by and for ' + nick_mono + '. I make pinging him easier.'

regexes = {
	'^(\s+)?gimme\s+mah\s+nick,?\s+bot!?(\s+)?$':
		nick_mono,
	'@totallyhuman\b':
		'@' + nick_mono,
	'^(\s+)?!THInbox(\s+)?$':
		inbox,
	'^(\s+)?/me\s+facepalms(\s+)?$':
		facepalm,
	'^(\s+)?!help\s+@?thathumandude(\s+)?$':
		long_help,
	'^(\s+)?!help(\s+)?$':
		short_help,
	'^(\s+)?!ping\s+@?thathumandude(\s+)?$':
		'Pong!',
	'^(\s+)?!ping(\s+)?$':
		'Pong!',
	'^(\s+)?!creator\s+@?thathumandude(\s+)?$':
		'/me was created by ' + nick_mono + '.',
	'^(\s+)?!uptime\s+@?thathumandude(\s+)?$':
		uptime,
	'^(\s+)?!kill\s+@?thathumandude(\s+)?$':
		kill
}

if __name__ == '__main__':
		run_minibot(botname = bot_nick, nickname = bot_nick, regexes = regexes)