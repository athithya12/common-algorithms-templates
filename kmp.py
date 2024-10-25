def kmp_search(pattern, text):
    # Step 1: Preprocess the pattern to create the lps array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[
                        length - 1
                    ]  # Fallback to the previous longest prefix suffix
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # Step 2: Search the pattern in the text
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    result = []  # Store the starting indices of matches

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):  # A match is found
            result.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:  # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]  # Fall back to lps[j-1]
            else:
                i += 1  # Move text index forward

    return result


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(pattern, text)
print("Pattern found at indices:", matches)
