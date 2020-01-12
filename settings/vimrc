call plug#begin('~/.vim/plugged')
Plug 'junegunn/vim-easy-align'
Plug 'https://github.com/junegunn/vim-github-dashboard.git'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }
Plug 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim' }
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug '~/my-prototype-plugin'
Plug 'https://github.com/bling/vim-airline'
Plug 'kien/rainbow_parentheses.vim'
let g:rbpt_colorpairs = [
                        \ ['brown',       'RoyalBlue3'],
                        \ ['Darkblue',    'SeaGreen3'],
                        \ ['darkgray',    'DarkOrchid3'],
                        \ ['darkgreen',   'firebrick3'],
                        \ ['darkcyan',    'RoyalBlue3'],
                        \ ['darkred',     'SeaGreen3'],
                        \ ['darkmagenta', 'DarkOrchid3'],
                        \ ['brown',       'firebrick3'],
                        \ ['gray',        'RoyalBlue3'],
                        \ ['darkmagenta', 'DarkOrchid3'],
                        \ ['Darkblue',    'firebrick3'],
                        \ ['darkgreen',   'RoyalBlue3'],
                        \ ['darkcyan',    'SeaGreen3'],
                        \ ['darkred',     'DarkOrchid3'],
                        \ ['red',         'firebrick3'],
                        \ ]
let g:rbpt_max = 16
let g:rbpt_loadcmd_toggle = 0
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces
Plug 'scrooloose/syntastic'
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
call plug#end()

"启动的时候不显示那个援助索马里儿童的提示 
set shortmess=atI 
"设置编码
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
filetype plugin indent on "使用智能补全
filetype indent on  "针对不同的文件采用不同的缩进方式
filetype plugin on  "允许插件
set smartindent
"显示行号
set nu
"突出当前行
set cursorline
"显示空格和tab键
set listchars=tab:▶-,trail:-
"启用鼠标
set mouse=a
set selection=exclusive
set selectmode=mouse,key
"括号匹配
set showmatch
"设置缩进
set tabstop=4
set shiftwidth=4
set autoindent
"总是显示状态栏
set laststatus=2
"状态栏内容
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}  
"显示光标当前位置
set ruler
" 智能补全
set completeopt=longest,menu
" 语法高亮 
syntax enable
syntax on 
" 不要生成swap文件，当buffer被丢弃的时候隐藏它 
setlocal noswapfile 
set bufhidden=hide 
" 在搜索的时候忽略大小写 
set ignorecase 
" 在搜索时，输入的词句的逐字符高亮（类似firefox的搜索） 
set incsearch
" 在输入未完毕时开始搜索
set is
" 不要换行 
set nowrap
" 历史记录
set history=1024
" 文件树
map <F3> :NERDTreeToggle<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" 运行程序
map <F5> :call CompileRun()<CR>
func! CompileRun()
    exec "w"
    if &filetype == 'c'
        exec "!g++ % -o %<"
        exec "! ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %<"
        exec "! ./%<"
    elseif &filetype == 'java' 
        exec "!javac %" 
        exec "!java %<"
    elseif &filetype == 'sh'
        :!./%
	elseif &filetype == 'py'
		exec "!clear"
        exec "!time python3 %"
    endif
endfunc
"新建.c,.h,.sh,.java文件，自动插入文件头 
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.java,*.py exec ":call SetTitle()" 
""定义函数SetTitle，自动插入文件头 
func SetTitle() 
    "如果文件类型为.sh文件 
    if &filetype == 'sh' 
        call setline(1,"\#########################################################################") 
        call append(line("."), "\# File Name: ".expand("%")) 
        call append(line(".")+1, "\# Author: monkeyhack") 
        call append(line(".")+2, "\# Created Time: ".strftime("%c")) 
        call append(line(".")+3, "\#########################################################################") 
        call append(line(".")+4, "\#!/bin/bash") 
        call append(line(".")+5, "") 
    else 
		if &filetype == 'py'
			call setline(1,"#########################################")
			call append(line("."), "# File Name: ".expand("%"))
			call append(line(".")+1, "# Author:monkeyhack")
			call append(line(".")+2, "#########################################################################") 
        	call append(line(".")+3, "# -*- coding:utf-8 -*-") 
        	call append(line(".")+4, "")
		else
        	call setline(1, "/*************************************************************************") 
        	call append(line("."), "    > File Name: ".expand("%")) 
        	call append(line(".")+1, "    > Author: monkeyhack") 
        	call append(line(".")+2, "    > Created Time: ".strftime("%c")) 
        	call append(line(".")+3, " ************************************************************************/") 
        	call append(line(".")+4, "")
		endif
    endif
    if &filetype == 'cpp'
        call append(line(".")+5, "#include<iostream>")
        call append(line(".")+6, "using namespace std;")
        call append(line(".")+7, "")
    endif
    if &filetype == 'c'
        call append(line(".")+5, "#include<stdio.h>")
        call append(line(".")+6, "")
    endif
    "新建文件后，自动定位到文件末尾
    autocmd BufNewFile * normal G
endfunc 

