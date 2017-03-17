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
	meta['self'].send_chat('/me has been up since %s (%s).' % (
		format_datetime(meta['self'].started, False),
		format_delta(time.time() - meta['self'].started), False), meta['msgid'])

def add_error(match, meta):
	errors.append({'sender': meta['sender'], 'message': match.group(1), 'time': time.time()})
	meta['self'].send_chat('Thank you for your feedback. Message will be delivered to ' + nick_mono + '.', meta['msgid'])
	
def check_errors(match, meta):
	if meta['sender'] == nick_mono or meta['sender'] == ':3':
		for e in range(0, len(errors)):
			meta['self'].send_chat('[' + errors[e]['sender'] + ', ' + str(format_delta(time.time() - errors[e]['time'], False)) + '] ' + errors[e]['message'], meta['msgid'])
			del errors[e]
	else:
		meta['self'].send_chat('Why do you care? It\'s not your bot. :P', meta['msgid'])
	
def kill(match, meta):
	meta['self'].send_chat('/me is exiting.', meta['msgid'])
	meta['self'].close()

nick_sans = u'totally\U0001D5C1\U0001D5CE\U0001D5C6\U0001D5BA\U0001D5C7'
nick_mono = u'totally\U0001D691\U0001D69E\U0001D696\U0001D68A\U0001D697'
bot_nick = 'thathumandude'
short_help = '/me is a bot to make pinging ' + nick_mono + ' easier.'
long_help = 'I am a bot made by and for ' + nick_mono + '. I make pinging him easier.'
errors = []

regexes = {
	'(?i)^(\s+)?gimme\s+mah\s+nick,?\s+bot!?(\s+)?$':
		nick_mono,
	'(?i)@totallyhuman\b':
		'@' + nick_mono,
	'(?i)^(\s+)?!THInbox(\s+)?$':
		inbox,
	'(?i)^(\s+)?/me\s+facepalms(\s+)?$':
		facepalm,
	'(?i)^(\s+)?!help\s+@?thathumandude(\s+)?$':
		long_help,
	'(?i)^(\s+)?!help(\s+)?$':
		short_help,
	'(?i)^(\s+)?!ping\s+@?thathumandude(\s+)?$':
		'Pong!',
	'(?i)^(\s+)?!ping(\s+)?$':
		'Pong!',
	'(?i)^(\s+)?!creator\s+@?thathumandude(\s+)?$':
		'/me was created by ' + nick_mono + '.',
	'(?i)^(?:\s+)?!error\s+@?thathumandude(?:\s+)?(.*)$':
		add_error,
	'(?i)^(\s+)?!checkerrors\s+@?thathumandude(\s+)?$':
		check_errors,
	'(?i)^(\s+)?!uptime\s+@?thathumandude(\s+)?$':
		uptime,
	'(?i)^(\s+)?!kill\s+@?thathumandude(\s+)?$':
		kill
}

if __name__ == '__main__':
		run_minibot(botname = bot_nick, nickname = bot_nick, do_uptime = False, regexes = regexes)
