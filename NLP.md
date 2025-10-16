# 🧭 Natural Language Processing (NLP) – Learning Progress

This file documents my daily learning and experiments in **Natural Language Processing**, as part of my AI-Research-Journey-by-KartikSaroop.  
Each section below links to a specific topic or day.


Introduction to NLP Basics
### 📚 What I Learned  
- Explored the **basics of NLP (Natural Language Processing)**  
- Practiced using **NLTK** library in Python  
- Implemented:
  - **Tokenization** – splitting text into words and sentences  
  - **Stemming & Lemmatization** – reducing words to their root form  
  - **POS Tagging** – identifying grammatical structure  
- Understood the importance of preprocessing in text-based ML models  

---

### 💻 Python Example
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

text = "Natural Language Processing helps computers understand human language."

tokens = word_tokenize(text)
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in tokens]
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]
pos_tags = pos_tag(tokens)

print("Tokens:", tokens)
print("Stems:", stems)
print("Lemmas:", lemmas)
print("POS Tags:", pos_tags)

🧠 Reflection
Learned how NLTK simplifies text preprocessing and makes it easier to prepare text data for machine learning models.
