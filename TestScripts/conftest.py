from SupportLibraries.driver_factory import DriverFactory
import pytest


@pytest.fixture(scope="session")
def get_driver(request, browser, platform, environment):
    print("session_level_setup: Running session level setup.")
    df = DriverFactory(browser, platform, environment)
    driver = df.get_driver_instance()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    print("session_level_setup: Running session level teardown.")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser Type")
    parser.addoption("--platform", help="Operating System Type")
    parser.addoption("--environment", help="Application Environment")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--environment")
