import matplotlib.pyplot as plt

def plot_points():
    num_points = int(input("how many points do you want to plot? "))

    x_coords = []
    y_coords = []

    for i in range(num_points):
        print(f"\nenter coordinates for point {i+1}:")
        try:
            x = float(input(f"x{i+1}: "))
            y = float(input(f"y{i+1}: "))
            x_coords.append(x)
            y_coords.append(y)
        except ValueError:
            print("invalid input")
            return

    if not x_coords:
        print("no points to plot")
        return

    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='red', marker='o', label='Points')

    for i in range(len(x_coords)):
        plt.text(x_coords[i] + 0.1, y_coords[i] + 0.1, f'P{i+1}({x_coords[i]}, {y_coords[i]})')

    plt.title('plotting points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.show()

plot_points()
