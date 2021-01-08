from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def Home(request):
	sid_obj = SentimentIntensityAnalyzer()
	res = request.POST
	feedback = res.get('subject', False)
	if feedback:
		sentiment_dict = sid_obj.polarity_scores(feedback)
		sentiment_value = sentiment_dict['compound']
		print(sentiment_value)
		if sentiment_dict['compound'] >= 0.1 :
			sentiment = "Positive"
		elif sentiment_dict['compound'] <= - 0.1 :
			sentiment = "Negative"
		else:
			sentiment = "Neutral"
		args = {}
		args['value'] = sentiment_value
		args['feedback'] = feedback
		args['sentiment'] = sentiment
	else:
		args = {}
		args['value'] = ''
		args['feedback'] = ''
		args['sentiment'] = ''
	return TemplateResponse(request, 'products/home.html', args)
