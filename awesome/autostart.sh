#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop
#run xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#run xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
#autorandr horizontal
run nm-applet
#run caffeine
run pamac-tray
run xfce4-power-manager
run blueberry-tray
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
run numlockx on
run nitrogen --restore
run setxkbmap -model pc105 -layout "us,ru" -variant ",winkeys" -option "grp:alt_shift_toggle"
run picom --config ~/.config/awesome/picom.conf
run /usr/lib/xfce4/notifyd/xfce4-notifyd
run sxhkd -c ~/.config/sxhkd/sxhkdrc
run xfce4-panel
