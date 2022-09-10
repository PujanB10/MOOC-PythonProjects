def anagrams(word1,word2):
    count=0
    for i in word1:
        if i in word2:
            count+=1
    if count==len(word2):
        return True
    return False

if __name__ == "__main__":
    print(anagrams("meta","malt"))