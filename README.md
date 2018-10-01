## MoveToDir

Plugin for [fman.io](https://fman.io) to move a selection of files to a directory. If the directory doesn't exist, create it and move the files.

Install with [fman's built-in command for installing plugins](https://fman.io/docs/installing-plugins).

### Usage

Select one or more files/directories and press **Shift+m** (I'm using my Vim Keymappings). Fman will then ask for a directory name. If the directory doesn't exist, create it and move the files there. Otherwise, just move the files.

**Warning**: Currently it runs in the same process/thread so be aware that running properties on a large dir will cause the UI to hang while calculating size

### Features

 - Creates named directory if it doesn't exist
 - Moves the files to that directory
