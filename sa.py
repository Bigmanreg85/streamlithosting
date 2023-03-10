import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

st.title("Richard Nero's Sentiment Analyser")

st.subheader("Input your text below to analyse the sentiment and chart the output")

user_input = st.text_input("Enter some text:")
st.audio("welcome.ogg")

scores = sia.polarity_scores(user_input)

l = ['Negative','Neutral','Positive','Overall']


new_scores = {}

for i, key in enumerate(scores.keys()):
	new_key = l[i]
	new_scores[new_key] = scores[key]

if user_input:
	# Create a bar chart of the sentiment scores
	fig = px.bar(x=list(new_scores.keys()), y=list(new_scores.values()))

	# Add chart title and axis labels
	fig.update_layout(title="Sentiment Scores", xaxis_title="Sentiment", yaxis_title="Score")

	# Display the chart
	st.plotly_chart(fig, use_container_width=True)

	if scores['compound'] > 0.05:
		msg = 'That had a positive sentiment'
	else:
		msg = 'That had a negative sentiment'

	st.write(msg)
	#st.write(scores)b
