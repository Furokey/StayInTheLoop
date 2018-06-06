"""
Project Name - StayInTheLoop
Description  - Scrape /r/outoftheloop, and use selenium with google trends to scrape most frequently searched posts contents
Author       - Bilaal Hussain
Date         - 5/15/2018
"""

import praw
import nltk
from nltk.corpus import stopwords
	
reddit = praw.Reddit('bot1', user_agent='First Bot v0.1')
subreddit = reddit.subreddit("outoftheloop")

#Data storage
post_ids = []
post_titles = []
post_responses = []


#Query limit
limit = 5



current_iterations = 0

#Purpose: filter_dictionary_words(text): Returns text with all common words from the Unix usr/share/dict/words dictionary
#	removed. Uses this to find any words that don't appear in the english language.
#Contract: ListOf(String) -> ListOf(String)
#This will often find the most important words in a reddit post. Often referring to the subject.
def filter_dictionary_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

#Purpose: filter_dictionary_words(text): Returns text with high frequency words with minimal lexical context filtered out
#Contract: ListOf(String) -> ListOf(String)
#This is a less aggressive version of the filter_dictionary_words function
def filter_common_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    common_vocab = set(w.lower() for w in nltk.corpus.stopwords.words('english'))
    uncommon = text_vocab - common_vocab
    return sorted(uncommon)
	
	
"""
for post in subreddit.hot(limit=1):
	post_titles.append(post.title)
	for tokenized in post_titles:
		print(filter_common_words(tokenized))
	"""
while (True):
	for post in content:
		# if it is a question, store the title and score
		if post.id not in post_ids:
			#debugging
			print '\nQuestion: ', post.title
			print 'Score: ', post.score
			post_ids.append(post.id)
			post_titles.append(post.title)

			
			post_comments = post.comments
			top_comment = ''
			
			for comment in post_comments:
				comment_text = post_comment.body
				comment_score = post_comment.score
				#TODO: Fix janky way of finding highest score. Look for API call that finds top post score
				if (comment_score > top_score):
					top_comment = comment_text
					top_score = comment.score

			# append the top comment to the answers list
			answers.append(top_comment)
			current_iterations += 1

			# print the status
			print "Iterations: ", current_iterations,
			time.sleep(delay_slot)
			
			if (current_iterations >= max_iterations):
				break

	# reached if max_iterations is met or no more content
	break


	
#
  #  print("Title: ", post.title)
  #  print("Text: ", post.selftext)
  #  print("Score: ", post.score)
  #  print("----------------------------\n")
