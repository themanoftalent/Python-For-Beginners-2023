import re


def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print(
    them to stdout.
    """
    # Show the character positions and input text
    print('*'*18)
    print('Joining Strings with /',''.join(str(i / 10 or ' ') for i in range(len(text))))
    print('*'*18)
    print('Containing % :',''.join(str(i % 10) for i in range(len(text))))
    print('*'*18)
    print('Lets see the content ',text)

    # Look for each pattern in the text and print( the results
    for pattern in patterns:
        print()
        print('*'*18)
        print('Matching "%s"' % pattern)
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print('*'*18)
            print('  %2d : %2d = "%s"' %(s, e - 1, text[s:e]))
    return


if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', ['ab'])
