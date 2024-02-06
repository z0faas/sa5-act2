def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

choice = input("Enter 't' for text or 'f' for file: ")

if choice == 't':
    text = input("Enter text to check for palindrome: ")
    check_palindrome(text)
elif choice == 'f':
    try:
        filepath = input("Enter filepath for palindrome check: ")
        text = open(filepath, "r").read()
        check_palindrome(text)
    except OSError:
        print(f"Unable to process file at {filepath}")
else:
    print("Invalid choice"