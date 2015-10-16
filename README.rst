.. image:: https://travis-ci.org/sbuss/pydockerfile.svg?branch=master
    :target: https://travis-ci.org/sbuss/pydockerfile

pydockerfile
============

``pydockerfile`` gives simplistic Dockerfile parsing. It performs no validation.


Installation
------------

.. code-block:: bash

    pip install pydockerfile

Usage
-----

.. code-block:: python

    import pydockerfile
    dockerfile = pydockerfile.parse_file('/path/to/Dockerfile')
    assert dockerfile.FROM
