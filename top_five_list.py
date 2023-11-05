import pandas as pd
from datetime import datetime

# Define tag mappings for similar tags
tag_mappings = {
    'romance': ['historical romance'],    
}

def preprocess_tags(tags):
    if isinstance(tags, list):
        cleaned_tags = [tag.strip() for tag in tags if tag.strip() != '']
        for key, value in tag_mappings.items():
            if any(tag in cleaned_tags for tag in value):
                cleaned_tags = [key]
                break
        return cleaned_tags
    else:
        return []

start_time = datetime.now()

# Load the JSON data into a Pandas DataFrame
df = pd.read_json('list.json', lines=True)

# Preprocess the 'tags' column
df['tags'] = df['tags'].apply(preprocess_tags)

# Count the tags
tag_counts = df['tags'].explode().value_counts()

# Ignore the empty string
tag_counts = tag_counts[tag_counts.index != '']

# Display the top 5 tag counts
print(tag_counts.head(5))

end_time = datetime.now()
time_taken = end_time - start_time
print("Time taken:", time_taken)

