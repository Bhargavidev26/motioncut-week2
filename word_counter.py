def word_counter(text):
    """
    Counts the number of words in the input text.
    Args:
        text (str): The input sentence or paragraph.
    Returns:
        int: The word count.
    """
    # Split the input into words using spaces as separators
    words = text.split()
    # Return the word count
    return len(words)

def main():
    try:
        user_input = input("Please enter a sentence or paragraph: ")
        if not user_input:
            print("Error: Empty input. Please provide some text.")
        else:
            count = word_counter(user_input)
            print(f"Word count: {count}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()