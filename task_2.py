
from textblob import TextBlob

# Sample user comments
comments = [
    "I love manga! It's so creative and engaging.",
    "Manhwa has the best art style in my opinion.",
    "I don't really like either; they're boring.",
    "The stories in manga are usually better than in manhwa.",
    "I find manhwa to be too predictable.",
    "Manga and manhwa both have their strengths!",
    "I dislike how slow-paced some manga can be."
]

# Initialize counters and lists for sentiment analysis
positive_comments = []
negative_comments = []
neutral_comments = []

# Analyze each comment
for comment in comments:
    analysis = TextBlob(comment)
    # Classify sentiment
    if analysis.sentiment.polarity > 0:
        positive_comments.append(comment)
    elif analysis.sentiment.polarity < 0:
        negative_comments.append(comment)
    else:
        neutral_comments.append(comment)

# Calculate total comments
total_comments = len(comments)

# Calculate percentages
positive_percentage = (len(positive_comments) / total_comments) * 100
negative_percentage = (len(negative_comments) / total_comments) * 100
neutral_percentage = (len(neutral_comments) / total_comments) * 100

# Summary of results
results_summary = {
    'Positive Comments (%)': positive_percentage,
    'Negative Comments (%)': negative_percentage,
    'Neutral Comments (%)': neutral_percentage,
}

# Print the results
print("Sentiment Analysis Results:")
for sentiment, percentage in results_summary.items():
    print(f"{sentiment}: {percentage:.2f}%")

# Print categorized comments
print("\nCategorized Comments:")
print("\nPositive Comments:")
for comment in positive_comments:
    print(f"- {comment}")

print("\nNegative Comments:")
for comment in negative_comments:
    print(f"- {comment}")

print("\nNeutral Comments:")
for comment in neutral_comments:
    print(f"- {comment}")
