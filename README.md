# My dotfiles

## What is this repo for?
This repo function is twofold:

1) It is a way to help me backup my custom 'dotfiles', by storing them. The dotfiles saved in this repo are listed in the section [Dotfiles](#dotfiles).

2) It keeps the `dotfiles_list` in it. This file is a guide for making `rsync` usage easier. The `dotfiles_list` contains the paths to many *dotfiles*

## Real cool heading

[Go to Real Cool Heading section](#real-cool-heading)


### But what are 'dotfiles'?
Have you seen those settings files that are hidden? Many Linux applications use them!
This file lists dotfiles inside different directories. It's purposeis to gather them all into one directory, so they can be pushed to one GitHub repository.

## How to use the dotfile_list file
This file is a path list for `rsync` to syncronize every file and copy their latest version to the <destination> folder, that is the folder that contains this README.
*Attention*: if the `--dry-run` parameter is used no real syncing will happen, but the expected outcome will be shown. *That's **always** kinda a great idea.*
  
### rsyncing:
  
```console
user@pc $ cd dotfiles
user@pc $ rsync -vr --dry-run --files-from=dotfiles_list $HOME "<destination>"
  # If everything is ok, then:
user@pc $ rsync -vr --files-from=dotfiles_list $HOME "<destination>"
```

## Dotfiles

- [x] .xprofile: startup commands for X11 desktop.
- [x] nitrogen: simple wallpaper manager.
- [x] picom: window composer. Blur, opacity, rounded corners and more for your desktop environment.
  - Restart `picom`: automatic.
- [x] qtile: Python tiling manager settings.
  - Restart `qtile`: Super+Ctrl+R.
- [x] kitty: a terminal emulator.
  - Restart `kitty`: Ctrl+Shift+F5.
