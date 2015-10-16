import pytest

from pydockerfile.parser import DockerfileParser
from tests.fixtures import DOCKERFILE_PATH
from tests.fixtures import DOCKERFILE_LINE_CONT_PATH
from tests.fixtures import dockerfile_str
from tests.fixtures import dockerfile_line_cont_str


@pytest.mark.parametrize(
    "dockerfile, size",
    [(dockerfile_str(), len(dockerfile_str().strip().split("\n"))),
     (dockerfile_line_cont_str(), 3)])
def test_num_lines_str(dockerfile, size):
    parser = DockerfileParser()
    parsed_dockerfile = parser.from_string(dockerfile)
    assert len(parsed_dockerfile) == size


@pytest.mark.parametrize(
    "dockerfile_path, size",
    [(DOCKERFILE_PATH, len(dockerfile_str().strip().split("\n"))),
     (DOCKERFILE_LINE_CONT_PATH, 3)])
def test_num_line(dockerfile_path, size):
    parser = DockerfileParser()
    dockerfile = parser.from_file(dockerfile_path)
    assert len(dockerfile) == size


@pytest.mark.parametrize(
    "dockerfile_s, dockerfile_path, dockerfile_ne_path",
    [(dockerfile_str(), DOCKERFILE_PATH, DOCKERFILE_LINE_CONT_PATH),
     (dockerfile_line_cont_str(), DOCKERFILE_LINE_CONT_PATH, DOCKERFILE_PATH)])
def test_eq(dockerfile_s, dockerfile_path, dockerfile_ne_path):
    parser = DockerfileParser()
    dockerfile_str = parser.from_string(dockerfile_s)
    dockerfile_file = parser.from_file(dockerfile_path)
    dockerfile_ne = parser.from_file(dockerfile_ne_path)
    assert dockerfile_str == dockerfile_file
    assert dockerfile_str != dockerfile_ne
    assert dockerfile_file != dockerfile_ne
    assert dockerfile_ne == dockerfile_ne
