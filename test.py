import os
import nltk

# Function to download NLTK stopwords corpus and save it to a folder
def download_stopwords(save_dir):
    # Download the stopwords corpus
    nltk.download('stopwords')
    # Get the path to the downloaded corpus
    stopwords_path = nltk.data.find('corpora/stopwords')
    # Define the destination directory
    dest_dir = os.path.join(save_dir, 'stopwords')
    # Create the directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    # Copy the stopwords corpus to the destination directory
    with open(os.path.join(dest_dir, 'stopwords.txt'), 'w') as f:
        f.write('\n'.join(nltk.corpus.stopwords.words('english')))
    # Return the path to the downloaded corpus
    return stopwords_path

# Define the directory where you want to save the stopwords corpus
save_directory = '/Users/pruthvipatel/Documents/projects/FakeNewsApp_API/nltk_data'

# Call the function to download and save the stopwords corpus
stopwords_path = download_stopwords(save_directory)

# Now you can use the stopwords_path variable if needed
print("Stopwords downloaded and saved to:", stopwords_path)
