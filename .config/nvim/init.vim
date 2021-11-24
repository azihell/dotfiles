" Highlights pairs of brackets or bracers
set showmatch
" Highlights all search matches
set hlsearch
" Makes '>' and '<' move the same value defined by tabstop
set shiftwidth=0
" Indentation size (in spaces) of a 'Tab'
set tabstop=2
" Automatizes indentation according to previous line and syntax
set smartindent
" Makes search happens progressively with the typing
set incsearch
" Makes search ignore letter case
set ignorecase
" Show line numbers
set number
" Makes line number dynamic, making it easier to count the size of the jumps
set relativenumber
" Vertical red line at the 80 spacing position to remember about line breaking
set cc=100

" Plugins enabling

" Defines plugins placement after downloading
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.config/nvim/plugged')
" File explorer
Plug 'scrooloose/NERDTree'
" Colors pairs of brackets, parenthesis, etc
Plug 'frazrepo/vim-rainbow'
" Color theme for Neovim
Plug 'arcticicestudio/nord-vim'
" Colors indentation spaces vertically
Plug 'nathanaelkane/vim-indent-guides'
call plug#end()

" Settings for vim-indent-guides
let g:indent_guides_enable_on_vim_startup = 1
set background=dark
let g:indent_guides_guide_size = 2
let g:indent_guides_auto_colors = 0
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  ctermbg=DarkCyan
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven ctermbg=DarkMagenta
autocmd FileType python setlocal shiftwidth=0 tabstop=2

" Settings for vim-rainbow
let g:rainbow_active = 1
