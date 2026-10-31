# SkyRoute — Flight Route Planner (DAA Mini Project)

A simple Flask web application demonstrating **Dijkstra's shortest path algorithm** on the seven-airport directed network from the case study.

## Technology
- Frontend: HTML, CSS, Jinja templates
- Backend: Python + Flask
- Algorithm: Dijkstra using an adjacency-list graph and a min-priority queue (`heapq`)
- Storage: No database required; the sample graph is stored in Python.

## Features
1. Select source and destination airports.
2. Calculate the minimum total flight-time route.
3. Display the route, each flight leg, total time, and settled order.
4. Display all direct connections in the sample network.

## Run on Windows
1. Install Python 3.10 or newer and enable **Add Python to PATH**.
2. Extract this ZIP and open the `flight-route-planner` folder.
3. Double-click `run.bat`.
4. Open **http://127.0.0.1:5000** in your browser.
5. No login, signup, username, password, or database setup is needed.

Keep the terminal window open while using the website. Press `Ctrl + C` to stop the server.

## Run manually
```bash
python -m venv venv
```
Activate the environment (`venv\Scripts\activate` on Windows, or `source venv/bin/activate` on macOS/Linux), then run:
```bash
pip install -r requirements.txt
python app.py
```
Open **http://127.0.0.1:5000**.

## Sample viva test
- From: Delhi (DEL)
- To: Bengaluru (BLR)
- Expected shortest route: **DEL → HYD → BLR**
- Expected total: **2.3 + 1.0 = 3.3 hours**

## Project assumptions
- Airport codes are vertices; listed direct flights are directed, weighted edges.
- Edge weights are non-negative illustrative flight durations in hours.
- Reverse flights are not assumed unless separately listed.
- The result minimises airborne flight time only. Layovers, fares, live schedules, cancellations, and seat availability are not modelled.
- This is an academic demonstration, not a live booking system.

## Project structure
```text
flight-route-planner/
├── app.py
├── requirements.txt
├── run.bat
├── README.md
├── VIVA_GUIDE.md
├── static/styles.css
└── templates/
    ├── base.html
    └── index.html
```
