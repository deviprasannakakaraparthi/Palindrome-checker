def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def process_file(input_file, output_file):
    """Read strings from input_file, check if they are palindromes, and write results to output_file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip()
            result = "Palindrome" if is_palindrome(word) else "Not a Palindrome"
            outfile.write(f"{word}: {result}\n")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'results.txt'
    
    try:
        process_file(input_file, output_file)
        print("Processing complete. Results saved to results.txt.")
    except Exception as e:
        print(f"An error occurred: {e}")

