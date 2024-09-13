import streamlit as st
import pickle
import gdown

# Title for your app
st.title("Movie Recommendation System")

# Function to download the large file from Google Drive
def download_similarity_file():
    url = "https://drive.google.com/file/d/10IPPAsFbnvuq5wf5n7jJMPhMv8txewr4/view?usp=drive_link"  # Replace 'your_file_id' with actual Google Drive file ID
    output = "similarity.pkl"
    
    # Download the file if it doesn't exist locally
    try:
        gdown.download(url, output, quiet=False)
        st.write("File downloaded successfully!")
    except Exception as e:
        st.write(f"Error downloading file: {e}")

# Download the similarity file if not already present
download_similarity_file()

# Load the downloaded file
try:
    with open('similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)
    st.write("File loaded successfully!")
except FileNotFoundError:
    st.error("Could not find the similarity.pkl file!")

