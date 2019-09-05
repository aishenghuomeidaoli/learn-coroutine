# pipeline.py
#
# An example of setting up a processing pipeline with generators
import os


def grep(pattern, lines):
    for log_line in lines:
        if pattern in log_line:
            yield log_line


if __name__ == '__main__':
    from follow import follow

    # Set up a processing pipe : tail -f | grep python
    logfile = open(os.path.join(os.path.dirname(__file__), "access-log"))
    log_lines = follow(logfile)
    py_lines = grep("python", log_lines)

    # Pull results out of the processing pipeline
    for line in py_lines:
        print(line, end='')
