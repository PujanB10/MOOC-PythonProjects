import string
def separate_characters(my_string: str):
    result=()
    letters=""
    punc=""
    rem=""
    for characters in my_string:
        if characters in string.ascii_letters:
            letters+=characters
        elif characters in string.punctuation:
            punc+=characters
        else:
            rem=rem+characters
    return(letters,punc,rem)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])