'''
letters = input('please Enter The letters:')
count = dict()
for letter in letters:
	count[letter] = count.get(letter, 0) + 1

if 2*count['z'] == count['o']:
	print('Yes')
else:
	print('No')
'''

i = 1
input_seats = []
seat_types = ['WS', 'MS', 'AS', 'AS', 'MS', 'WS']
test_cases = input()
while i <= int(test_cases) :
    seat_per_case  = int(input())
    input_seats.append(seat_per_case)
    i+=1
for item in input_seats:
    current_seat_type = seat_types[item % 6 - 1]
    if item%12 == 0:
        units = int(item/12)-1
    else:
        units = int(item/12)
    facing_seat_no = (12*(units+1) - item + 1 )+ 12 * (units)
    #facing_seat_type = facing_seat_no % 6
    facing_seat = seat_types[facing_seat_no % 6 -1]
    print("{} {}".format(facing_seat_no, facing_seat))


