if [ -f "$HOME/.common_env" ]; then
  source "$HOME/.common_env"
fi

# start WM on login of TTY1
if [[ -z $DISPLAY ]] && [[ $(tty) == /dev/tty1 ]]; then
    # start wm
    #$HOME/dwl.sh
    #$HOME/hyprland.sh
    startx &
fi
