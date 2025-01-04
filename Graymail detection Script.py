import re
import tkinter as tk
from tkinter import messagebox

def check_graymail(headers):
    """
    Checks for graymail indicators in email headers.
    :param headers: A string containing email headers.
    :return: A report indicating the presence of graymail-related tags.
    """
    # Common graymail-related header tags
    graymail_tags = [
        "List-Unsubscribe",
        "Precedence: bulk",
        "Precedence: list",
        "List-Id",
        "X-Mailer",
        "X-Campaign",
        "X-Mailgun-Tag",
        "X-Newsletter",
        "X-Mailing-List",
    ]

    # Report for matching graymail tags
    report = []
    for tag in graymail_tags:
        if re.search(tag, headers, re.IGNORECASE):
            report.append(f"Graymail Indicator Found: {tag}")

    if report:
        return "\n".join(report)
    else:
        return "No graymail indicators found in the headers."

def analyze_headers():
    """
    Callback function to analyze headers entered in the text box.
    """
    headers = header_input.get("1.0", tk.END).strip()
    if not headers:
        messagebox.showerror("Error", "Please enter email headers.")
        return

    # Check for graymail indicators
    result = check_graymail(headers)

    # Print results in the terminal
    print("\n--- Graymail Analysis ---")
    print(result)

    # Notify the user
    messagebox.showinfo("Analysis Complete", "Results printed in the terminal.")

# Create the GUI window
root = tk.Tk()
root.title("Graymail Header Analyzer")

# Instruction Label
instruction = tk.Label(root, text="Enter email headers below:")
instruction.pack(pady=5)

# Text box for input
header_input = tk.Text(root, width=80, height=20)
header_input.pack(pady=5)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Headers", command=analyze_headers)
analyze_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()