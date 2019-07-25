from django.http import HttpResponse
from django.shortcuts import render
import operator
import spacy
from collections import Counter
import string
from spacy import displacy


def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	nlp = spacy.load("en_core_web_sm")
	wordlist = nlp(fulltext)
	words = [token for token in wordlist if token.pos_ != "PUNCT" and token.pos_ != "SYM"]
	foolproof = fulltext.split()
	mylist = [(token.text, token.pos_) for token in wordlist if token.pos_ != 'PUNCT' and token.pos_ != "SYM"]
	word_freq = len(words)
	sentence_spans = list(wordlist.sents)
	options = {'compact': True, 'page': True, 'minify': True}
	parsing_tree = displacy.render(sentence_spans, style="dep", options=options)
	
	histogram = dict()

	for word in foolproof:
		if word not in histogram:
			histogram[word] = 1
		else:
			histogram[word] += 1

	sortedwords = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'fulltext':fulltext,'count':word_freq,'sortedwords':sortedwords,'pos_tagging':mylist, "tree":parsing_tree})