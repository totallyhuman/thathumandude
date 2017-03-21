#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################
# thathumandude                                       #
#                                                     #
# My personal bot for Euphoria. (euphoria.io)         #
#######################################################

from random import *
from basebot import * # Euphoria bot library

def reply(content, match, meta):
	meta['self'].send_chat(content, meta['msgid'])

# Prints out the messages if the sender is me
def inbox(match, meta):
	if meta['sender'] == nick_mono or meta['sender'] == ':3':
		try:
			for m in range(0, len(mails) + 1):
				sender = mails[m]['sender']
				time_since = str(format_delta(time.time() - mails[m]['time'], False))
				message = mails[m]['message']
				
				reply('[%s, %s ago] %s' % (sender, time_since, message))
		except IndexError:
			return 'No more messages for you!'
		del mails[:]
	else:
		return 'Why do you care? It\'s not your inbox. :P'

# Adds a dict with all the properties of an mail
def add_mail(match, meta):
	mails.append({'sender': meta['sender'], 'message': match.group(1), 'time': time.time()})

# Prints out start time and the time since
def uptime(match, meta):
	started = str(format_datetime(meta['self'].started, False))
	time_since = str(format_delta(time.time() - meta['self'].started, False))
	
	return '/me has been up since %s (%s).' % (started, time_since)

# Adds a dict with all the properties of an error
def add_error(match, meta):
	errors.append({'sender': meta['sender'], 'message': match.group(1), 'time': time.time()})
	
	return 'Thank you for your feedback. Message will be delivered to %s.' % nick_mono

# Prints out the errors if the sender is me
def check_errors(match, meta):
	if meta['sender'] == nick_mono or meta['sender'] == ':3':
		try:
			for e in range(0, len(errors) + 1):
				sender = errors[e]['sender']
				time_since = str(format_delta(time.time() - errors[e]['time'], False))
				message = errors[e]['message']
				
				reply('[%s, %s ago] %s' % (sender, time_since, message))
		except IndexError:
			return 'No more errors for you!'
		del errors[:]
	else:
		return 'Why do you care? It\'s not your bot. :P'

# Closes the connection, effectively "killing" it
def kill(match, meta):
	reply('/me is exiting.')
	meta['self'].close()

# Easter egg that has a 1/20 chance of sending "Stop hitting yourself!"
def facepalm(match, meta):
	if randint(1, 20) == 1:
		return 'Stop hitting yourself!'

nick_sans = 'totally\U0001D5C1\U0001D5CE\U0001D5C6\U0001D5BA\U0001D5C7' # My notify nick
nick_mono = 'totally\U0001D691\U0001D69E\U0001D696\U0001D68A\U0001D697' # My nick
bot_nick = 'thathumandude' # The bot's nick
short_help = '/me is a bot to make pinging %s easier.' % nick_mono # The short help message
long_help = 'I am a bot made by and for %s. I make pinging him easier.' % nick_mono # The long help message
errors = [] # The array for errors
mails = [] # The array for mails

regexes = {
	'(?i)^(\s+)?gimme\s+mah\s+nick,?\s+bot!?(\s+)?$':
		nick_mono, # "gimme mah nick, bot!" returns my nick
	'(?i)^(\s+)?gimme\s+mah\s+sans\s+nick,?\s+bot!?(\s+)?$':
		nick_sans,
	'(?i)@totallyhuman\b':
		'@%s' % nick_mono,  # "@totallyhuman" pings my actual nick
	'(?i)^(\s+)?!THInbox(\s+)?$':
		inbox, # "!THInbox" calls the inbox() method
	'(?i)^(?:\s+)?!(?:(?:t|not)?notify|tell)\s+@?totally(?:human|\U0001D691\U0001D69E\U0001D696\U0001D68A\U0001D697)\s+(.*)$':
		add_mail,
	'(?i)^(\s+)?/me\s+facepalms(\s+)?$':
		facepalm, # "/me facepalms" calls the facepalm() method
	'(?i)^(\s+)?!help\s+@?thathumandude(\s+)?$':
		long_help, # "!help @thathumandude" returns the long help message
	'(?i)^(\s+)?!help(\s+)?$':
		short_help, # "!help" returns the short help message
	'(?i)^(\s+)?!ping\s+@?thathumandude(\s+)?$':
		'Pong!', # "!ping @thathumandude" returns "Pong!"
	'(?i)^(\s+)?!pingpong\s+@?thathumandude(\s+)?$':
		'ERROR',
	'(?i)^(\s+)?!ping(\s+)?$':
		'Pong!', # "!ping" returns "Pong!"
	'(?i)^(\s+)?!creator\s+@?thathumandude(\s+)?$':
		'/me was created by %s.' % nick_mono, # "!creator @thathumandude" returns my nick
	'(?i)^(?:\s+)?!error\s+@?thathumandude(?:\s+)(.*)$':
		add_error, # "!error @thathumandude" calls the add_error() method
	'(?i)^(\s+)?!checkerrors\s+@?thathumandude(\s+)?$':
		check_errors, # "!checkerrors @thathumandude" calls the check_errors() method
	'(?i)^(\s+)?!uptime\s+@?thathumandude(\s+)?$':
		uptime, # "!uptime @thathumandude" calls the uptime() method
	'(?i)^(\s+)?!kill\s+@?thathumandude(\s+)?$':
		kill # "!kill @thathumandude" calls the kill() method
}

if __name__ == '__main__':
	# Initiates a MiniBot with the following attributes:
	# botname = bot_nick (nick used for logging)
	# nickname = bot_nick (actual nick used)
	# do_uptime = False (disabling the default uptime function)
	# regexes = regexes (passing the regexes dict for the bot to follow)
	run_minibot(botname = bot_nick, nickname = bot_nick, do_uptime = False, regexes = regexes)
