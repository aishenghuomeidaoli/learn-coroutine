# follow.py
#
# A generator that follows a log file like Unix 'tail -f'.
#
# Note: To see this example work, you need to apply to 
# an active server log file.  Run the program "logsim.py"
# in the background to simulate such a file.  This program
# will write entries to a file "access-log".
import os, time


def follow(the_file):
    # f.seek(offset, from_what)
    # offset 代表某一行偏移量，from_what 0|1|2 0代表文件首行，1代表当前行，2代表文件末行
    the_file.seek(0, 2)
    while True:
        log_line = the_file.readline()
        if not log_line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield log_line


# Example use
if __name__ == '__main__':
    logfile = open(os.path.join(os.path.dirname(__file__), "access-log"))
    for line in follow(logfile):
        print(line, end='')
