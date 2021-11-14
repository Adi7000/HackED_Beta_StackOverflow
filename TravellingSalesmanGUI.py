import tkinter as tk
from PIL import ImageTk, Image
from math import sqrt
import os
from greedy import *
from copy import deepcopy

dictionary_of_cities = {
    'ATL': ["Hartsfield-Jackson International Airport", 'Atlanta', 'GA', (618, 356)],
    'LAX': ["Los Angeles International Airport", 'Los Angeles', 'CA', (55, 309)],
    'ORD': ["O'Hare International Airport", 'Chicago', 'IL', (548, 193)],
    'DFW': ["Dallas/Fort Worth International Airport", 'Dallas & Ft. Worth', 'TX', (408, 381)],
    'DEN': ["Denver International Airport", 'Denver', 'CO', (290, 235)],
    'CLT': ["Charlotte Douglas International Airport", 'Charlotte', 'NC', (671, 316)],
    'LAS': ["McCarran International Airport", 'Las Vegas', 'NV', (117, 281)],
    'PHX': ["Phoenix Sky Harbor International Airport", 'Phoenix', 'AZ', (159, 342)],
    'MCO': ["Orlando International Airport", 'Orlando', 'FL', (688, 453)],
    'SEA': ["Seattle–Tacoma International Airport", 'Seattle', 'WA', (73, 34,)],
    'MIA': ["Miami International Airport", 'Miami', 'FL', (714, 504)],
    'IAH': ["George Bush Intercontinental Airport", 'Houston', 'TX', (436, 440)],
    'JFK': ["John F. Kennedy International Airport", 'New York City', 'NY', (761, 187)],
    'FLL': ["Fort Lauderdale–Hollywood International", 'Fort Lauderdale', 'FL', (716, 499)],
    'SFO': ["San Francisco International Airport", 'San Francisco', 'CA', (13, 219)],
    'MSP': ["Minneapolis–Saint Paul International Airport", 'Minneapolis & Saint Paul', 'MN', (468, 138)],
    'BOS': ["Logan International Airport", 'Boston', 'MA', (796, 143)],
    'PHL': ["Philadelphia International Airport", 'Philadelphia', 'PA', (743, 207)],
    'STL': ["St. Louis Lambert International Airport", 'St. Louis', 'MO', (516, 261)],
    'BWI': ["Baltimore/Washington International Airport", 'Baltimore & Washington, D.C.', 'MD', (723, 236)],
    'TPA': ["Tampa International Airport", 'Tampa', 'FL', (667, 466)],
    'SAN': ["San Diego International Airport", 'San Diego', 'CA', (69, 341)],
    'SLC': ["Salt Lake City International Airport", 'Salt Lake City', 'UT', (186, 199)],
    'IAD': ["Washington Dulles International Airport", 'Washington, D.C.', 'VA', (727, 226)],
    'LGA': ["LaGuardia Airport", 'New York', 'NY', (761, 186)],
    'DCA': ["Ronald Reagan Washington National Airport", 'Washington, D.C', 'VA', (714, 234)],
    'PDX': ["Portland International Airport", 'Portland', 'OR', (58, 67)],
    'CLE': ["Cleveland Hopkins International Airport", 'Cleveland', 'OH', (639, 194)],
    'CVG': ["Cincinnati/Northern Kentucky International Airport", 'Cincinnati', 'KY', (604, 249)],
    'MEM': ["Memphis International Airport", 'Memphis', 'TN', (524, 336)],
    'MDW': ["Chicago Midway International Airport", 'Chicago', 'IL', (550, 200)],
    'PIT': ["Pittsburgh International Airport", 'Findlay and Moon Township', 'PA', (667, 214)],
    'WER': ["Newark Liberty International Airport", 'Newark, Elizabeth', 'NJ', (757, 186)],
    'DTW': ["Detroit Metropolitan Wayne County Airport", "Romulus", "MI", (615, 182)]
}
dictionary_of_cities_by_locations = {
    "(618, 356)": "Hartsfield-Jackson International Airport",
    "(55, 309)": "Los Angeles International Airport",
    "(548, 193)": "O'Hare International Airport",
    "(408, 381)": "Dallas/Fort Worth International Airport",
    "(290, 235)": "Denver International Airport",
    "(671, 316)": "Charlotte Douglas International Airport",
    "(117, 281)": "McCarran International Airport",
    "(159, 342)": "Phoenix Sky Harbor International Airport",
    "(688, 453)": "Orlando International Airport",
    "(73, 34)": "Seattle–Tacoma International Airport",
    "(714, 504)": "Miami International Airport",
    "(436, 440)": "George Bush Intercontinental Airport",
    "(761, 187)": "John F. Kennedy International Airport",
    "(716, 499)": "Fort Lauderdale–Hollywood International",
    "(13, 219)": "San Francisco International Airport",
    "(468, 138)": "Minneapolis–Saint Paul International Airport",
    "(796, 143)": "Logan International Airport",
    "(743, 207)": "Philadelphia International Airport",
    "(516, 261)": "St. Louis Lambert International Airport",
    "(723, 236)": "Baltimore/Washington International Airport",
    "(667, 466)": "Tampa International Airport",
    "(69, 341)": "San Diego International Airport",
    "(186, 199)": "Salt Lake City International Airport",
    "(727, 226)": "Washington Dulles International Airport",
    "(761, 186)": "LaGuardia Airport",
    "(714, 234)": "Ronald Reagan Washington National Airport",
    "(58, 67)": "Portland International Airport",
    "(639, 194)": "Cleveland Hopkins International Airport",
    "(604, 249)": "Cincinnati/Northern Kentucky International Airport",
    "(524, 336)": "Memphis International Airport",
    "(550, 200)": "Chicago Midway International Airport",
    "(667, 214)": "Pittsburgh International Airport",
    "(757, 186)": "Newark Liberty International Airport",
    "(615, 182)": "Detroit Metropolitan Wayne County Airport"

}


