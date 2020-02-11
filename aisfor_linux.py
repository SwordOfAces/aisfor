#!/usr/bin/env python3
# what is that A even for, anyway?
# tweets out what the A must obviously stand for

import os
import random
import time

import tweepy

# Get path of executable file, rather than hard-coding
PATH = os.path.dirname(os.path.realpath(__file__)) + '/'
WORDS_NAME = "AWords.txt"
WORDS_FILE = PATH + WORDS_NAME

def main():
	cfg = get_config()
	api = get_api(cfg)
	words = get_words_list(WORDS_FILE)
	make_tweet(words, api)

def get_config():
	with open(PATH + 'keys') as keyFile:
		consumer_key = keyFile.readline().rstrip()
		consumer_secret = keyFile.readline().rstrip()
		access_token = keyFile.readline().rstrip()
		access_token_secret = keyFile.readline().rstrip()
	cfg = {}
	cfg['consumer_key'] = consumer_key
	cfg['consumer_secret'] = consumer_secret
	cfg['access_token'] = access_token
	cfg['access_token_secret'] = access_token_secret
	return cfg

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)
	
def get_words_list(WORDS_FILE):
	with open(WORDS_FILE) as f:
		words = f.readlines() # words is a list of all the words in the file
		return words
		
def make_tweet(words, api):
	a_word = _get_word(words)
	tweet = _get_message(a_word)
	api.update_status(tweet)
		
def _get_message(a_word):
	messages = ["the a is actually for ",
                    "the a is for ",
                    "the a stands for ",
                    "a is for ",
                    "obviously, the a is for ",
                    "the a is *really* for ",
                    "a stands for ",
                    "the a in lgbtqia stands for ",
                    "a *actually* stands for "
                    ]
	msg = random.choice(messages)
	return msg + a_word

def _get_word(words):
	choice = random.randint(0, len(words))
	return words[choice]
	
if __name__ == "__main__":
	main()
