from fman import DirectoryPaneCommand, show_alert, show_prompt
from fman.fs import is_dir, makedirs, move
from fman.url import join, basename


class MoveToDir(DirectoryPaneCommand):
    def __call__(self):
        # get_chosen_files() returns the files selected by the user
        # (="red" files). If no files are selected, the file under the cursor
        # is returned:
        chosen_files = self.get_chosen_files()
        if chosen_files:   # equivalent to `len(chosen_files) > 0`
            ndnam, okay = show_prompt("Directory Name?")
            # Check ndnam as well because it could be empty
            if ndnam and okay:
                numf = 0
                newdirp = join(self.pane.get_path(), ndnam)
                if not self.isADir(newdirp):
                    # Create directory and its parent directories:
                    makedirs(newdirp)
                for filep in chosen_files:
                    move(filep, join(newdirp, basename(filep)))
                    numf += 1
                show_alert('%d items were moved!' % numf)
        else:
            show_alert("No files or directories selected")

    def isADir(self, path):
        result = False
        try:
            result = is_dir(path)
        except Exception:
            result = False
        return(result)
