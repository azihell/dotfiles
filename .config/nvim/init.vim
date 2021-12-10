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
" Set character encoding to UTF-8
set encoding=utf-8
" When scrolling (up or down), the cursor can have a distance from the limit
" of the screen and the scrolling action will still take place
set scrolloff=5
" Enables 24-bit RGB color on the terminal UI
set termguicolors

""""""""""""""""""""
" Plugins enabling "
""""""""""""""""""""

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
" Color visualization
Plug 'chrisbra/Colorizer'
" deoplete completion plugin
" It is a requirement for the jedi-vim Python autocompletion plugin!
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
" Python autocompletion
Plug 'davidhalter/jedi-vim'
" Advanced status bar
Plug 'vim-airline/vim-airline'
" Neon theme
Plug 'rafamadriz/neon'
" Awesome Vim color schemes
Plug 'rafi/awesome-vim-colorschemes'

call plug#end()

" Settings for vim-indent-guides
let g:indent_guides_enable_on_vim_startup = 1
set background=dark
let g:indent_guides_guide_size = 2
let g:indent_guides_auto_colors = 0
let g:colorizer_auto_color = 1
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  ctermbg=026
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven ctermbg=DarkMagenta
autocmd FileType python setlocal shiftwidth=0 tabstop=2

" Settings for vim-rainbow
let g:rainbow_active = 1

" Settings for deoplete
let g:deoplete#enable_at_startup = 1

" Settings for Vim theme
colorscheme nord
let g:airline_theme = 'nord'
let g:nord_cursor_line_number_background = 1
let g:nord_italic_comments = 1
