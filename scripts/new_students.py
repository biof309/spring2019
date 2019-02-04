import difflib
import pathlib

diff = [x.split('\t') for x in difflib.unified_diff(pathlib.Path('old.txt').read_text().split('\n'), pathlib.Path('new.txt').read_text().split('\n')) if x.startswith('+')]
new_names, new_emails = zip(*[x for x in diff if len(x) > 1])
print('\n'.join(new_emails))
