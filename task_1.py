import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline

# Sample dataset of webtoon descriptions and categories
data = {
    'description': [
        'A story about a girl who finds true love amidst chaos.',  # romance
        'An epic battle between heroes and villains.',              # action
        'A fantasy world where magic reigns and dragons fly.',     # fantasy
        'A love triangle unfolds in a high school setting.',       # romance
        'A detective solving crimes in a bustling city.',          # action
        'A tale of friendship and adventures in a magical realm.',  # fantasy
        'A young hero rises to save the world from darkness.',      # action
        'A romantic comedy about misunderstandings and love.',     # romance
        'An action-packed story of revenge and redemption.',        # action
        'A young girl discovers her magical powers and destiny.',   # fantasy
        'A love story set in a futuristic world.',                  # romance
        'A martial artist fighting for justice.',                   # action
        'A magical journey to discover hidden powers.',             # fantasy
    ],
    'category': [
        'romance', 'action', 'fantasy', 'romance', 'action',
        'fantasy', 'action', 'romance', 'action', 'fantasy',
        'romance', 'action', 'fantasy'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Split the dataset into features and labels
X = df['description']
y = df['category']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define a pipeline with TF-IDF vectorizer and Random Forest Classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', RandomForestClassifier())
])

# Use StratifiedKFold to maintain the distribution of classes
stratified_kfold = StratifiedKFold(n_splits=3)

# Define hyperparameters for Grid Search
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [10, 20, None],
    'classifier__min_samples_split': [2, 5],
    'classifier__min_samples_leaf': [1, 2],
}

# Implement Grid Search to find the best hyperparameters
grid_search = GridSearchCV(pipeline, param_grid, cv=stratified_kfold, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Predict using the best model from Grid Search
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=1)

print(f'Accuracy: {accuracy:.2f}')
print('Best Parameters:', grid_search.best_params_)
print('Classification Report:')
print(report)
