#!/bin/bash

# Define the range of workspaces to show
WORKSPACES=(6 7 8 9 10)

# Get active workspace info
ACTIVE_JSON=$(hyprctl workspaces -j)

# Loop through the list and build output
OUTPUT=""
for ID in "${WORKSPACES[@]}"; do
    # Check if the workspace exists
    MATCH=$(echo "$ACTIVE_JSON" | jq --argjson id "$ID" '.[] | select(.id == $id)')
    
    if [[ -n "$MATCH" ]]; then
        FOCUSED=$(echo "$MATCH" | jq '.focused')
        if [[ "$FOCUSED" == "true" ]]; then
            OUTPUT+="<span color=\"#88c0d0\">[$ID]</span> "
        else
            OUTPUT+="<span color=\"#aaaaaa\">$ID</span> "
        fi
    else
        OUTPUT+="<span color=\"#444444\">$ID</span> "
    fi
done

echo "$OUTPUT"
