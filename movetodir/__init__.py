from fman import DirectoryPaneCommand, show_alert, show_prompt
import os
import shutil
from fman.url import as_human_readable
from fman.url import as_url


class MoveToDir(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        output = ""
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirPath = os.path.dirname(as_human_readable(selected_files[0])) + os.sep
            ndnam,okay = show_prompt("Directory Name?")
            if okay:
                numf = 0
                newdirp = dirPath + ndnam + os.sep
                if not os.path.isdir(newdirp):
                    os.mkdir(newdirp)
                for filep in selected_files:
                    head, tail = os.path.split(as_human_readable(filep))
                    filename = tail or os.path.basename(head)
                    shutil.move(dirPath + filename,newdirp + filename)
                    numf += 1
                output += str(numf) + " items were moved!"
            else:
                output = "User Canceled!"
        else:
            output += "No files or directories selected"

        show_alert(output)
