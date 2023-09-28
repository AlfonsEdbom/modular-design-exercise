import pandas as pd
from matplotlib import pyplot as plt
import click

import my_statistics as stats

def read_temperatures_from_file(file_name: str, num_measurements: int, column_name: str):
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column_name]

def plot_temperatures(temperatures: list[float], mean: float, num_measurements: int, output_file) -> None:
    plt.xlabel("Number of measurement")
    plt.ylabel("Air temperatures")
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(output_file)
    plt.show()
    plt.clf()

@click.command()
@click.option('--num_measurements', help='Number of temperatures to read and plot.', type=int, required = True)
@click.option('--inputfile', help='The input data file', required=True)
@click.option('--outputfile', help='The output image file', required=True)

def main(num_measurements, inputfile, outputfile):

    # read data from file
    temperatures = read_temperatures_from_file(inputfile, num_measurements, "Air temperature (degC)")

    # compute statistics
    mean = stats.compute_statistics(temperatures) 

    # plot results
    plot_temperatures(temperatures, mean, num_measurements, outputfile)

if __name__ == "__main__":
    main()