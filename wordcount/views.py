from django.http import HttpResponse
import operator
import spacy
from spacy import displacy
from collections import Counter
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	nlp = spacy.load("en_core_web_sm")
	wordlist = nlp(fulltext)
	pos_tagging = [(token.text, token.pos_) for token in wordlist if token.pos_ != 'PUNCT' and token.pos_ != "SYM"]
	word_freq = len(pos_tagging)
	tokenized = [token.text for token in wordlist if token.pos_ != "PUNCT" and token.pos_ != "SYM"]
	sentence_spans = list(wordlist.sents)
	options = {'compact': True, 'page': True, 'minify': True, 'collapse_punct': True,
	 'collapse_phrases': True, 'offset_x':60}
	parsing_tree = displacy.render(sentence_spans, style="dep", options=options)
	named_entities = displacy.render(sentence_spans, style="ent")
	histogram = dict()

	for word in tokenized:
		if word not in histogram:
			histogram[word] = 1
		else:
			histogram[word] += 1

	sortedwords = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'fulltext':fulltext,'count':word_freq,'sortedwords':sortedwords,'pos_tagging':pos_tagging, "tree":parsing_tree, "named_entities":named_entities})