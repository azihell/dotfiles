# My dotfiles

## What is this file?

Merely a list for rsync to follow. A way to help backup my custom 'dotfiles'! But what are 'dotfiles'?
Have you seen those settings files that are hidden? Many Linux applications use them!

This file lists dotfiles inside different directories. It's purpose
is to gather them all into one directory, so they can be pushed to
one GitHub repository.

## How to use this file

This file is a path list for `rsync` to syncronize every file and copy their latest version to
the <destination> folder that will be pushed here.
*ATTENTION*: `--dry-run` is used to simulate what will happen. *That's **always** kinda a great idea.*

### rsyncing:

Go to the folder where the `dotfiles_list` is and

`rsync -vr --dry-run --files-from=dotfiles_list $HOME <destination>`


## AND FINALLY, WHAT MATTERS: WHAT IS BEING PUSHED TO GIT

### .xprofile - startup commands for X11 desktop.
### picom -  window composer. Blur, opacity, rounded corners and more for your desktop environment.
How to restart `picom`: automatic
### qtile - Python tiling manager settings.
How to restart `qtile`: Super+Ctrl+R
### nitrogen - simple wallpaper manager
### kitty - a terminal emulator
How to restart `kitty`: Ctrl+Shift+F5
