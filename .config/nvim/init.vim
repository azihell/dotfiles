set nocompatible
set mouse=v
set showmatch
set hlsearch
set tabstop=2
set softtabstop=2
set shiftwidth=2
set autoindent
set incsearch
set ignorecase
set number
set mouse=a
set cc=80
set relativenumber

call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.config/nvim/plugged')
" File explorer
	Plug 'scrooloose/NERDTree'
	Plug 'frazrepo/vim-rainbow'
	Plug 'arcticicestudio/nord-vim'
call plug#end()
