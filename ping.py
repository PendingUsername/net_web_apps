from bottle import run, route, static_file
import subprocess
import tkinter as tk
import webbrowser
from threading import Thread
import matplotlib.pyplot as plt
import io
import base64

# ----------- Bottle Web Server Code ----------- #

# Route for the home page
@route('/')
def index():
    page = """<html>
              <head>
                <title>Ping Tool</title>
                <style>
                  body { font-family: Arial, sans-serif; text-align: center; margin: 40px; }
                  h1 { color: #4CAF50; }
                  h2 { color: #555; }
                  p { font-size: 18px; }
                  .container { max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
                </style>
              </head>
              <body>
                <div class="container">
                  <h1>Ping!</h1>
                  <h2>Add host to the URL to begin ping.</h2>
                  <p>Example: <a href="http://127.0.0.1:8080/x.com">http://127.0.0.1:8080/x.com</a></p>
                </div>
              </body>
              </html>
           """
    return page

# Function to generate and return a matplotlib chart as a base64 encoded image
def create_ping_chart(response_times):
    # Create a figure and a bar chart
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3, 4], response_times, color='#4CAF50')
    ax.set_xlabel('Ping Attempt')
    ax.set_ylabel('Response Time (ms)')
    ax.set_title('Ping Response Times')

    # Save the figure to a BytesIO object and encode as base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_base64 = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close(fig)  # Close the figure to free memory
    return chart_base64

# Handle ping requests for both with and without trailing slash
@route('/<host>')
@route('/<host>/')
def ping_host(host):
    try:
        # Use subprocess to capture the output of the ping command
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            # Extract the response times from the ping results
            response_times = [float(line.split("time=")[1].split(" ")[0]) 
                              for line in result.stdout.splitlines() if "time=" in line]
            result_message = f"<h3>{host} is reachable.</h3><pre>{result.stdout}</pre>"
        else:
            response_times = []
            result_message = f"<h3>{host} is not reachable.</h3><pre>{result.stderr}</pre>"

    except Exception as e:
        # In case of any unexpected errors
        result_message = f"<h3>Error pinging {host}.</h3><pre>{str(e)}</pre>"
        response_times = []

    # If we have response times, create a chart and embed it as a base64 image
    if response_times:
        chart_image = create_ping_chart(response_times)
        chart_html = f'<img src="data:image/png;base64,{chart_image}" alt="Ping Chart" />'
    else:
        chart_html = ""

    # Create the final HTML page with styled ping results and chart
    page = f"""<html>
               <head>
                 <title>Ping Results</title>
                 <style>
                   body {{ font-family: Arial, sans-serif; text-align: center; margin: 40px; }}
                   h1 {{ color: #4CAF50; }}
                   pre {{ text-align: left; max-width: 600px; margin: auto; white-space: pre-wrap; word-wrap: break-word; }}
                   .container {{ max-width: 700px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }}
                   img {{ margin-top: 20px; max-width: 600px; }}
                   button {{ background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px; }}
                   button:hover {{ background-color: #45a049; }}
                 </style>
               </head>
               <body>
                 <div class="container">
                   <h1>Ping Results for {host}</h1>
                   {result_message}
                   {chart_html}
                   <button onclick="location.reload()">Refresh</button>
                 </div>
               </body>
               </html>
            """
    return page

# ----------- Tkinter GUI Code ----------- #

def open_webpage():
    # Get the host entered in the input field
    host = entry.get().strip()
    if host:
        # Format the URL and open it in the web browser
        url = f"http://127.0.0.1:8080/{host}"
        webbrowser.open(url)

def start_gui():
    # Create the main tkinter window
    root = tk.Tk()
    root.title("Ping Web Address")

    # Create a label widget
    label = tk.Label(root, text="Enter Host Address (e.g., x.com):")
    label.pack(pady=10)

    # Create an entry widget for user input
    global entry
    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)

    # Create a button that opens the webpage
    button = tk.Button(root, text="Ping Host", command=open_webpage)
    button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()

# ----------- Main Function to Run Both GUI and Web Server ----------- #

def start_server():
    # Start the Bottle web server
    run(host='127.0.0.1', port=8080)

# Run both the GUI and the web server concurrently
if __name__ == "__main__":
    # Run the Bottle web server in a separate thread
    server_thread = Thread(target=start_server)
    server_thread.daemon = True  # This ensures the thread will exit when the main program exits
    server_thread.start()

    # Start the GUI
    start_gui()



