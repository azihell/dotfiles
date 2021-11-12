###################
# My QTile ricing #
###################

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

##############
# MY IMPORTS #
##############

#############
# MY COLORS #
#############

# Neon colors
neon = [["#fe3218", "#fe3218"],   # [0] Crimson red
	 ["#ff911a", "#ff911a"],  # [1] Orange
	 ["#e100f5", "#e100f5"],  # [2] Magenta
	 ["#450eff", "#450eff"],  # [3] Blue
	 ["#21006f", "#21006f"],  # [4] Darkest blue
	 ["#78fdfa", "#78fdfa"],  # [5] Cyan
       ]


############
# MY FONTS #
############

# Inconsolata: https://fonts.google.com/specimen/Inconsolata
# LoRes: https://fonts.adobe.com/fonts/lo-res


###################
# MOUSE CALLBACKS #
###################


# "Super key" DEFINITION 
mod = "mod4"

# Preferred terminal
terminal = "kitty"

#######################
# HOTKEYS DEFINITIONS #
#######################

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 1dB+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 1dB-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -e set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -e set 5%-")),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 50%"))
]

#####################
# GROUP DEFINITIONS #
#####################

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

#####################
# LAYOUT DEFINTIONS #
#####################

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4, margin=5),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(margin=10, border_focus=neon[5], border_normal=neon[3], single_border_width=0, single_margin=0),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

###################
# WIDGET DEFAULTS #
###################

widget_defaults = dict(
    font='LoRes 9 OT',
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

###########
# SCREENS #
###########

screens = [
    Screen(
        top=bar.Bar(
            [	widget.CurrentLayout(background=neon[4], padding=6),
                widget.GroupBox(background=neon[2], rounded=True),
             	widget.Sep(padding=6, foreground=neon[4], background=neon[4], linewidth=0),
                widget.Prompt(background=neon[3], padding=6),
             	widget.Sep(padding=6, foreground=neon[4], background=neon[4], linewidth=0),
                widget.WindowName(background=neon[4]),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
		widget.WidgetBox(background=neon[4], widgets=[
	                widget.TextBox("hellion", name="neon_default", foreground=neon[0], background=neon[4]),
			widget.Net(interface=["enp7s0f1", "wlan0"], background=neon[4])
			]
		),
                widget.Systray(),
                widget.Clock(format='%a %d-%b %H:%M', background=neon[4]),
             	widget.Sep(padding=10, foreground=neon[4], background=neon[4], linewidth=0),
		widget.BatteryIcon(background=neon[4]),
		widget.Volume(background=neon[4], volume_app="pavucontrol"),
             	widget.Sep(padding=10, foreground=neon[4], background=neon[4], linewidth=0),
                widget.QuickExit(background=neon[1]),
            ],
            24,
        ),
	
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile!"
