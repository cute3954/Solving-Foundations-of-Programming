# Given a String
S = 'abppplee'
# Set of Words
D = ['able', 'ale', 'apple', 'bale', 'kangaroo']
# Subsequence of S and Longest Word in D
W = ''
FirstLetterOfS = S[0]
LastLetterOfS = S[len(S)-1]
# Array for Subsequences
Subsequences = []
# Find Subsequences
for i in range(len(D)):
    if D[i].startswith(FirstLetterOfS) and D[i].endswith(LastLetterOfS):
        Subsequences.append(D[i])
# Sort an Array in Descending Order
# without reordering the remaining characters? OMG...
Subsequences = sorted(Subsequences, key=len, reverse=True)

W = Subsequences[0]
print(W)
