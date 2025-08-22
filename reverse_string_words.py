
def reverseWords(s: str) -> str:
    # Step 1: Split the string by spaces (removes multiple spaces automatically)
    words = s.split()
    
    # Step 2: Reverse the list of words
    words.reverse()
    
    # Step 3: Join the words with a single space
    return " ".join(words)


# ----------- Main Function for Testing -----------

if __name__ == "__main__":
    # Test cases
    test_inputs = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "    ",
        "word"
    ]

    for inp in test_inputs:
        print(f"Input: '{inp}'")
        print(f"Output: '{reverseWords(inp)}'")
        print("-" * 40)
