## find_shortest_distance

Finds the shortest distance between substrings in a file. Distance is expressed as number of words between the substrings.

### Remarks

Algorithm is chosen as a compromise between readability and performance. For maximum performance, see the alternative algorithm in commit d0e71ff8b0b063121562bc818fb39fca5d3d6b47.

### Usage

The program reads the file to search in from stdin and expects the search substrings as arguments. Example:
```
python3 find_shortest_distance.py find me
```

### Tests

Run the doctests with
```
python3 -m doctest -v find_shortest_distance.py
```
