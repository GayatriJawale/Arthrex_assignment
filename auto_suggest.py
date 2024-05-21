def auto_suggest(input_words, search_pattern):
    output = []

    #function to check if the word matches the pattern
    def matches(word, pattern):
        if pattern.startswith('*') and pattern.endswith('*'):
            # Match between wildcards
            return pattern[1:-1] in word
        elif pattern.startswith('*'):
            # Match any suffix
            return word.endswith(pattern[1:])
        elif pattern.endswith('*'):
            # Match any prefix
            return word.startswith(pattern[:-1])
        else:
            # Match any part
            return pattern in word

    # Filter words based on the search pattern
    for word in input_words:
        if matches(word, search_pattern):
            output.append(word)

    return output

def main():
    print("\u0332".join("Instructions:"))
    print(" 1.Enter up to 5 words. \n 2.Press Enter after each word. \n 3.Leave a blank to stop.")

    input_words = []
    for _ in range(5):
        word = input().strip()
        if word:
            input_words.append(word)
        else:
            break

    search_pattern = input("Enter the search pattern: ").strip()

    output = auto_suggest(input_words, search_pattern)

    print("Output:", output)

if __name__ == "__main__":
    main()

###############################################################    

#Alternate Logic 
# (Couldnt pass the pattern between wildcards test case)

###############################################################
'''
def auto_suggest(input_words, search_pattern):
    def starts_with(input_words, search_pattern):
        prefix = search_pattern.strip('*')
        ele_at_start = []
        for ele in input_words:
            if ele.startswith(input_words,prefix):
                ele_at_start.append(ele)
        print(ele_at_start)


    def ends_with(word, suffix):
        return word.endswith(suffix)

    def contains_pattern(word, pattern):
        return pattern in word

    def matches_pattern(word, pattern):
        prefix, suffix = pattern.split('*')
        return word.startswith(prefix) and word.endswith(suffix)
    
    # def matches_pattern_between(word, pattern):
    #     prefix, middle, suffix = pattern.split('*')
    #     print(word.startswith(prefix) and middle in word and word.endswith(suffix))

    switch = {
        1: ends_with,
        2: starts_with,
        3: matches_pattern,
        4: contains_pattern,
        # 5: matches_pattern_between
    }

    # output = []
    if search_pattern == '':
        search_type = 4
    elif search_pattern.startswith('*'):
        search_type = 1
    elif search_pattern.endswith('*'):
        search_type = 2
    elif '*' in search_pattern:
        search_type = 3
    # elif search_pattern.count('*') == 2:
    #     search_type = 5
    else:
        search_type = 4

    # for word in input_words:
    #     if switch[search_type](word, search_pattern):
    #         output.append(word)
    # return output

def main():
    input_words = []
    print("\u0332".join("Instructions:"))
    print(" 1.Enter up to 5 words. \n 2.Press Enter after each word. \n 3.Leave a blank to stop.")
    for _ in range(5):
        word = input().strip()
        if word:
            input_words.append(word)
        else:
            break
    search_pattern = input("Enter the search pattern: ")
    auto_suggest(input_words, search_pattern)
    # output = auto_suggest(input_words, search_pattern)
    # print("output:", output)

if __name__ == "__main__":
    main()
'''