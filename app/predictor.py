from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

training_data = [
    "Python developer machine learning API",
    "React frontend JavaScript HTML CSS",
    "Data analysis pandas numpy visualization",
    "Android Kotlin Java mobile app",
]

labels = [
    "Backend Developer",
    "Frontend Developer",
    "Data Scientist",
    "Android Developer"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(training_data)

model = LinearSVC()

model.fit(X, labels)

def predict_category(resume_text):

    transformed = vectorizer.transform([resume_text])

    prediction = model.predict(transformed)

    return prediction[0]
    