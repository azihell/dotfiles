#!/bin/fish

echo "Running rsync in dry-run mode"
rsync -vr --dry-run --files-from=dotfiles_list $HOME (pwd)
