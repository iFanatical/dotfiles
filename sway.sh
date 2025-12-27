#!/bin/bash

# Toolkit Backend Variables
export GDK_BACKEND=wayland;x11
export QT_QPA_PLATFORM=wayland;xcb
export CLUTTER_BACKEND=wayland

# xdg Specifications
export XDG_CURRENT_DESKTOP=sway
export XDG_SESSION_DESKTOP=sway
export XDG_SESSION_TYPE=wayland
export XDG_DESKTOP_PORTAL_BACKEND=wlr

# QT Variables
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
export QT_QPA_PLATFORMTHEME=qt5ct
export QT_QPA_PLATFORMTHEME=qt6ct

# Define the executable you want to check
EXECUTABLE="sway"

# Get the process name from the executable path
PROCESS_NAME=$(basename "$EXECUTABLE")

# Check if the process is already running
if ! pgrep -x "$PROCESS_NAME" > /dev/null; then
    echo "Starting $PROCESS_NAME..."
    "$EXECUTABLE" &
else
    echo "$PROCESS_NAME is already running."
fi

