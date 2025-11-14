

def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Function that calculates the edit distance between two strings using the Levenshtein Algorithm.

    Technique: Tabulation 
    """
    table = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(len(str1) + 1):
        table[0][i] = i

    for j in range(len(str2) + 1):
        table[j][0] = j

    for j in range(1, len(str2) + 1):
        for i in range(1, len(str1) + 1):
            if str2[j - 1] == str1[i - 1]:
                table[j][i] = table[j - 1][i - 1]

            else:
                table[j][i] = 1 + min(
                    table[j][i - 1],
                    table[j - 1][i - 1],
                    table[j - 1][i],
                )

    return table[-1][-1]
