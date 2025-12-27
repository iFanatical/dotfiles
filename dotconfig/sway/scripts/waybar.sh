#!/bin/bash

killall waybar
waybar --config $HOME/.config/sway/apps/waybar/config --style $HOME/.config/sway/apps/waybar/style.css
waybar --config $HOME/.config/sway/apps/waybar/config-dp1 --style $HOME/.config/sway/apps/waybar/style.css