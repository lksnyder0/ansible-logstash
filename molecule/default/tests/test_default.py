import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["logstash"])
def test_packages(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("svc", ["logstash"])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


def test_config_file(host):
    log_file = host.file("/etc/logstash/logstash.yml")

    assert log_file.exists
    assert log_file.user == "logstash"
    assert log_file.group == "logstash"
    assert log_file.mode == 0o0640


def test_config_file_contents(host):
    conf_file = host.file("/etc/logstash/logstash.yml")

    assert conf_file.md5sum == "21151e47aa7ae4d814323909b395701c"


def test_default_pipeline(host):
    pipeline_output = host.file("/tmp/logstash_output.txt")

    assert pipeline_output.exists
    assert b'"message":"ok"' in pipeline_output.content
