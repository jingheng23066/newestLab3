import temperature

def test_find_min_max():
    # Test case for finding minimum and maximum values
    data = [3, 7, 2, 9, 1]
    min_val, max_val = temperature.find_min_max(data)
    assert min_val == 1
    assert max_val == 9

def test_calc_average():
    # Test case for calculating average
    data = [3, 7, 2, 9, 1]
    avg = temperature.calc_average(data)
    assert avg == 4.4

def test_calc_median_temperature():
    # Test case for calculating median temperature
    temperatures = [25, 30, 22, 18, 20]
    median = temperature.calc_median_temperature(temperatures)
    assert median == 22