def airport_selected(airport, temp_canvas, r=7):
    global visited_airports
    if len(desired_airports) == 0:  # If it is the starting point, dot will be green
        color = 'green'
    else:
        if airport[0] in visited_airports:  # Otherwise, dot will be red
            return
        color = 'red'

    coords = airport[3]
    x0 = coords[0] - r
    x1 = coords[0] + r
    y0 = coords[1] - r
    y1 = coords[1] + r

    desired_airports.append(coords)  # Appends relevant data for future reference
    visited_airports.append(airport[0])  # Appends relevant data for future reference
    return temp_canvas.create_oval(x0, y0, x1, y1, fill=color)


def add_airports():
    addAirports["state"] = tk.DISABLED  # Disables the button that gets the user here

    # Adds a button for every single airport in the dictionary
    airport_root = tk.Tk()
    airport_root.config(bg="#ADD8E6")
    airport_root.wm_title("Add Airports")
    n = 1
    m = 0
    for airport in sorted(dictionary_of_cities.values()):
        btn = tk.Button(airport_root, text=airport[0], bg="#D3D3D3", command=lambda airport=airport: airport_selected
        (airport, canvas))
        btn.grid(row=n, column=m)
        n += 1
        if n == 18 and m == 0:
            m += 2
            n = 1
    done_btn = tk.Button(airport_root, text='Calculate Flight Path', bg='#D3D3D3', command=lambda:
                         algorithm_select(airport_root))
    done_btn.grid(row=0, column=1)
    pass


