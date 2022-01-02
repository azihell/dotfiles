###################
# My QTile ricing #
###################

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile import qtile
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

##############
# MY IMPORTS #
##############

# 'logger' is a logging object that enables writing on the standard Qtile log file
# It's located at ~/.local/share/qtile/qtile.log
# Suggestion: use "tail -f ~/.local/share/qtile/qtile.log" to watch the log file in real time
import subprocess
from libqtile.log_utils import logger
from libqtile import hook
from libqtile.widget import base

# Sets the minimum logger level. See https://docs.python.org/3/library/logging.html#levels
logger.setLevel(20)

# from Xlib import X, display
# from Xlib.ext import randr
# from pprint import pprint
# 
# d = display.Display()
# s = d.screen()
# r = s.root
# res = r.xrandr_get_screen_resources()._data
# 
# num_screens = 0
# for output in res['outputs']:
#   print("Output %d:" % (output))
#   mon = d.xrandr_get_output_info(output, res['config_timestamp'])._data
#   print("%s: %d" % (mon['name'], mon['num_preferred']))
#   if mon['num_preferred']:
#     num_screens += 1
# 
# print("%d screens found!" % (num_screens))

##############
# MY METHODS #
##############

# @hook.subscribe.focus_change
def mylogger():
  logger.warning("Group changed!")

def get_bluetooth_mac():
  device = subprocess.Popen(["bluetoothctl", "devices"], stdout=subprocess.PIPE,
      stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  device.wait()
  output, errors = device.communicate()
  device = output.split(" ")
  mac = device[1]
  mac_with_underscores = mac.replace(":", "_")
  logger.info("Bluetooth widget connected device: '%s'", mac_with_underscores)
  return("/dev_"+mac_with_underscores)

##############
# MY WIDGETS #
##############

#############
# MY COLORS #
#############

tc = {"btred": "#fe3218", "orange": "#ff911a", "magenta": "e100f5",
  "btblue": "#450eff", "dkblue": "#21006f", "cyan": "#66d9ff",
  "black": "#000000", "white": "#ffffff", "green": "#00ff00"}

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

    # ATT: Must install pulseaudio-ctl (can be found in AUR) in order to control the volume!
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +1dB"),
      desc="Raise the volume using PulseAudio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -1dB"),
      desc="Lower the volume using PulseAudio"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -e set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -e set 5%-")),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 50%")),
]
#################################
# GROUP DEFINITIONS AND HOTKEYS #
#################################

group_info = [
    ['1', 'Web'],
    ['2', 'Nav'],
    ['3', 'Cmd'],
    ['4', 'Dbg'],
    ['5', '1'],
    ['6', '2'],
    ]

groups = [Group(name=i[0], label=i[1]) for i in group_info]

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

    Key([mod], "d", lazy.group['4'].toscreen(toggle=False),
                    lazy.restart()),
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
    layout.MonadTall(margin=10, border_focus=tc["cyan"], border_normal= tc["btblue"]
      , single_border_width=0, single_margin=0),
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
      [ widget.Sep(padding=10, linewidth=0),
#        Group selections using block mode:
#        widget.GroupBox(active=tc["btblue"], inactive=tc["white"], rounded=True,
#          fontshadow=tc["black"], fontsize=18, padding=0, font='LoRes 12 OT',
#          visible_groups=['1', '2', '3'], highlight_method='block',
#          block_highlight_text_color="#66d9ff"),
#        widget.GroupBox(active=tc["green"], inactive=tc["btred"], rounded=True,
#          fontshadow=tc["black"], fontsize=18, padding=0, font='LoRes 12 OT', borderwidth=9,
#          visible_groups=['4'], highlight_method='block', block_highlight_text_color="#00ff00"),
        widget.GroupBox(active=tc["orange"], inactive=tc["white"], rounded=True,
          fontshadow=tc["black"], fontsize=18, padding=0, font='LoRes 12 OT',
          visible_groups=['1', '2', '3'], highlight_method='line',
          highlight_color=['66d9ff','21006f']),
        widget.GroupBox(active=tc["green"], inactive=tc["btred"], rounded=True,
          fontshadow=tc["black"], fontsize=18, padding=0, font='LoRes 12 OT',
          visible_groups=['4'], highlight_method='line',
          highlight_color=['66d9ff','21006f']),
        widget.Sep(padding=6, linewidth=0),
        widget.Prompt(padding=6, fontshadow=tc["black"]),
        widget.Sep(padding=6, linewidth=0),
        widget.WindowName(fontshadow=tc["black"], font='LoRes 15 OT Bold', fontsize=18),
        # widget.Chord(
        #   chords_colors={
        #     'launch': ("#ff0000", "#ffffff"),
        #     },
        #   name_transform=lambda name: name.upper(),
        #   ),
        # widget.WidgetBox(widgets=[
        #   widget.TextBox("hellion", name="neon_default"),
        #   widget.Net(interface=["enp7s0f1"], foreground=tc["black"]),
        #   widget.Memory(foreground=tc["black"]),
        #   ], foreground=tc["black"]),
        widget.Image(scale=True, filename="~/.config/qtile/icons/bluetooth.png", padding=10),
        widget.Bluetooth(fontshadow=tc['black'], hci=get_bluetooth_mac()),
        widget.Sep(padding=6, linewidth=0),
        widget.CheckUpdates(fontshadow=tc["black"], padding=10,
          update_interval=10),
        widget.Sep(padding=6, linewidth=0),
        widget.Image(scale=True, filename="~/.config/qtile/icons/cpu.png", padding=10),
        widget.CPU(format='{freq_current} GHz {load_percent}%',
          fontshadow=tc["black"], ),
        widget.Sep(padding=6, linewidth=0),
        widget.Image(scale=True, filename="~/.config/qtile/icons/memory.png", padding=10),
        widget.Memory(format='{MemPercent: .2f}''%', fontshadow=tc['black']),
        widget.Sep(padding=6, linewidth=0),
        widget.Image(scale=True, filename="~/.config/qtile/icons/calendar.png", padding=10),
        widget.Clock(fontshadow=tc["black"], format='%a %d-%b %H:%M'),
        widget.Sep(padding=10, linewidth=0),
        widget.Image(scale=True, filename="~/.config/qtile/icons/volume.png", padding=0),
        widget.PulseVolume(fontshadow=tc["black"], volume_app="pavucontrol", padding=10,
          get_volume_command="pactl get-sink-volume $(pactl get-default-sink) | grep % | cut -d " " -f 6",
          limit_max_volume=True),
#          volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -2dB",
#          volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +2dB"),
        widget.BatteryIcon(theme_path='/home/azihell/.config/qtile/icons/mybatt',
          padding=10, update_interval=1),
        widget.Battery(fontshadow=tc["black"], format='{percent:2.0%} {hour:d}:{min:02d}',
          padding=0),
        widget.Sep(padding=10, linewidth=0) 
      ],
      24,
      background=[tc["magenta"],tc["cyan"]]
    ),
  ),
  Screen(
    top=bar.Bar(
      [ widget.GroupBox(active=tc["green"], inactive=tc["btred"], rounded=True,
          fontshadow=tc["black"], fontsize=18, padding=0, font='LoRes 12 OT',
          visible_groups=['5', '6'], highlight_method='line',
          highlight_color=['66d9ff','21006f'])
      ],
      24,
      background=[tc["magenta"],tc["cyan"]]
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
