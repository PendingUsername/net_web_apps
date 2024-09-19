# Ping Tool with Python and Data Visualization

## Overview

This project is a simple Python-based tool that allows users to ping a specific host and visualize the results in their web browser. It uses the `Bottle` web framework to serve the web interface and `Tkinter` for a simple GUI. The ping results are displayed as both raw output and a bar chart generated using `matplotlib` to visualize response times.

## Features

- **Ping Hosts**: Enter a host address (e.g., `x.com`) and get ping statistics.
- **Data Visualization**: Ping response times are displayed as a bar chart using Python’s `matplotlib`.
- **Simple GUI**: A graphical user interface built with `Tkinter` allows users to input a host address.
- **Web Interface**: The ping results, including a visualization, are displayed in a browser via the Bottle web server.

## Technologies Used

- **Python**: The core programming language used.
- **Bottle**: A lightweight WSGI micro web framework for Python.
- **Matplotlib**: Used for creating bar charts to visualize ping times.
- **Tkinter**: Provides the graphical user interface (GUI) for the tool.
- **Subprocess**: Executes the ping command and retrieves the output.

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```bash
    pip install bottle matplotlib
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. The Tkinter GUI will launch. Enter a host address and click "Ping Host" to open your browser and view the results.

## Usage

1. Launch the application, and a GUI window will appear.
2. Enter the host (e.g., `google.com` or `x.com`) into the text box and click the "Ping Host" button.
3. Your default web browser will open and display the ping results, including:
   - Ping statistics for the entered host.
   - A bar chart visualizing the response times for each ping attempt.

## MIT License

Copyright (c) 2024 PendingUsernam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

