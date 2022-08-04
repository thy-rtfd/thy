# Thy's desktop environment

How I configure my desktop environment

## Operating System

As of writing (Mar 2021), I use [Linux Mint 20 Cinnamon](https://linuxmint.com/rel_ulyana_cinnamon.php) (codename Ulyana) which is based on [Ubuntu 20.04](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes). 

[Cinnamon Desktop Environment](https://en.wikipedia.org/wiki/Cinnamon_(desktop_environment)) derives from [GNOME 3](https://en.wikipedia.org/wiki/GNOME_3) but follows traditional [desktop metaphor](https://en.wikipedia.org/wiki/Desktop_metaphor) conventions.

## Replicate Windows Shortcuts

I'm a Linux user who are `forced` to use Windows at work. 

Here's how to replicate Windows shortcuts to my Development Machine.

TODO: put the `dconf load` command

## Jetbrains PyCharm shortcuts conflict

Some shortcuts conflict with global system actions. To fix these conflicts, I reassign or disable the conflicting shortcut.

Taken from [jetbrains](https://www.jetbrains.com/help/pycharm/configuring-keyboard-and-mouse-shortcuts.html#conflicts), here are a few examples of system shortcut conflicts with the default keymap in PyCharm

| Shortcut            | System action                            | IntelliJ IDEA action            |
|---------------------|------------------------------------------|---------------------------------|
| Ctrl+Alt+S          | Shade window                             | Open the Settings dialog        |
| Ctrl+Alt+L          | Lock screen                              | Reformat Code                   |
| Ctrl+Alt+T          | Launch Terminal                          | Surround With                   |
| Ctrl+Alt+F12        | Open the tty12 virtual console	File path |                                 |
| Ctrl+Alt+Left/Right | Switch between Workspaces                | Undo/redo navigation operations |
| Alt+F7              | Move window                              | Find Usages                     |
 | Alt+F8              | Resize window                            | Evaluate Expression             |

## References

- <https://github.com/webpro/awesome-dotfiles>
