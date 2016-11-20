# Enter your code here. Read input from STDIN. Print output to STDOUT
input_data = raw_input() 
has_change = True
while has_change and input_data:
    result = []
    has_change = False
    previous_char = input_data[0]
    for c in input_data[1:]:
        if c != previous_char:
            result.append(previous_char)
            previous_char = c
        else:
            previous_char = ''
            has_change = True
    if previous_char != '':
        result.append(input_data[-1])
    input_data = ''.join(result)

print input_data if input_data else "Empty String"
