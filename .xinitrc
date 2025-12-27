#!/usr/bin/env bash

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi
if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi
if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi
if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

xrandr --output DisplayPort-0 --mode 1920x1080 --rate 100.00 --output DisplayPort-1 --mode 1920x1080 --rate 100.00 --primary
dunst -conf $HOME/.config/dunst/dunstrc-xorg &
$HOME/source-files/fehbg.sh
numlockx &
picom &
$HOME/.custom-exes/color-demo-app/cmdemo_script DisplayPort-1 1.2 &
$HOME/.custom-exes/color-demo-app/cmdemo_script DisplayPort-0 1.2 &
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &
gsettings set org.gnome.desktop.interface gtk-theme fan-custom-tokyonight &
gsettings set org.gnome.desktop.interface icon-theme Tela-circle-nord &
gsettings set org.gnome.desktop.interface cursor-theme breeze-dark &
gsettings set org.gnome.desktop.interface font-name "Ubuntu Mono 10" &
gsettings set org.gnome.desktop.interface cursor-size 24 &
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark' &
solaar --window hide &
dinitctl -u restart gpu-screen-recorder
dinitctl -u restart gpu-screen-recorder-ui
setxkbmap -option caps:none
xset r rate 200 35
xset s off -dpms
xset dpms 0 0 0
xset s noblank
xset s off
xsetroot -cursor_name left_ptr

oxwm-startup.sh;
