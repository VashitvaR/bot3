import streamlit as st
import random

qa_data = {
    "How is Nayak always looking to improve and enhance its features?": "Nayak is always looking for ways to improve and enhance its features. If you have any suggestions or specific areas you'd like to see improvements, feel free to share them with us!",
    "What is Nayak's approach to addressing societal challenges?": "Nayak integrates artificial intelligence to contribute to its effectiveness in addressing societal challenges. The goal is to provide a platform that is continually evolving and making a positive impact.",
    "Does Nayak have specific success stories?": "While Nayak doesn't have specific success stories, its focus is on creating positive outcomes for individuals facing societal challenges. Your feedback and experiences contribute to the ongoing improvement of the platform.",
    "What are Nayak's goals in addressing abuse, fraud, and danger?": "Nayak aims to influence policy changes and raise awareness about abuse, fraud, and danger. By connecting victims with authorities, the platform seeks to address conflicts and empower those affected.",
    "How does Nayak address challenges or barriers?": "Nayak acknowledges there may be challenges or barriers. If you have faced any difficulties using the platform, we'd like to hear more about your experiences to make necessary improvements.",
    "How can individuals contribute to building a supportive community using Nayak?": "If you've found success using Nayak, recommending the platform to others facing similar challenges can help build a supportive community and amplify its impact.",
    "How does Nayak encourage collaboration with support systems and authorities?": "Nayak encourages collaboration with existing support systems and authorities to create a comprehensive solution. Together, we can work towards a safer and more supportive environment.",
    "What role does Nayak play in supporting individuals, communities, and governments?": "Nayak plays a crucial role in supporting individuals, communities, and governments. By promoting collaboration and providing valuable insights, the platform aims to make a positive impact in addressing societal challenges.",
    "How does Nayak aim to foster a sense of community and solidarity?": "Nayak strives to foster a sense of community and solidarity among individuals facing societal challenges. Your participation and engagement contribute to creating a supportive environment.",
    "In what way is Nayak open to feedback for continuous improvement?": "Nayak is open to feedback on how it can better address specific challenges and empower victims. Your insights and suggestions play a vital role in the continuous improvement of the platform.",
    "How does Nayak ensure user privacy and data security?": "Nayak prioritizes user privacy and data security by implementing robust encryption measures and adhering to strict data protection protocols. Our commitment is to ensure that user information is handled with the utmost care and in compliance with privacy regulations.",
    "Can users customize their experience on Nayak based on their specific needs and preferences?": "Yes, Nayak provides users with the ability to customize their experience based on individual needs and preferences. Personalization features allow users to tailor the platform to better suit their requirements and address specific challenges they may be facing.",
    "What measures does Nayak take to prevent and address misinformation on its platform?": "Nayak employs advanced algorithms and fact-checking mechanisms to identify and mitigate misinformation on the platform. Additionally, users are encouraged to report any content that raises concerns, enabling prompt action to address and rectify such instances.",
    "How does Nayak collaborate with experts and organizations to stay informed about evolving societal challenges?": "Nayak actively collaborates with experts, organizations, and researchers to stay informed about evolving societal challenges. This collaborative approach ensures that the platform remains at the forefront of addressing emerging issues effectively.",
    "Are there any plans for Nayak to expand its services or features in the future?": "Nayak is committed to continuous improvement and innovation. While specific plans for expansion are proprietary, the platform regularly evaluates opportunities to enhance its services and features to better serve its users.",
    "How does Nayak empower users to take proactive steps in addressing societal issues?": "Nayak empowers users by providing tools and resources to take proactive steps in addressing societal issues. This includes educational content, collaboration opportunities, and the ability to connect with support systems and authorities.",
    "Can users connect with each other on Nayak to share experiences and support one another?": "Yes, Nayak facilitates user connections to encourage the sharing of experiences and mutual support. Building a community of individuals facing similar challenges fosters a supportive environment and amplifies the impact of collective efforts.",
    "What steps does Nayak take to ensure accessibility for users with diverse needs?": "Nayak is designed with accessibility in mind, incorporating features to accommodate users with diverse needs. This includes options for customizable interfaces, assistive technologies, and adherence to accessibility standards.",
    "How does Nayak handle reports of abuse or misuse of its platform?": "Nayak takes reports of abuse or misuse seriously. The platform has established protocols to investigate and address such reports promptly. Users are encouraged to report any instances of misuse to contribute to a safer online environment.",
    "Are there educational resources or guides available on Nayak to help users navigate the platform effectively?": "Yes, Nayak provides educational resources and guides to help users navigate the platform effectively. These resources cover various aspects, including how to use features, engage with the community, and access support when needed."
}



def display_questions(questions):
    for i, question in enumerate(questions, start=1):
        st.checkbox(f"{i}. {question}")

def main():
    all_questions = list(qa_data.keys())
    
    # Randomly select 5 questions for the user to choose from
    random_questions = random.sample(all_questions, 5)

    st.title("Select Questions to Display")
    display_questions(random_questions)

    # Get user input for marked questions using checkboxes
    selected_indices = [index for index, question in enumerate(random_questions, start=1) if st.checkbox(f"{index}. {question}")]
    
    # Display the selected questions and their answers
    for index in selected_indices:
        selected_question = random_questions[index - 1]
        st.write("\nQuestion:", selected_question)
        st.write("Answer:", qa_data[selected_question])

if __name__ == "__main__":
    main()
