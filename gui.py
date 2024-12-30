import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SignalVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Signal Visualizer')
        self.root.geometry('800x500')
        self.root.configure(bg='black')

        # Default values
        self.frequency = 1
        self.amplitude = 1
        self.phase = 0

        # Time array
        self.t = np.linspace(0, 1, 500)
        self.update_signal()

        # Matplotlib figure
        self.fig = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(self.t, self.y)  # Correctly unpack the line object
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Signal Visualizer')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side='left', fill='both', expand=1)

        # Controls
        self.controls_frame = tk.Frame(self.root, bg='black')
        self.controls_frame.pack(side='right', fill='y', padx=10, pady=10)

        # Amplitude
        tk.Label(self.controls_frame, text="Amplitude", bg="black", fg="white").pack(pady=5)
        self.amplitude_entry = tk.Entry(self.controls_frame)
        self.amplitude_entry.insert(0, str(self.amplitude))
        self.amplitude_entry.pack(pady=5)

        # Frequency
        tk.Label(self.controls_frame, text="Frequency", bg="black", fg="white").pack(pady=5)
        self.frequency_entry = tk.Entry(self.controls_frame)
        self.frequency_entry.insert(0, str(self.frequency))
        self.frequency_entry.pack(pady=5)

        # Phase
        tk.Label(self.controls_frame, text="Phase", bg="black", fg="white").pack(pady=5)
        self.phase_entry = tk.Entry(self.controls_frame)
        self.phase_entry.insert(0, str(self.phase))
        self.phase_entry.pack(pady=5)

        # Update Button
        self.update_button = tk.Button(self.controls_frame, text="Update Plot", command=self.update_plot)
        self.update_button.pack(pady=20)

        self.root.mainloop()

    def update_signal(self):
        """Updates the signal data based on amplitude, frequency, and phase."""
        self.y = self.amplitude * np.sin(2 * np.pi * self.frequency * self.t + self.phase)

    def update_plot(self):
        """Updates the plot when the button is clicked."""
        try:
            # Get values from entries
            self.amplitude = float(self.amplitude_entry.get())
            self.frequency = float(self.frequency_entry.get())
            self.phase = float(self.phase_entry.get())

            # Update signal
            self.update_signal()

            # Update plot
            self.line.set_ydata(self.y)  # Update the y-data of the line
            self.ax.relim()  # Recompute limits
            self.ax.autoscale_view()  # Autoscale the view
            self.canvas.draw()  # Redraw the canvas
        except ValueError:
            print("Please enter valid numeric values for amplitude, frequency, and phase.")


if __name__ == '__main__':
    app = SignalVisualizer()
