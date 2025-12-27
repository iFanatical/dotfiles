import os
import subprocess
import colors
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
browser = "brave --ozone-platform=x11"
browser2 = "firefox"
myTerm = "kitty"

colors = colors.Tokyonight

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle floating
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    # qtile management
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "n", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),

    # Restart/quit qtile
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "BackSpace", lazy.shutdown()),

    # Programs
    Key([mod], "return", lazy.spawn(myTerm)),
    Key([mod, "shift"], "w", lazy.spawn("sh -c $SCRIPTS/fanos-set-wallpaper-feh")),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod, "shift"], "b", lazy.spawn("firefox")),
    Key([mod], "d", lazy.spawn("sh -c $HOME/.config/rofi/launchers/type-1/launcher.sh")),

    # Multimedia
    Key([], "XF86AudioPlay", lazy.spawn("sh -c $SCRIPTS/control-player.sh play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl preivous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("sh -c $SCRIPTS/volumeinc.sh")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("sh -c $SCRIPTS/volumedec.sh")),
    Key([], "XF86AudioMute", lazy.spawn("sh -c $SCRIPTS/volumetoggle.sh")),
]

groups = [Group(i) for i in "1234567890"]

s = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for index, i in enumerate(groups):
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(s[index]),
                lazy.to_screen(s[index]),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 2,
                "border_focus": colors[7],
                "border_normal": colors[0]
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(
    font="JetBrainsMonoNL Nerd Font Propo Bold",
    fontsize=12,
    padding = 0,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.Spacer(length = 4),
        widget.TextBox(
                 foreground = colors[6],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("fanos-menu")},
	             text = '󰌧',
                 ),
        widget.Spacer(length = 4),
        widget.Prompt(
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 fontsize=14,
                 foreground = colors[1]
        ),
        widget.GroupBox(
                 fontsize = 14,
                 margin_y = 5,
                 margin_x = 2,
                 padding_y = 0,
                 padding_x = 2,
                 borderwidth = 3,
                 active = colors[8],
                 inactive = colors[15],
                 rounded = False,
                 highlight_color = colors[2],
                 highlight_method = "line",
                 this_screen_border = colors [0],
                 this_current_screen_border = colors[7],
                 other_screen_border = colors[0],
                 other_current_screen_border = colors[7],
                 ),
        widget.TextBox(
                 text = '│',
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.CurrentLayout(
                 foreground = colors[1],
                 padding = 5
                 ),
        widget.TextBox(
                 text = '│',
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.WindowName(
                 fontsize = 12,
                 foreground = colors[17],
                 background = colors[2],
                 padding = 8,
                 max_chars = 40
                 ),
        widget.GenPollCommand(
                 update_interval = 300,
                 cmd = "kernel.sh",
                 shell = True,
                 foreground = colors[7],
                 padding = 4,
                 ),
        widget.TextBox(
                 text = '│',
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.GenPollCommand(
                 update_interval = 300,
                 cmd = "mem-usage.sh",
                 shell = True,
                 foreground = colors[13],
                 padding = 4,
                 ),
        widget.TextBox(
                 text = '│',
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.Volume(
                 foreground = colors[6],
                 padding = 4, 
                 fmt = ' {}',
                 step = 5,
                 ),
        widget.TextBox(
                 text = '│',
                 font = "JetBrainsMonoNL Nerd Font Propo Bold",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.Clock(
                 foreground = colors[8],
                 padding = 4, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-date.sh')},
                 format = "󰸗 %I:%M:%S %p",
                 ),
        widget.Systray(padding = 4),
        widget.Spacer(length = 8),

        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    widgets_screen1.pop(16)
    return widgets_screen1 

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin=[0, 0, 0, 0], size=24)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), margin=[0, 0, 0, 0], size=24))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

auto_fullscreen = True
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

wmname = "LG3D"
