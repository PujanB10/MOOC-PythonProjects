def same_chars(word,ind1,ind2):
    if ind1>len(word)-1 or ind2>len(word)-1 or word[ind1]!=word[ind2]:
        return False
    return True
if __name__ == "__main__":
    print(same_chars("coder", 1,10))