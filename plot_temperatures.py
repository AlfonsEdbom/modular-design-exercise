import pandas as pd
from matplotlib import pyplot as plt

def read_temperatures_from_file(file_name: str, num_measurements: int, column_name: str):
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column_name]

def compute_statistics(temperatures: list[float]) -> float:
    num_measurements = len(temperatures)
    mean = sum(temperatures) / num_measurements
    return mean

def test_compute_statistics():
    test_data = [i for i in range(1,5)]
    mean = compute_statistics(test_data)
    assert mean == 2.5

def plot_temperatures(temperatures: list[float], mean: float, num_measurements: int) -> None:
    plt.xlabel("Number of measurement")
    plt.ylabel("Air temperatures")
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(f"{num_measurements}.png")
    plt.show()
    plt.clf()

for num_measurements in [25, 100, 500]:
    # read data from file
    temperatures = read_temperatures_from_file("temperatures.csv", num_measurements, "Air temperature (degC)")

    # compute statistics
    mean = compute_statistics(temperatures) 

    # plot results
    plot_temperatures(temperatures, mean, num_measurements)