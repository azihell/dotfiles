#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '


# My aliases

alias Bashed='nvim ~/.bashrc'
alias Bash='. ~/.bashrc'
alias e='exa -lha'
alias cd2='cd ../..'
alias cd3='cd ../../..'
alias cd4='cd ../../../..'

alias qed='nvim ~/.config/qtile/config.py'

# Exports

export EDITOR=nvim
