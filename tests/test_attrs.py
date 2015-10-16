from tests.fixtures import basic_dockerfile  # nopep8

basic_dockerfile  # shut up pep8


def test_from(basic_dockerfile):
    assert basic_dockerfile.FROM
    assert len(basic_dockerfile.FROM) == 1
    assert basic_dockerfile.FROM[0].args == "ubuntu:trusty"


def test_many(basic_dockerfile):
    assert basic_dockerfile.RUN
    assert len(basic_dockerfile.RUN) == 3
    assert basic_dockerfile.RUN[0].cmd == "RUN"
    assert basic_dockerfile.RUN[0].args == "apt-get update"
    assert basic_dockerfile.RUN[1].args == "apt-get install -y python"
    assert basic_dockerfile.RUN[2].args == "apt-get install -y python-pip"
