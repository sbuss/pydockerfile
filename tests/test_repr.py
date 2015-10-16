import pytest

from tests.fixtures import basic_dockerfile  # nopep8
from tests.fixtures import dockerfile_with_comments  # nopep8


@pytest.mark.parametrize(
    "dockerfile, expected",
    [(basic_dockerfile(), "<Dockerfile(FROM ubuntu:trusty...)>"),
     (dockerfile_with_comments(), "<Dockerfile(# Comments before FROM...)>")])
def test_dockerfile_repr(dockerfile, expected):
    assert repr(dockerfile) == expected


def test_line_repr(dockerfile_with_comments):
    assert (repr(dockerfile_with_comments.lines[0]) ==
            "<Line(#, Comments before FROM)>")
    assert (repr(dockerfile_with_comments.lines[1]) ==
            "<Line(FROM, ubuntu)>")
    assert (repr(dockerfile_with_comments.lines[2]) == "<Line(, )>")
    assert (repr(dockerfile_with_comments.lines[3]) ==
            "<Line(RUN, apt-get update && apt-get install -y python)>")
    assert (repr(dockerfile_with_comments.lines[4]) == "<Line(, )>")
    assert (repr(dockerfile_with_comments.lines[5]) ==
            "<Line(#, Comments below a RUN)>")
    assert (repr(dockerfile_with_comments.lines[6]) ==
            "<Line(#, Comment without a leading space)>")
    assert (repr(dockerfile_with_comments.lines[7]) == "<Line(, )>")
    assert (repr(dockerfile_with_comments.lines[8]) ==
            "<Line(CMD, bash)>")
