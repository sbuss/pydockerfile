import pytest

from pydockerfile.parser import DockerfileParser


DOCKERFILE_PATH = 'tests/dockerfiles/basic.Dockerfile'
DOCKERFILE_LINE_CONT_PATH = 'tests/dockerfiles/line-cont.Dockerfile'
DOCKERFILE_WITH_COMMENTS_PATH = 'tests/dockerfiles/with-comments.Dockerfile'


@pytest.fixture
def dockerfile_str():
    with open(DOCKERFILE_PATH) as f:
        return f.read()


@pytest.fixture
def dockerfile_line_cont_str():
    with open(DOCKERFILE_LINE_CONT_PATH) as f:
        return f.read()


@pytest.fixture
def dockerfile_with_comments_str():
    with open(DOCKERFILE_WITH_COMMENTS_PATH) as f:
        return f.read()


@pytest.fixture
def basic_dockerfile():
    parser = DockerfileParser()
    return parser.from_string(dockerfile_str())


@pytest.fixture
def dockerfile_with_comments():
    parser = DockerfileParser()
    return parser.from_string(dockerfile_with_comments_str())
