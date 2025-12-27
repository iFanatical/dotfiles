#!/usr/bin/env bash

xmobar &  # primary
screens=$(xrandr --query | grep " connected" | cut -d" " -f1)
i=1
for screen in $screens; do
    if [ $i -gt 1 ]; then
        xmobar -x $((i-1)) ~/.config/xmobar/xmobarrc &
    fi
    ((i++))
done
