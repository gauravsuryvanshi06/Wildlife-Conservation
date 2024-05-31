
import firebase_admin
from firebase_admin import credentials

def get_firebase_app():
    if not firebase_admin._apps:
        cred_path = 'wildlife-comprehension-75d27ea2fd6b.json'
        cred = credentials.Certificate(cred_path)
        firebase_app = firebase_admin.initialize_app(cred)
    else:
        firebase_app = firebase_admin.get_app()  
    return firebase_app
# Path: firebase_setup.py