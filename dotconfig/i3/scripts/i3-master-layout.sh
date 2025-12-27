#!/bin/bash
# Apply a master layout: one master window on the left, stack on the right

# Get the current workspace
workspace=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name')

# Set the master window (focused window)
i3-msg "focus; split h; resize set 55 ppt"

# Move subsequent windows to the right stack
i3-msg "layout stacking"

# Ensure new windows go to the stack
i3-msg "focus parent; focus right"
