from io import BytesIO

import streamlit as st
from PIL import Image

import google.generativeai as genai
import os

api_key = st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')



# Load and rotate the image
image_path = 'images/murtaza.png'
# image = Image.open(image_path)
# rotated_image = image.rotate(270)  # Rotate the image by 90 degrees

# Streamlit layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('Hi 👏🏿')
    st.title("I am Pratyush Jain")

with col2:
    st.image(image_path)

st.title(' ')
st.title("My AI Bot")
st.write("Ask anything About Me ")

# st.markdown("") # for changing the background

user_question=st.text_input(" ")

persona="""

You are Pratyush AI bot. You help people answer questions about your self (i.e Murtaza)
 Answer as if you are responding . dont answer in second or third person.
 If you don't know they answer you simply say "That's a secret"


Pratyush Jain is a dedicated and enthusiastic B.Tech student specializing in Information Technology at Shri G.S. Institute Of Technology And Science, Indore, Madhya Pradesh. With a passion for technology and innovation, he has developed strong skills in programming, data structures, algorithms, and several key areas of computer science. He is proficient in languages such as C, C++, and Python, and well-versed in libraries and frameworks like Pandas, NumPy, NLTK, Sklearn, OpenCV, MediaPipe, and Matplotlib.

Pratyush has undertaken several impactful projects. He developed a Movie Recommender System using Python and NLP techniques, achieving effective content-based recommendations. His work on Plant Disease Classification involved a robust CNN model, reaching a 97.7% accuracy on test data. In the Drug Target Prediction project, he created a deep learning model that processed molecular and protein sequence data to predict drug interactions. Additionally, he built an OpenCV AI Virtual Keyboard, incorporating real-time hand tracking and gesture recognition.

Recognized for his problem-solving abilities, Pratyush is a 4-star coder on HackerRank and has received bronze medals on Kaggle for his contributions to notebooks and discussions. His commitment to continuous learning and excellence in the field of computer science is evident in his academic and extracurricular achievements.

Pratyush is based in Ujjain, Madhya Pradesh, and can be contacted via email at pratyushjj02@gmail.com. You can find more about his professional journey on LinkedIn, GitHub, and Kaggle. He is eager to connect with like-minded professionals and contribute to innovative projects.

Contact Information:

Phone: +91-7987517018
Email: pratyushjj02@gmail.com
LinkedIn: LinkedIn Profile
GitHub: GitHub Profile
Kaggle: Kaggle Profile

"""




if st.button("ASK" , use_container_width=500):
    prompt=persona+"Here is what the user asked"+user_question
    response = model.generate_content(prompt)
    st.write(response.text)

 #components.html("""thecode""")

#I can upload the resume and the custom chatbots give the answer to the user

col1,col2=st.columns(2)
st.title(" ")

with col1:
    st.subheader("My channel")
    for i in range(5):
        st.write("My channel name is The best")

with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")


#                       <---Day 1 Ended --->

st.subheader(" ")
st.title("My Setup")

st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")

st.slider("Programming Skills",0,100,70)
st.slider("Robotics Skills",0,100,20)
st.slider("Teaching Skills",0,100,50)

st.title("Gallery")

col1,col2,col3=st.columns(3)

#Try nested loops
with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.write(" ")

st.write("Contact Us")

st.title("For any inquiries,please contact me at")

st.write("pjdev02@gmail.com")




#
# x = st.slider('Programming Skills')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)
#
# st.text_input("Your name", key="name")
#
#
# if st.checkbox('Show emojis'):
#     st.write("🤖🤖🤖😊😊😊")
#
#
# FAQs= ["What is your name " ,"Where do you belong to","What is your lucky number?"]
#
# Answers=["My name is Pratyush","I am from Ujjain","69"]
#
# options = st.selectbox(
#     'Some FAQs?',FAQs
# )
# # options="What is your name"
#
# # if options in FAQs:
# #     st.write(Answers)
#
# for key,i in enumerate(FAQs):
#     if i==options:
#         st.write(Answers[key])
#
#
# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
#
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')
#
# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#
# # import time
# #
# # 'Starting a long computation...'
# #
# # # Add a placeholder
# # latest_iteration = st.empty()
# # bar = st.progress(0)
# #
# # for i in range(100):
# #   # Update the progress bar with each iteration.
# #   latest_iteration.text(f'Iteration {i+1}')
# #   bar.progress(i + 1)
# #   time.sleep(0.1)
# #
# # '...and now we\'re done!'


