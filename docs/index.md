# The mpi_print package

This module provides a `print` function that prints its arguments, 
preceeded by a line identifying the MPI rank of the printing 
process, and a timestamp. This is helpful when examining the output
from different ranks in the same file or file-like object.

The exported `print()` function is in fact a decorated version of
the builtin `print()` using the _mpi_print_decorator. It takes the 
same arguments as the original builtin`print()` function, which is 
also available from the `mpi_print` module as `builtin_print`.

To use the decorated print function instead of the builtin print put this import statement
in a script or module:

```
    >>> from mpi_print import print         # mpi_print_decorator(print)
    >>> from mpi_print import builtin_print # the builtin print, as is.
    >>> builtin_print("Hello, world.")
    Hello, world.
    >>> print("Hello, world.")

    MPI rank: 0 [timestamp: 2023-02-02 20:48:26.544420]
    Hello, world.
```
In fact, this is all you need to know. 