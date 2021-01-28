from datetime import date

def days_diff(a, b):
	start_date = date(*a)
	date_end = date(*b)
	result = abs((date_end - start_date).days)
	return result

if __name__ == '__main__':

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238