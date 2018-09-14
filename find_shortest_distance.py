#!/usr/bin/env python3

def find_shortest_distance(a, b, s):
    """
    Finds the shortest distance between substrings a and b in s. Distance is expressed as number of words between the substrings.

    For example:
    >>> find_shortest_distance('motivation', 'development', 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.')
    2

    It does not matter which of the two arguments comes first:
    >>> find_shortest_distance('motivation', 'development', 'We do value and reward development in our motivation team. Motivation is a key skill for a DevOp.')
    2

    If at least one of the arguments cannot be found, this is indicated by a result None:
    >>> find_shortest_distance('foo', 'bar', '') is None
    True

    Search is case-insensitive:
    >>> find_shortest_distance('Foo', 'bar', 'foo Bar')
    0

    Distance between identical arguments expects multiple occurences:
    >>> find_shortest_distance('foo', 'foo', 'foo') is None
    True
    >>> find_shortest_distance('foo', 'foo', 'foo foo')
    0

    Adjacent punctuation is considered part of a word:
    >>> find_shortest_distance('foo', 'bar', 'foo. between bar') is None
    True
    >>> find_shortest_distance('foo', 'bar', 'foo . between bar')
    2

    Words can be split by newlines, tabs or multiple spaces, too:
    >>> find_shortest_distance('foo', 'bar', 'foo\\nbetween\\tbetween  bar')
    2

    Multibyte characters work as well:
    >>> find_shortest_distance('\U0001f604isAnEmoji', 'foo', 'foo bar \U0001f604isAnEmoji')
    1

    Words appearing as parts of other words are not a match:
    >>> find_shortest_distance('foo', 'bar', 'foobaz bar') is None
    True

    The shortest distance need not be the first distance:
    >>> find_shortest_distance('foo', 'bar', 'foo word bar foo')
    0

    Long texts are handled well:
    >>> with open('kafka.txt', 'r') as f:
    ...     find_shortest_distance('he', 'a', f.read())
    1
    """
    a, b = a.lower(), b.lower()
    min_distance, last_match, last_index = None, None, None
    for i, word in enumerate(s.lower().split()):
        if word in (a, b):
            if last_match and (word != last_match or a == b):
                distance = i - last_index - 1
                min_distance = min(distance, min_distance) if min_distance else distance
            last_index = i
            last_match = word
    return min_distance

if __name__ == '__main__':
    import sys

    if (len(sys.argv) != 3):
        print("usage: {} string1 string2".format(sys.argv[0]))
        exit(1)
    print(find_shortest_distance(sys.argv[1], sys.argv[2], sys.stdin.read()))
