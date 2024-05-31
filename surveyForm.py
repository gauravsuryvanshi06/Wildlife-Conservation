# import base64
# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# cred = credentials.Certificate('wildlife-comprehension-75d27ea2fd6b.json')
# db = firestore.client()

# def encode_image_to_base64(image):
#     if image is not None:
#         with open(image.name, "rb") as img_file:
#             return base64.b64encode(img_file.read()).decode('utf-8')
# def save_to_firestore(answer1, answer2,answer3,answer4,answer5,answer6,files):
#         # Add a new document with a generated ID to the collection
#         doc_ref = db.collection(u'survey_responses').add({
#             u'question1': answer1,
#             u'question2': answer2,
#             u'question3': answer3,
#             u'question4': answer4,
#             u'question5': answer5,
#             u'question6': answer6,
#             # Add more fields for additional questions
#         })
#         if files:
#             storage_ref = firebase_admin.storage.bucket("your-storage-bucket")
#             for file_idx, file in enumerate(files):
#              blob = db.blob(f"files/{doc_ref.id}/file{file_idx + 1}.jpg") 
#              blob.upload_from_file(file)

# def survey_form():
#         st.title(':green[Survey Form]')
        
#         # Text questions
#         question1 = st.text_input("Please enter your first and last name:")
#         question2 = st.text_input("Please enter the email address you used to sign up for a Wildlife Insights account. We suggest signing up with your organizational email, though if you'd like to download images from your project at a later date you must sign up for an account with a Google associated email.:")
#         question3 = st.text_input("Your affiliation/organization:")
#         question4 = st.selectbox("Organization type:", ["Government", "Academia", "Non Profit","Commercial","Other"])
#         question5 = st.text_area("Describe your project:")
#         question6 = st.text_input("In what country/countries are you or have you collected camera trap data?")
#         files = st.file_uploader("Upload Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

#     # Add more questions as needed

#         # Submit button
#         if st.button("Submit"):
#             # Call a function to save data to Firestore
#             save_to_firestore(question1, question2,question3,question4,question5,question6,files)  # Pass all answers to the function
#             st.success("Survey submitted successfully!")


