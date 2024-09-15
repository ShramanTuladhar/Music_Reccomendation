import pandas as pd
import pandas as pd

# Define file paths
file_path = {
    'happy': 'Data/happy_cleaned.csv',
    'sad': 'Data/sad_cleaned.csv',
    'angry': 'Data/angry_cleaned.csv',
    'anxious': 'Data/anxious_cleaned.csv',
    'relaxed': 'Data/relaxed_cleaned.csv',
    'excited': 'Data/excited_cleaned.csv',
    'bored': 'Data/bored_cleaned.csv',
    'lonely': 'Data/lonely_cleaned.csv',
    'hopeful': 'Data/hopeful_cleaned.csv',
    'confident': 'Data/confident_cleaned.csv',
    'tired': 'Data/tired_cleaned.csv',
    'irritated': 'Data/irritated_cleaned.csv',
    'surprised': 'Data/surprised_cleaned.csv',
    'grateful': 'Data/grateful_cleaned.csv',
    'fearful': 'Data/fearful_cleaned.csv'
}

# Load DataFrames from CSV files
def load_data(file_path):
    return pd.read_csv(file_path)

mood_dfs= {}

for mood, path in file_path.items():
    mood_dfs[mood] = load_data(path)
    

# Load main DataFrame
df = pd.read_csv('Data/df.csv')
