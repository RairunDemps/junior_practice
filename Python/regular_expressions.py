import re

pattern = ['^a...s$', '[abc]', '[^abc]', '..',
        '^b', 'a$', 'ma*n', 'ma+n', 'ma?n', 'a{2,3}',
        'a|b', '(a|b|c)xz', '\Athe', '\bfoo', 'foo\b',
        '\Bfoo', 'foo\B', '\d', '\D', '\s',
        '\S', '\w', '\W', 'Python\Z']
test_string = ['abyss', 'abc de ca', 'hey jedi', 'abcd',
        'bat', 'ada', 'mn', 'man', 'mn', 'aabc daaaat',
        'acdbea', 'axz cabxz', 'the sun', 'a football', 'the afoo test',
        'afootball', 'the afootest', '12abc3', '1ab34"50', 'Python RegEx',
        'a b', '12&": ;c', '1a2%c', 'I like Python']

for i in range(0, len(pattern)):
    result_match = re.match(pattern[i], test_string[i])
    result_findall = re.findall(pattern[i], test_string[i])
    result_split = re.split(pattern[i], test_string[i])
    result_sub = re.sub(pattern[i], '', test_string[i])
    result_subn = re.subn(pattern[i], '', test_string[i])
    result_search = re.search(pattern[i], test_string[i])
    
    print(f"pattern '{pattern[i]}', "\
        f"test_string '{test_string[i]}', "\
        f"|result.match {result_match},| "\
        f"|result.findall {result_findall},| "\
        f"|result.split {result_split}| "\
        f"|result.sub {result_sub}| "\
        f"|result.subn {result_subn}| "\
        f"|result.search {result_search}\n")


string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(f" group {match.group()}, span {match.span()}, match.re {match.re}, match.string {match.string}")
else:
  print("pattern not found")

# raw string example
string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)
