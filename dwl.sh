#!/usr/bin/env bash
export XDG_CURRENT_DESKTOP=wlroots
slstatus -s | dbus-launch dwl -s "sh -c '$SCRIPTS/autostart.sh'"
