# Function to replace hashes with [HASH] tokens in a text string
def replace_hashes_with_tokens(text):
    return text.replace('#', '[HASH]')

# Example text string
text = "This is a #sample text with #hashtags included."

# Replace hashes with [HASH] tokens
result = replace_hashes_with_tokens(text)

# Output the result
print(result)
