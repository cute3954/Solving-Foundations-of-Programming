# https://codingbat.com/prob/p256268
#
# Fix this duplicate collapsing code:
# public String collapseDuplicates(String a) { int i = 0; String result = "";
# while (i < a.length()) { char ch = a.charAt(i); result += ch;
# while (a.charAt(i+1) == ch) { i++; } i++; } return result; }
#
# collapseDuplicates("a") → "a"
# collapseDuplicates("aa") → "a"
# collapseDuplicates("abc") → "abc"
def collapseDuplicates(a):
    i = 0
    result = ""

    while i < len(a):
        ch = a[i]
        if result == "" or result[len(result) - 1] != ch:
            result += ch
        i += 1

    return result

result = collapseDuplicates("abbbcaaaccc")
print(result)