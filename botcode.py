import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import pairwise_distances

# Nayak-related data
data = [
    {"question": "How is Nayak always looking to improve and enhance its features?", "answer": "Nayak is always looking for ways to improve and enhance its features. If you have any suggestions or specific areas you'd like to see improvements, feel free to share them with us!"},
    # ... (other questions and answers)
    {"question": "How can Nayak users report potential security vulnerabilities and contribute to platform safety?", "answer": "Nayak encourages users to report potential security vulnerabilities. A dedicated security team reviews reports, and a responsible disclosure program is in place to ensure the prompt resolution of identified vulnerabilities"}
]

# Create a DataFrame
df_nayak = pd.DataFrame(data)

# Bag of Words (BOW)
cv = CountVectorizer()
x_bow = cv.fit_transform(df_nayak['question']).toarray()
features_bow = cv.get_feature_names_out()
df_bow = pd.DataFrame(x_bow, columns=features_bow)

def chat_bow(question):
    tidy_question = question.lower()
    cv_ = cv.transform([tidy_question]).toarray()
    cos = 1 - pairwise_distances(df_bow, cv_, metric='cosine')
    index_value = cos.argmax()
    return df_nayak['answer'].loc[index_value]

# TF-IDF
tfidf = TfidfVectorizer()
x_tfidf = tfidf.fit_transform(df_nayak['question']).toarray()
features_tfidf = tfidf.get_feature_names_out()
df_tfidf = pd.DataFrame(x_tfidf, columns=features_tfidf)

def chat_tfidf(question):
    tidy_question = question.lower()
    tf = tfidf.transform([tidy_question]).toarray()
    cos = 1 - pairwise_distances(df_tfidf, tf, metric='cosine')
    index_value = cos.argmax()
    return df_nayak['answer'].loc[index_value]

# Streamlit App
def main():
    st.title("Nayak Chatbot")

    # User input
    user_input_question = st.text_input("Ask Nayak a question:")
    
    # Method selection
    method = st.radio("Select Chatbot Method:", ['Bag of Words (BOW)', 'TF-IDF'])
    
    # Chatbot response
    if st.button("Get Nayak's Answer"):
        if method == 'Bag of Words (BOW)':
            response = chat_bow(user_input_question)
        elif method == 'TF-IDF':
            response = chat_tfidf(user_input_question)
        else:
            response = "Select a valid method."

        st.text_area("Nayak's Response:", response)

if __name__ == "__main__":
    main()
