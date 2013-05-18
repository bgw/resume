Resume Generator
================

This is the set of generation scripts and custom templates I use to build [my
resume][]. The actual yaml data files I use are not public (because they contain
personal information that's only available in a private print version).

Features
--------

-   HTML and LaTeX (print) output targets
-   Tiny code-base
-   Easy to write your own templates

Setup on Debian (or a derivative)
---------------------------------

1.  Install some stuff through apt:

        sudo aptitude install rubygems latexmk python3 python3-jinja

2.  Install some stuff through rubygems:

        sudo gem install compass

3.  Write some configuration files (I need to provide some examples here).
4.  Run the build script with your configuration files:

        ./build ../path/to/build.yaml

5.  Look in `output` (will be created in the cwd) for your resulting html and
    pdf files.

To-Do
-----

-   Port build system from ReST to [Pandoc][], and allow the user to specify any
    input format they want
-   General code cleanup
-   Build with [Docco][] for some sexy literate programming magic
-   Make some example data files for public distribution with the repository

  [my resume]: https://www.cise.ufl.edu/~woodruff/
  [Pandoc]: http://johnmacfarlane.net/pandoc/
  [Docco]: https://github.com/jashkenas/docco
