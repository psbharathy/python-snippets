# Python Assert 
def attendance(days):
	assert len(days) !=0, "Days should not be empty"
	return  8 * days[0] 

print("Total number of hours is ",attendance([20]))

print("Total number of hours is ",attendance([]))

# Output 

# Traceback (most recent call last):
#   File "py-assert.py", line 8, in <module>
#     print("Total number of hours is ",attendance([]))
#   File "py-assert.py", line 3, in attendance
#     assert len(days) !=0, "Days should not be empty"
# AssertionError: Days should not be empty
