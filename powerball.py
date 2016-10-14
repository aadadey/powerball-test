import random

###to test whether string input is a valid integer
def validInt(i, min, max, excl=[]):
    result = False
    try:
        int(i)
        result = True
    except ValueError:
        return result

    return int(i) >= min and int(i) <= max and i not in excl

def getPowerball():
	num = ''
	result = []
	invalidFlag = True

	###loop to get first number
	while invalidFlag:
		num = input('Please enter a number between 1 and 69: ')
		invalidFlag = not validInt(num, 1, 69)

	result.append(num)

	###loop for numbers 2 thru 5
	for i in range(0,4):
		invalidFlag = True
		while invalidFlag:
			print('---\nPowerball numbers selected so far: %s' % ' '.join(result))
			num = input('Please enter a number between 1 and 69, excluding the above: ')
			invalidFlag = not validInt(num, 1, 69, result)
		result.append(num)
	invalidFlag = True

	###for the the 6th
	while invalidFlag:
		print('---\nPowerball numbers selected so far: %s' % ' '.join(result))
		num = input('Please enter a number between 1 and 26: ')
		invalidFlag = not validInt(num, 1, 26)
	result.append(num)

	return result

def printPowerballs(dict):
	for emp in dict:
		first_five = dict[emp][:5]
		pball = dict[emp][5]
		print('%s -- %s Powerball: %s' % (emp, ' '.join(first_five), pball))

def mostCommon(list):
	count_dict = {}
	max_count = 0
	max_list = []
	###get counts for all numbers
	for num in list:
		if num in count_dict.keys():
			count_dict[num] += 1
		else:
			count_dict[num] = 0

	###get max number
	for num in count_dict:
		if count_dict[num] > max_count:
			max_count = count_dict[num]

	###get all numbers with max count1
	for num in count_dict:
		if count_dict[num] == max_count:
			max_list.append(num)

	return random.choice(max_list)

def pickWinner(dict):
	num_list = []
	winner = []

	for emp in dict:
		num_list.append(dict[emp])

	for i in range(0, 6):
		pos_list = []

		for j in range(0, len(num_list)):
			pos_list.append(num_list[j][i])

		winner.append(mostCommon(pos_list))

	printPowerballs({'Winning Powerball': winner})

print('Welcome to Greenphire Powerball! In this game, employees can enter a drawing to win ONE BILLION DOLLARS!')
print('Step right up if you are feeling lucky!\n')
print('In this game, you will be drawing a total of six numbers. The first five must each be between 1 and 69,')
print('with no repeats. The last number (Powerball number) must be between 1 and 26.')
input('Press Enter to continue...')

continue_loop = True
employee_num = 1
powerball_dict = {}

while continue_loop:
	print('\nEmployee #%d\n----------------' % employee_num)
	fname = input('Enter your first name: ')
	lname = input('Enter your last name: ')
	powerball_dict['%s %s' % (fname, lname)] = getPowerball()
	print('\nDrawings Entered:')
	printPowerballs(powerball_dict)
	invalidFlag = True

	while invalidFlag:
		cont = input('Enter another drawing? (Y/N): ')
		invalidFlag = cont.lower() not in ['y', 'n', 'yes', 'no']

	continue_loop = cont.lower() in ['y', 'yes']
	employee_num += 1

pickWinner(powerball_dict)