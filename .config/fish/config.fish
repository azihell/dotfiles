if status is-interactive
    # Commands to run in interactive sessions can go here

##############
# My aliases #
##############

alias fished='nvim ~/.config/fish/config.fish'
alias Fish='. ~/.config/fish/config.fish'
alias e='exa -lha'
alias cd2='cd ../..'
alias cd3='cd ../../..'
alias cd4='cd ../../../..'

alias qed='nvim ~/.config/qtile/config.py'
alias qlog='tail -f ~/.local/share/qtile/qtile.log'

function ranger --wraps ranger --description "Test"
	set -e LINES
	set -e COLUMNS
	command ranger
end

###################
# History control #
###################

export HISTCONTROL=ignoreboth:erasedups

###########
# Exports #
###########

export EDITOR=nvim

# Small pathsize

set -g fish_prompt_pwd_dir_length 40

end
