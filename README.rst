*********
mpi-print
*********

Print statements from MPI programs can be confusing, as you do not now
by which rank the output was produced. The import of

.. code-block:: python

    from mpi_print import print

overloads the the builtin print function to first print the rank and
a timestamp. E.g.

.. code-block:: python

    from mpi_print import print, builtin_print
    builtin_print('hello world.') # prints:
    #   hello world.
    print('hello world.') # prints:
    #   MPI rank: 1 [timestamp: 2023-02-02 20:48:26.544420]
    #   hello world.

* Documentation: https://mpi_print.readthedocs.io
