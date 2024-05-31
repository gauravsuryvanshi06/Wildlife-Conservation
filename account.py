import streamlit as st
from firebase_admin import credentials
from firebase_admin import auth 

from firebase_setup import get_firebase_app
import firebase_admin

# if credentials.Certificate('w.json'): 
#     app = firebase_admin.initialize_app(credentials.Certificate('w.json'))

# app = get_firebase_app()
def account():

    st.title('Welcome to :green[Wildlife Insights]')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f(): 
        try:
            user = auth.get_user_by_email("user@example.com")
            #print(user.uid)
            st.write("Logged In Successfully")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False 


    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        # email = st.text_input('Email Address')
        # password = st.text_input('Password',type='password')
        # st.session_state.email_input = email
        # st.session_state.password_input = password
        
        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password',type = 'password')
            st.button('Login',on_click= f)
        
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password',type = 'password')
            username = st.text_input('Enter your Unique UserName')
            
            if st.button('Create my Account'):
                user = auth.create_user(email = email,password = password,uid=username)
                st.success('Account created Successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()

    if st.session_state.signout:
                    st.text('Name '+st.session_state.username)
                    st.text('Email id: '+st.session_state.useremail)
                    st.button('Sign out', on_click=t) 

        
                
      