import sys
import time


class ProgressBar:

    """Simple progress bar class."""

    def __init__(
        self, start_value, total_value, width, start_border='[',
        end_border=']', progress_char='#', remaining_char='-'
    ):
        """Initialize progress bar.

        :start_value: initial value
        :total_value: Total value
        :width: progressbar width
        :start_border: Character at the start of progress bar
        :end_border: Character at the end of progress bar
        :progress_char: Character indicating progress
        :remaining_char: Character indicating remaining progress

        """
        self._start_value = start_value
        self._total_value = total_value
        self._width = width
        self._start_border = start_border
        self._end_border = end_border
        self._progress_char = progress_char
        self._remaining_char = remaining_char

        self._progress = self.set_progress(self._start_value)

    def set_progress(self, value):
        """Update progress.

        :value: new value
        :returns: number of progress characters.

        """
        return round(self._width * value / self._total_value)

    def progress(self, value):
        self._progress = self.set_progress(value)
        sys.stdout.write("\r{}{}{}{}".format(
            self._start_border,
            self._progress_char * self._progress,
            self._remaining_char * (self._width - self._progress),
            self._end_border)
        )
        sys.stdout.flush()

    def do_with_progress(self, iterator):
        for value in iterator:
            self.progress(value)

if __name__ == "__main__":
    import time
    pb = ProgressBar(1, 100, 50)
    for i in range(100):
        pb.progress(i)
        time.sleep(0.1)

    #def sleeper():
    #    for i in range(100):
    #        yield i
    #        time.sleep(0.1)
    #pb.do_with_progress(sleeper())
    #print()
