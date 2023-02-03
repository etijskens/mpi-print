# -*- coding: utf-8 -*-

"""
The `mpi_print` module exports:

- `print`, a decorated version of the builtin `print` function. It first prints its arguments,
  preceded by a line identifying the MPI rank of the printing proces, and a timestamp.
- `builtin_print`, a reference to the builtin `print` function.
- `mpi_rank`, a function returning the MPI rank of the current proces.

## Typical use

```
    >>> from mpi_print import print         # mpi_print_decorator(print)
    >>> from mpi_print import builtin_print # the builtin print, as is.
    >>> builtin_print("Hello, world.")
    Hello, world.
    >>> print("Hello, world.")

    MPI rank: 0 [timestamp: 2023-02-02 20:48:26.544420]
    Hello, world.
    >>> from mpi_print import mpi_rank
    >>> mpi_rank()
    0
    >>>
```
"""

__version__ = "0.1.0"


from mpi4py import MPI
import io
from pathlib import Path
from datetime import datetime

builtin_print = print


def mpi_rank() -> int:
    """Convenience function that retrieves the rank of the current process.

    Returns:
        The rank of the current process.
    """
    return MPI.COMM_WORLD.Get_rank()


def _mpi_print_decorator(func):
    """A decorator for the builtin print function that first prints a message identifying
    the printing rank and a timestamp.

    (For internal use only).
    """

    def wrapper(*args, **kwargs):
        # remember the 'file' keyword argument if present, to make printing to file and StringIO, ... work too.
        if 'file' in kwargs:
            file = kwargs['file']
            del kwargs['file']
        else:
            file = None

        output = io.StringIO()
        # We first print to a string and than print the string to stdout. This is to avoid
        # that different print calls get separated in the output because several ranks may
        # bne writing simultaneously.
        builtin_print(f"\nMPI rank: {mpi_rank()} [timestamp: {datetime.now()}]\n"
                      , *args, file=output, **kwargs)
        # probhibit that the line following 'MPI rank: <rank>' starts with a space.
        output = output.getvalue().replace("\n ", "\n")
        builtin_print(output, file=file)

    return wrapper


# Decorate the builtin print function and use it as the default print.
# The decorated print funtion accepts all the same arguments.
# The undecorated function is still accessible as builtin_print from this module.
print = _mpi_print_decorator(builtin_print)



# ==============================================================================
# Q&D test code
if __name__ == "__main__":
    # test print
    # import random, time
    # time.sleep(random.random())
    print(f"-*# rank {mpi_rank()} print to stdout #*-")

    # test printing to a file
    with open("mpi_print.output.txt", mode="a") as f:
        print(f"-*# rank {mpi_rank()} print to 'mpi_print.output.txt' #*-", file=f)

