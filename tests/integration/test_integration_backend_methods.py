import pytest

from threescale_api.errors import ApiClientError

from tests.integration import asserts

def test_list_methods(backend_hits_metric, backend_method):
    assert len(backend_hits_metric.methods.list()) >= 1

def test_should_create_method(backend_method, method_params):
    asserts.assert_resource(backend_method)
    asserts.assert_resource_params(backend_method, method_params)


def test_should_not_create_method_for_custom_metric(backend_hits_metric, method_params):
    resource = backend_hits_metric.methods.create(params=method_params, throws=False)
    asserts.assert_errors_contains(resource, ['system_name'])


def test_should_friendly_name_be_required(backend_hits_metric):
    resource = backend_hits_metric.methods.create(params={}, throws=False)
    asserts.assert_errors_contains(resource, ['friendly_name'])


def test_should_raise_api_exception(backend_hits_metric):
    with pytest.raises(ApiClientError):
        backend_hits_metric.methods.create(params={})


def test_should_read_method(backend_method, method_params):
    resource = backend_method.read()
    asserts.assert_resource(resource)
    asserts.assert_resource_params(resource, method_params)


def test_should_update_method(backend_method, updated_method_params):
    resource = backend_method.update(params=updated_method_params)
    asserts.assert_resource(resource)
    asserts.assert_resource_params(resource, updated_method_params)


def test_should_delete_method(backend_hits_metric, updated_method_params):
    resource = backend_hits_metric.methods.create(params=updated_method_params)
    assert resource.exists()
    resource.delete()
    assert not resource.exists()


def test_should_list_methods(backend_hits_metric):
    resources = backend_hits_metric.methods.list()
    assert len(resources) == 1
