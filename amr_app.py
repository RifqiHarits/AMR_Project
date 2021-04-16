import amr_elements
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

topFrame = tk.Frame(root, bg="grey")
topFrame.pack(side="top")

bottomFrame = tk.Frame(root, bg="grey")
bottomFrame.pack(side="bottom")

amrLabel = tk.Label(topFrame, text="AMR ID:")
amrLabel.pack(side="left")
amrID = tk.Entry(topFrame)
amrID.pack(side="left")

goalWaypointLabel = tk.Label(bottomFrame, text="Waypoint ID:")
goalWaypointLabel.pack(side="left")

goalWaypointID = tk.Entry(bottomFrame)
goalWaypointID.pack(side="left")


def send_goal():
    amr_id = amrID.get()
    waypoint_id = goalWaypointID.get()
    graph_id = ""
    amr_elements.AMRServerElement.send_goal(amr_id, graph_id, waypoint_id)


sendGoal = tk.Button(bottomFrame, text="Send Goal", bg="#263D42")
sendGoal.pack(side="left")

root.mainloop()
