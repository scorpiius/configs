#### V's Qtile config ####


from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "Left", lazy.layout.decrease_ratio(), desc="Grow master width"),
    Key([mod], "Right", lazy.layout.increase_ratio(), desc="Shrink master width"),
    Key([mod, "shift"], "Left", lazy.layout.increase_nmaster(), desc="Increase number of master windows"),
    Key([mod, "shift"], "Right", lazy.layout.decrease_nmaster(), desc="Decrease number of master windows"),
    Key([mod], "Down", lazy.group.next_window(), desc="Move focus to next window"),
    Key([mod], "Up", lazy.group.prev_window(), desc="Move focus to previous window"),
    Key([mod], "space", lazy.window.toggle_floating(), desc="Put the focused window to/from floating mode"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen mode"),
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Put the focused window to/from minimize mode"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
]

groups = [
    Group("1", matches=[Match(wm_class=["Google-chrome", "Yandex-browser"])]),
    Group("2"),
    Group("3", matches=[Match(wm_instance_class=["Steam"])]),
    Group("4", matches=[Match(wm_class=["TelegramDesktop"])]),
    Group("5", matches=[Match(wm_class=["yandex-music-player"])]),
    Group("6"),
]

KP = {
    '1': 'End',
    '2': 'Down',
    '3': 'Next',
    '4': 'Left',
    '5': 'Begin',
    '6': 'Right',
    '7': 'Home',
    '8': 'Up',
    '9': 'Prior',
    '0': 'Insert',
}

for i in groups:

    group_name = i.name
    group_letter = i.name[0]

    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

    if not group_letter in KP.keys():
        continue

    keys.extend([

        Key([mod], "KP_" + KP[group_letter],
            lazy.group[group_name].toscreen(),
        ),

        Key([mod, "shift"], 'KP_' + KP[group_letter],
            lazy.window.togroup(group_name, switch_group=False),
        ),

    ])

def init_layout_theme():
    return{"border_width":2,
           "border_focus": "#b78ff2",
           "border_normal": "#666666"
           }

layout_theme = init_layout_theme()

layouts = [
     layout.Tile(
         **layout_theme,
         margin=8,
         ratio=0.52,
         ratio_increment=0.02,
         master_match=[Match(wm_class=["Google-chrome", "Yandex-browser"])],
         shift_windows=True,
         border_on_single=False,
         margin_on_single=False
     ),
]

screens = [
    Screen(
        top=bar.Gap(29),
    )
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(**layout_theme,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
bring_front_click = "floating_only"
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"
