from bs4 import BeautifulSoup
from selenium import webdriver
from textblob import TextBlob

# First we try to get all the comments from the webpage
print("Running chrome")
driver = webdriver.Chrome()
url = 'https://animemangatoon.com/difference-between-manga-and-manhwa-webtoon/'
driver.get(url)

print("Parsing the webpage")
html = BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all(id="div-comment-3")  # all comments are within this div
# result = html.find_all('p', {"id":"div-comment-3"}) should have worked but didn't.
# Couldn't get p values directly

# Had to do this since maybe the html was not in proper format
r = BeautifulSoup(str(result[0]), "html.parser")  # parsing result again to overcome the issue
para = r.find_all('p')

list_comments = []
for item in para:
    list_comments.append(item.text)

print("\nComments from the webpage :", list_comments[0], sep="\n")

# adding more comments the list as the webpage had only 1 comment
list_comments.extend(["I love the art style in manhwa!",
                      "Manga has such a rich history.",
                      "I prefer manga over manhwa.",
                      "Beautiful article.",
                      "Nice summary. Couldn't have worded it better",
                      "Manhwa is boring compared to manga.",
                      "Both have their strengths, but I enjoy manhwa more.",
                      "This article is a waste of time!",
                      "I don't see the difference, they're both great.",
                      "Manhwa has better character development.",
                      "I dislike how manga is drawn sometimes.",
                      "The stories in manhwa are often more engaging."])


# Function to analyze sentiment
def analyze_sentiment(comments):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            positive_count += 1
        elif analysis.sentiment.polarity < 0:
            negative_count += 1
        else:
            neutral_count += 1

    total_comments = len(comments)

    # Calculate percentages
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    neutral_percentage = (neutral_count / total_comments) * 100

    return {
        "total_comments": total_comments,
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count,
        "positive_percentage": positive_percentage,
        "negative_percentage": negative_percentage,
        "neutral_percentage": neutral_percentage
    }


# Analyzing the comments
results = analyze_sentiment(list_comments)

# Printing the results
print("\nSentiment Analysis Results:")
print(f"Total Comments: {results['total_comments']}")
print(f"Positive Comments: {results['positive']} ({results['positive_percentage']:.2f}%)")
print(f"Negative Comments: {results['negative']} ({results['negative_percentage']:.2f}%)")
print(f"Neutral Comments: {results['neutral']} ({results['neutral_percentage']:.2f}%)")