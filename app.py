"""Flight Route Planner - Dijkstra's shortest path algorithm.

Simple educational Flask app. No login, signup, or database is required.
"""
from heapq import heappop, heappush
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "flight-route-planner-demo"

AIRPORTS = {
    "DEL": "Delhi", "JAI": "Jaipur", "BOM": "Mumbai",
    "CCU": "Kolkata", "HYD": "Hyderabad", "MAA": "Chennai",
    "BLR": "Bengaluru",
}

# Directed graph: weights are illustrative flight times in hours.
GRAPH = {
    "DEL": {"JAI": 1.0, "BOM": 2.2, "CCU": 2.1, "HYD": 2.3},
    "JAI": {"BOM": 1.7, "HYD": 2.0},
    "CCU": {"MAA": 2.0, "BLR": 2.5},
    "BOM": {"HYD": 1.4, "BLR": 1.7, "MAA": 1.8},
    "HYD": {"BLR": 1.0, "MAA": 1.2, "CCU": 2.0},
    "MAA": {"BLR": 1.0},
    "BLR": {},
}

def dijkstra(source, destination):
    distances = {airport: float("inf") for airport in GRAPH}
    previous = {}
    distances[source] = 0.0
    priority_queue = [(0.0, source)]
    settled_order = []

    while priority_queue:
        current_distance, current_airport = heappop(priority_queue)
        if current_distance > distances[current_airport]:
            continue
        settled_order.append(current_airport)
        if current_airport == destination:
            break
        for neighbour, flight_time in GRAPH[current_airport].items():
            new_distance = current_distance + flight_time
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current_airport
                heappush(priority_queue, (new_distance, neighbour))

    if distances[destination] == float("inf"):
        return None

    path = []
    current = destination
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(source)
    path.reverse()

    legs = []
    for start, end in zip(path, path[1:]):
        legs.append({
            "from": start, "to": end,
            "from_city": AIRPORTS[start], "to_city": AIRPORTS[end],
            "hours": GRAPH[start][end],
        })
    return {"distance": distances[destination], "path": path,
            "legs": legs, "settled_order": settled_order}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    source = "DEL"
    destination = "BLR"
    if request.method == "POST":
        source = request.form.get("source", "")
        destination = request.form.get("destination", "")
        if source not in AIRPORTS or destination not in AIRPORTS:
            flash("Please select valid source and destination airports.", "error")
        elif source == destination:
            result = {"distance": 0.0, "path": [source], "legs": [],
                      "settled_order": [source]}
        else:
            result = dijkstra(source, destination)
            if result is None:
                flash(f"No listed route is available from {source} to {destination}.", "error")
    return render_template("index.html", airports=AIRPORTS, graph=GRAPH,
                           result=result, source=source, destination=destination)

if __name__ == "__main__":
    print("\nFlight Route Planner: http://127.0.0.1:5000\n")
    app.run(debug=True)
