def compute_statistics(temperatures: list[float]) -> float:
    num_measurements = len(temperatures)
    mean = sum(temperatures) / num_measurements
    return mean

def test_compute_statistics():
    test_data = [i for i in range(1,5)]
    mean = compute_statistics(test_data)
    assert mean == 2.5