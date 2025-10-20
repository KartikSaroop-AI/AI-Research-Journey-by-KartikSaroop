import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer 
#we have used Text Vectorization tool, to convert text data into numerical form, easier for our model to understand.
from sklearn.naive_bayes import MultinomialNB #Used Naive Bayes classifier 
from sklearn.pipeline import make_pipeline

# Sample data
texts = ["I love this product", "Worst thing ever", "Amazing experience", "Terrible waste of money"]
labels = ["positive", "negative", "positive", "negative"]

# Train model and Make Predictions
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, labels)

print(model.predict(["I love working on python"]))
