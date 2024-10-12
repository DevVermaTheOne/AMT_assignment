import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


webtoon_data = pd.read_csv('webtoon_data.csv')

required_data = webtoon_data[['Genre', 'Summary']]
required_data = required_data.dropna()

X = required_data['Summary']
y = required_data['Genre']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical data using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize and train the Decision Tree Classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train_vectorized, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test_vectorized)

# Evaluating the decision tree model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy using Decision trees: {accuracy:.2f}')

print("Now using Logistic Regression with TF-IDF")
# Creating a pipeline with TF-IDF and Logistic Regression
pipeline = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
pipeline.fit(X_train, y_train)

# Predictions
predictions = pipeline.predict(X_test)

# Evaluating the logistic Regression model
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy using Logistic Regression: {accuracy:.2f}')
