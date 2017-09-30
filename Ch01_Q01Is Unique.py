import sys

input_string = input("Enter the string:")
#input = sys.argv[1]
#print(input)

unique_chars = ''.join(set(input_string))
#print(unique_chars)
print("=================================")

if (len(input_string) == len(unique_chars)):
	print("The input string is unique")
else:
	print("The input string is not unique")
print("==================================")