def removeConsuctiveCharacter(S):
    # if is empty
    if not S:
        return ""
    result = [S[0]]
    for char in S[1:]:
        if char != result[-1]:
            result.append(char)

    return ''.join(result)

s = input("Enter String:")
print("String after removing consuctive string:",removeConsuctiveCharacter(s))