def longest(strings: list):
    result=""
    for word in strings:
        if len(word)>len(result):
            result=word
    return result
if __name__ == "__main__":
    my_strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(my_strings))