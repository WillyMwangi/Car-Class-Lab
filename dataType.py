#DATA TYPES LAB
#Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
# Complete the test to produce the perfect function that accounts for all expectations.

def data_type(a):
	"""Takes one input and returns a value in respect to data type of the input  """
	a_type =type(a)
	if a_type == str:
		return len(a)           # For strings, return its length.
	elif a_type ==bool:
		return a        # For booleans return the boolean
	elif a_type ==int:
		if a == 100:
			return 'equal to 100'   # For integers return a string showing how it compares to hundred e.g. For 67
		elif a < 100:
			return 'less than 100'  #return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be

		else:
			return 'more than 100'

	elif a_type ==list:
		try:
			if a[2]:
				return a[2]     # For lists return the 3rd item, or None if it doesn't exist
		except(IndexError):
			return None
	else:
		return 'no value'    # For None return string 'no value'