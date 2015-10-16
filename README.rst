pydockerfile
============

`pydockerfile` gives simplistic Dockerfile parsing. It performs no validation.


Installation
------------

.. code-block:: bash
    pip install pydockerfile

Usage
-----

.. code-block:: python
    import pydockerfile
    dockerfile = pydockerfile.parse('/path/to/Dockerfile')
    assert dockerfile.FROM
