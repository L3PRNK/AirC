import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def login():
    # Initialize Firebase Admin SDK without a JSON file
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'your-project-id'
    })

    # Initialize Firestore database
    db = firestore.client()

    # Function to check user credentials
    def check_credentials(username, password):
        # Get a reference to the users collection
        users_ref = db.collection('users')
        # Query for the user document
        query = users_ref.where('username', '==', username).where('password', '==', password).limit(1).get()
        # Check if the query returned any documents
        if len(query) == 1:
            return True
        else:
            return False

    # Prompting the user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check user credentials
    if check_credentials(username, password):
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Invalid username or password. Please try again.")

# Calling the login function to start the login process
login()
