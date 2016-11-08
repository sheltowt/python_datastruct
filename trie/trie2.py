_end = '_end_'

# *args = list of arguments as positional arguments
# **kwargs = dictionary whose keys become separate keyword arguments and values


def make_trie(*words):
	root = dict()
	for word in words:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		current_dict[_end] = _end
	return root

def in_trie(trie, word):
	current_dict = trie 
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return False
	else:
		if _end in current_dict:
			return True
		else:
			return False

make_trie('foo', 'bar', 'baz', 'barz')