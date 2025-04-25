import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import datetime

# Updated Bus Schedule Data
bus_schedule = {
    "ISBT-43": [
        {"destination": "Airport", "distance": 15.3, "coords": (8, 9), "schedule": ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]},
        {"destination": "Kaimbwala", "distance": 15.5, "coords": (6, 8), "schedule": ["06:30", "09:30", "12:30", "15:30", "18:30"]},
        {"destination": "Mata Mansa Devi", "distance": 19.6, "coords": (9, 7), "schedule": ["07:00", "10:00", "13:00", "16:00", "19:00"]},
        {"destination": "Saketri", "distance": 24, "coords": (5, 9), "schedule": ["06:15", "09:15", "12:15", "15:15", "18:15"]},
        {"destination": "Railway Station", "distance": 12, "coords": (7, 2), "schedule": ["06:20", "09:20", "12:20", "15:20", "18:20"]}
    ],
    "ISBT-17": [
        {"destination": "Sector 34", "distance": 5, "coords": (3, 6), "schedule": ["06:10", "09:10", "12:10", "15:10", "18:10"]},
        {"destination": "PGI", "distance": 7, "coords": (4, 7), "schedule": ["06:20", "09:20", "12:20", "15:20", "18:20"]},
        {"destination": "Punjab University", "distance": 6, "coords": (3, 8), "schedule": ["06:30", "09:30", "12:30", "15:30", "18:30"]},
        {"destination": "Sector 17 Plaza", "distance": 3, "coords": (5, 5), "schedule": ["06:40", "09:40", "12:40", "15:40", "18:40"]},
        {"destination": "Sector 22", "distance": 4, "coords": (4, 4), "schedule": ["06:50", "09:50", "12:50", "15:50", "18:50"]}
    ],
    "PGI": [
        {"destination": "IT Park", "distance": 21.0, "coords": (6, 9), "schedule": ["06:00", "09:00", "12:00", "15:00", "18:00"]},
        {"destination": "DERABASSI", "distance": 35.0, "coords": (9, 1), "schedule": ["06:15", "09:15", "12:15", "15:15", "18:15"]},
        {"destination": "CHHATTBIR ZOO", "distance": 27.9, "coords": (2, 3), "schedule": ["06:30", "09:30", "12:30", "15:30", "18:30"]},
        {"destination": "ZIRAKPUR", "distance": 20.0, "coords": (8, 2), "schedule": ["07:00", "10:00", "13:00", "16:00", "19:00"]},
        {"destination": "NEW AIRPORT", "distance": 30.9, "coords": (9, 9), "schedule": ["07:30", "10:30", "13:30", "16:30", "19:30"]}
    ],
    "Landran": [
        {"destination": "DERA BASSI", "distance": 34.0, "coords": (9, 0.5), "schedule": ["06:00", "09:00", "12:00", "15:00", "18:00"]},
        {"destination": "PGI", "distance": 24.6, "coords": (5, 7), "schedule": ["06:30", "09:30", "12:30", "15:30", "18:30"]}
    ]
}

# Function to create individual graphs
def plot_bus_routes(stop_name, color):
    G = nx.DiGraph()
    for route in bus_schedule[stop_name]:
        G.add_edge(stop_name, route["destination"], weight=route["distance"], schedule=route["schedule"])

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=color, font_size=10, font_weight="bold", edge_color="gray", width=2, alpha=0.8)
    edge_labels = {(u, v): f"{d['weight']} km\n({', '.join(d['schedule'])})" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="black")
    plt.title(f"Bus Routes from {stop_name} with Distance & Timings")
    plt.show()

# Plot routes for all stops
plot_bus_routes("ISBT-43", "lightblue")
plot_bus_routes("ISBT-17", "lightgreen")
plot_bus_routes("PGI", "orange")
plot_bus_routes("Landran", "teal")

# Load Chandigarh Map and plot ISBT-43 and ISBT-17
map_image_path1 = r"C:\Users\user\Desktop\bus1.png"
img1 = mpimg.imread(map_image_path1)
isbt_coords = {"ISBT-43": (3, 7), "ISBT-17": (7, 5)}

plt.figure(figsize=(12, 8))
plt.imshow(img1, extent=[0, 10, 0, 10])

# Plot ISBT stops
for stop, coords in isbt_coords.items():
    plt.scatter(*coords, c="red" if stop == "ISBT-43" else "purple", s=200, label=stop, edgecolors="black")

# Draw routes from ISBTs
for stop, routes in bus_schedule.items():
    if stop in isbt_coords:
        for route in routes:
            x_dest, y_dest = route["coords"]
            color = "blue" if stop == "ISBT-43" else "green"
            plt.scatter(x_dest, y_dest, c=color, s=100, edgecolors="black")
            plt.arrow(isbt_coords[stop][0], isbt_coords[stop][1], 
                      x_dest - isbt_coords[stop][0], y_dest - isbt_coords[stop][1],
                      head_width=0.2, head_length=0.3, fc=color, ec=color, linestyle="-", alpha=0.7)
            plt.text(x_dest, y_dest, f"{route['destination']}\n{route['distance']} km", fontsize=9, ha="right", color="black")

plt.legend()
plt.title("Chandigarh Bus Routes (ISBT-43 & ISBT-17) with Directions")
plt.show()

# Plot PGI and Landran routes on Chandigarh map
map_image_path2 = r"C:\Users\user\Documents\bus2.png"
img2 = mpimg.imread(map_image_path2)
pgi_coords = {"PGI": (5, 7), "Landran": (2, 2)}

plt.figure(figsize=(12, 8))
plt.imshow(img2, extent=[0, 10, 0, 10])

for stop, coords in pgi_coords.items():
    plt.scatter(*coords, c="orange" if stop == "PGI" else "teal", s=200, label=stop, edgecolors="black")

for stop in pgi_coords:
    for route in bus_schedule[stop]:
        x_dest, y_dest = route["coords"]
        color = "orange" if stop == "PGI" else "teal"
        plt.scatter(x_dest, y_dest, c=color, s=100, edgecolors="black")
        plt.arrow(pgi_coords[stop][0], pgi_coords[stop][1], 
                  x_dest - pgi_coords[stop][0], y_dest - pgi_coords[stop][1],
                  head_width=0.2, head_length=0.3, fc=color, ec=color, linestyle="-", alpha=0.7)
        plt.text(x_dest, y_dest, f"{route['destination']}\n{route['distance']} km", fontsize=9, ha="right", color="black")

plt.legend()
plt.title("PGI & Landran Bus Routes on Chandigarh Map")
plt.show()

# Scheduling function
def get_next_bus(source, destination):
    source = source.strip().upper()
    destination = destination.strip().upper()
    for src, routes in bus_schedule.items():
        if src.upper() == source:
            for route in routes:
                if route["destination"].upper() == destination:
                    current_time = datetime.now().strftime("%H:%M")
                    next_bus_times = [time for time in route["schedule"] if time > current_time]
                    return next_bus_times[0] if next_bus_times else "No more buses today"
    return "Route not found"

# Console Interface
while True:
    print("\nBus Scheduling System")
    print("1. Check Next Bus Timing")
    print("2. Exit")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        source = input("Enter source (ISBT-43 / ISBT-17 / PGI / Landran): ")
        destination = input("Enter destination: ")
        next_bus = get_next_bus(source, destination)
        print(f"Next bus from {source} to {destination} is at {next_bus}")
    elif choice == "2":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
