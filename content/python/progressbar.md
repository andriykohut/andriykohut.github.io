Title: Simple python progress bar
Date: 2015-07-31 14:23
Modified: 2015-07-31 14:24
Category: Python
Tags: progressbar,python,eyecandy
Summary: How to create simple python progress bar without any external libraries

I'm big on beautiful command line tools, I often launch `htop` just to please my eyes. [tig](https://github.com/jonas/tig) output on a large repo with hundreds of intertwined branches is like an work of art to me.

When working on some command line tool or script I try make it beautiful. Today I'm going to explain how to create simple and beautiful command line progress bar in python.

So let's start, here's how `wget` progress bar looks like:
```
[#############################           ]
```
Here we have `[` and `]` indicating the left and right border of progress bar, progress is denoted by sequence of `#` characters, and remaining work is just a bunch of spaces.

Let's initialize our progress bar:
```python
class ProgressBar:

    def __init__(
        self, start_value, total_value, width, start_border='[',
        end_border=']', progress_char='#', remaining_char='-'
    ):
        self._start_value = start_value
        self._total_value = total_value
        self._width = width
        self._start_border = start_border
        self._end_border = end_border
        self._progress_char = progress_char
        self._remaining_char = remaining_char

        self._progress = self.set_progress(self._start_value)
```

Here we have following parameters:
* `start_value` - Initial value of progress
* `total_value` - Value for 100% progress
* `width` - progress bar width
* `start_border`, `end_border` - indicate the left and right borders of progress bar
* `progress_char` - single-character string to represent current progress
* `remaining_char` - single-character string to represent remaining progress

The variable `self._progress` will hold the current number of progress chars. Next we'll need to define `set_progress` method. That's simple:
```python
def set_progress(self, value):
    return round(self._width * value / self._total_value)
```
I didn't really knew how to make a progress bar to appear as a single line, without printing new line for each step, eg:
```
[########################                ]
[#############################           ]
[##################################      ]
```
and so on. But, as it turns out, it's pretty simple. `\r` - the carriage return character is what we need here. Here's what it does:
```ipython
In [1]: import sys

In [2]: lines = ['this will be removed', '\r', 'this will be displayed']

In [3]: for line in lines:
   ....:     sys.stdout.write(line)
   ....:
this will be displayed
```
If you ever used a typewriter, it should be familiar :)

So let's define a `progress` method which will actually display something - update progress:
```python
def progress(self, value):
     self._progress = self.set_progress(value)
     sys.stdout.write("\r{}{}{}{}".format(
         self._start_border,
         self._progress_char * self._progress,
         self._remaining_char * (self._width - self._progress),
         self._end_border)
     )
     sys.stdout.flush()
```

Here we just calculate the number of progress characters and remaining characters, and then rewrite the current progress line with the new one. Flushing is important to make sure progress updates with each step.

Let's try how it works:
```python
import time

pb = ProgressBar(1, 100, 50)
for i in range(100):
  pb.progress(i)
  time.sleep(0.1)
```
Here's some [asciinema](https://asciinema.org/) demo:
<script type="text/javascript" src="https://asciinema.org/a/0yda22tv9hafgr15ff4z28utm.js" id="asciicast-0yda22tv9hafgr15ff4z28utm" async></script>

Let's add some helper methods for working with generators:
```python
def do_with_progress(self, gen):
    for value in gen:
        self.progress(value)
```

Then we can have something like:
```python
def sleeper():
    for i in range(100):
        yield i
        time.sleep(0.1)
pb.do_with_progress(sleeper())
```
