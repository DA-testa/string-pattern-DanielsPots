#221RDB387
# python3

def read_input():
    input_letter = input().strip().upper()
    if input_letter == "I":
        pattern = input().strip()
        text = input().strip()
    elif input_letter == "F":
        file_name = 'tests/06'
        with open(file_name) as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
    else:
        print("try again")
        exit()
    return input_letter, pattern, text

def print_occurrences(occurrences):
    print(' '.join(map(str, occurrences)))

def get_occurrences(input_version, pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    result = []

    if input_version == "I":
        for i in range(text_len - pattern_len + 1):
            if text[i: i + pattern_len] == pattern:
                result.append(i)
    elif input_version == "F":
        pattern_hash = 0
        text_hash = 0
        for i in range(pattern_len):
            pattern_hash += ord(pattern[i]) * pow(10, pattern_len - i - 1)
            text_hash += ord(text[i]) * pow(10, pattern_len - i - 1)         
        
        for i in range(text_len - pattern_len + 1):
            if text_hash == pattern_hash:
                if text[i:i + pattern_len] == pattern:
                    result.append(i)
            
            if i < text_len - pattern_len:
                text_hash = (text_hash - ord(text[i]) * pow(10, pattern_len - 1)) * 10 + ord(text[i + pattern_len])                
    return result

if __name__ == '__main__':
    input_version, pattern, text = read_input()
    occurrences = get_occurrences(input_version, pattern, text)
    print_occurrences(occurrences)
