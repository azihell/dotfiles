# My dotfiles

## What is this repo for?
Merely a list for `rsync` to follow, in the end of the day. A way to help me backup my custom 'dotfiles'!

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

## And finally - what is being pushed!

- .xprofile: startup commands for X11 desktop.
- nitrogen: simple wallpaper manager.
- picom: window composer. Blur, opacity, rounded corners and more for your desktop environment.
  - Restart `picom`: automatic.
- qtile: Python tiling manager settings.
  - Restart `qtile`: Super+Ctrl+R.
- kitty: a terminal emulator.
  - Restart `kitty`: Ctrl+Shift+F5.
