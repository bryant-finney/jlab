# `py3.9` Directory

This subdirectory configures [`pyenv`](https://github.com/pyenv/pyenv) to use a separate
interpreter from the rest of this project. The original motivation for this was that
[`neovim`](https://neovim.io/) did not support `python3.10` at the time of creation
([PR #15937](https://github.com/neovim/neovim/pull/15937) has been merged, but not
released).