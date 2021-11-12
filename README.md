# My *dotfiles*

## What is this repo for?
This repo function is twofold:

1) It is a way to help me backup my custom *dotfiles*, by storing them. They are listed in the section [Dotfiles](#dotfiles).

2) It keeps the `dotfiles_list` in it. This file is a guide for making `rsync` usage easier. The `dotfiles_list` contains the paths to many *dotfiles*

## Real cool heading

[Go to Real Cool Heading section](#real-cool-heading)


### But what are *dotfiles*?
Many Linux applications store their settings into hidden files. This repo gathers a lot of them into one place,for easy management. This is more easily done using `rsync`, as explained below.

## How to use `rsync` and the `dotfile_list`
`rsync` reads the `dotfile_list` file in order to syncronize the *dotfiles* listed in it and copy their latest version to the *<destination>* folder, which is the folder containing this README.
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
