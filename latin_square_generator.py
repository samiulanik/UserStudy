import itertools

system_list = [['baseline','timed','categorization'],['timed','categorization','baseline'],['categorization','baseline','timed']]

video_list = [ ['splatter','fire', 'two'], ['fire', 'two','splatter'],['two','splatter','fire']]

final_list = []

for i in itertools.product(system_list,video_list):
	final_list.append(i)

participant_counter = 1

for i in system_list:
	print i

for i in video_list:
	print i

for i in final_list:
	print i