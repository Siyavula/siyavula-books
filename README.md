siyavula-books
==============

This repository contains the source code from which we compile the Siyavula Everything* Series books. These works are released under a Creative Commons Attribution 3.0 Unported license. Please see the file contained within this repository called 'license.txt' for the full license agreement.



Book format
-----------

These books are typeset in a markup language called LaTeX.

To compile these books you will need a modern version of TexLive with most of the add-on packages. We made a small modfication to the mdframed.sty package and this file should be copied into your mdframed/ folder in the texlive installation folder. The file is contained in the extras folder in this directory.


Each book folder contains a file called "build.sh". Running this file with a working texlive distribution should result in a file called 'main.pdf' containing the compiled pdf form of the book. We have tested this only on Ubuntu Linux.

        
