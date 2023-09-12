import csv
import sys

"""
More interesting race track data in https://github.com/TUMFTM/racetrack-database
"""


def get_racetrack_coordinates(csv_path):
    with open(csv_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        racetrack_coordinates = []
        for row in reader:
            X, Y = map(float, row)
            racetrack_coordinates.append((X, Y))

        return tuple(racetrack_coordinates)


def write_coordinates_to_text_file(coordinates, output_file):
    with open(output_file, mode="w") as file:
        file.write("  <!-- start of race track coordinates -->\n")
        arg_pn = '  <arg name="pN" value="{x: XX, y: YY, z: 0.0}"/>'
        pts = ""
        for pxy in range(len(coordinates)):
            x, y = coordinates[pxy]
            pn = "p" + str(pxy + 1)
            arg = (
                arg_pn.replace("pN", pn)
                .replace("XX", str(float(x)))
                .replace("YY", str(float(y)))
            )
            pts += "$(arg " + pn + "),"
            file.write(arg + "\n")
        file.write("  <!-- end of race track coordinates -->\n")

        file.write("  <!-- list of points that draw the racetrack -->\n")
        arg_pts = '  <arg name="pts" value="points: [points]"/>'
        arg_pts = arg_pts.replace("[points]", "[" + pts[0:-1] + "]")
        file.write(arg_pts + "\n")


def main():
    # Check if the CSV file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python racetrack_arg_converter.py <csv_file_name>")
        sys.exit(1)

    # Get the CSV file name from the command-line argument
    csv_file_name = sys.argv[1]
    output_text_file = csv_file_name.replace(".csv", ".txt")

    # Call the function to print racetrack coordinates
    points = get_racetrack_coordinates(csv_file_name)
    write_coordinates_to_text_file(points, output_text_file)

    print("Copy the covertion result from " + output_text_file)


if __name__ == "__main__":
    main()