def algorithm_select(old_root):
    # Prompts the user to select the algorithm they wish to use

    old_root.destroy()
    new_root = tk.Tk()
    new_root.geometry("700x850")
    new_root.config(bg='#ADD8E6')
    new_root.wm_title('Select An Algorithm')

    greedy_btn = tk.Button(new_root, text='Greedy Algorithm', bg='#D3D3D3', command=lambda:
    greedy_plot(new_root, desired_airports, canvas))
    greedy_btn.pack()

    sectional_btn = tk.Button(new_root, text='Sectional Algorithm', bg='#D3D3D3', command=lambda:
    sectional_plot(new_root, desired_airports, canvas))
    sectional_btn.pack()

    compare_btn = tk.Button(new_root, text='Compare both options', bg='#D3D3D3', command=lambda:
    compare(new_root, desired_airports, canvas))
    compare_btn.pack()

    global btn_list
    btn_list = [greedy_btn, sectional_btn, compare_btn]

    return


def draw_line(old_root, points, canvas, algorithm_type, color='red', thickness="5", create_btns=False):
    remove_buttons(btn_list)
    distance = 0
    for i in range(len(points)):
        if i == len(points) - 1:  # Breaks out when final point is reached, it was already connected by prev. loop
            break
        else:
            canvas.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], fill=color,
                               width=thickness, arrow=tk.LAST, arrowshape=(16, 20, 6))
            distance += sqrt((points[i][0] - points[i + 1][0]) ** 2 + (points[i][1] - points[i + 1][1]) ** 2)
    # Prints some important statistics such as the order of airports travelled and the distance travelled
    ordered_airports = []
    for key in points:
        ordered_airports.append(dictionary_of_cities_by_locations[str(key)])

    airports_visited_label = tk.Label(old_root, text="Using the " + algorithm_type + ' (' + color + ')'
                                                     " algorithm your flight path is:\n" +
                                                     " to ".join(visited_airports), wraplength="400", bg='#FFFFFF')
    airports_visited_label.pack(pady=20)
    distance_label = tk.Label(old_root, text="Your travel distance is roughly " + str(round(distance*5.545541)) + ' km',
                              wraplength="400", bg='#FFFFFF')
    distance_label.pack(pady=10)
    if create_btns is True:
        new_trip_btn = tk.Button(old_root, text="New Trip", bg='#D3D3D3', command=lambda: rerun_program(old_root))
        new_trip_btn.pack()
        quit_btn = tk.Button(old_root, text='Quit', bg='#D3D3D3', command=lambda: close_program(old_root))
        quit_btn.pack()
    return


def compare(old_root, points, canvas):
    points_copied = deepcopy(points)
    greedy_points = greedy(points)
    sectional_points = sectional(points_copied)

    draw_line(old_root, greedy_points, canvas, 'greedy')
    draw_line(old_root, sectional_points, canvas, 'sectional', "orange", "3", create_btns=True)
    pass


def greedy_plot(root, points, canvas):
    ordered_points = greedy(points)
    draw_line(root, ordered_points, canvas, 'greedy')
    pass


def sectional_plot(root, points, canvas):
    ordered_points = sectional(points)
    draw_line(root, ordered_points, canvas, 'sectional')
    pass


def close_program(new_root):
    root.destroy()
    new_root.destroy()
    pass


def remove_buttons(button_list):
    for button in button_list:
        button.destroy()
    pass


def rerun_program(new_root):
    close_program(new_root)
    os.system("python TravellingSalesmanGUI.py")
    exit()
    pass


desired_airports = []
visited_airports = []
# Creates the main window
root = tk.Tk()
root.wm_title("Trip Planner")

# Creates the canvas on which the images and geometry
canvas = tk.Canvas(root, width="850", height="525", bg="white")
canvas.pack()

test = Image.open("Map.png")
airport_map = ImageTk.PhotoImage(Image.open("Map.png"))
canvas.create_image(0, 0, image=airport_map, anchor="nw")
addAirports = tk.Button(root, text="Plan Trip", padx=10, pady=5, fg="black", bg="#D3D3D3", command=add_airports)
addAirports.pack()

root.mainloop()
