from typing import Type
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.config_loader import ConfigLoader
from Test.parallel.prallel_deals_test import ParallelDealsPageTests
from Test.parallel.prallel_leads_test import ParallelLeadsPageTests
from Test.parallel.parllel_accounts_test import ParallelAccountsPageTests
from Test.parallel.prallel_contacts_test import ParallelContactsPageTests
from Test.parallel.prallel_activities_test import ParallelActivitiesPageTests

from Test.non_parallel.non_parallel_deals_test import NonParallelDealsPageTests
from Test.non_parallel.non_parallel_home_page_test import NonParallelHomePageTests
from Test.non_parallel.non_parallel_leads_test import NonParallelLeadsPageTests
from Test.non_parallel.non_parallel_accounts_test import NonParallelAccountsPageTests
from Test.non_parallel.non_parallel_activities_test import NonParallelActivitiesPageTests
from Test.non_parallel.non_parallel_contacts_test import NonParallelContactsPageTests

serial_cases = [NonParallelDealsPageTests, NonParallelHomePageTests, NonParallelLeadsPageTests,
                NonParallelAccountsPageTests, NonParallelActivitiesPageTests, NonParallelContactsPageTests]
parallel_cases = [ParallelDealsPageTests, ParallelLeadsPageTests, ParallelAccountsPageTests, ParallelContactsPageTests,
                  ParallelActivitiesPageTests]
test_cases = [NonParallelDealsPageTests, NonParallelHomePageTests, NonParallelLeadsPageTests,
              NonParallelAccountsPageTests, NonParallelActivitiesPageTests, NonParallelContactsPageTests,
              ParallelDealsPageTests, ParallelLeadsPageTests, ParallelAccountsPageTests, ParallelContactsPageTests,
              ParallelActivitiesPageTests]
demo_cases = [NonParallelAccountsPageTests]

def run_tests_for_browser(browser: str, test_case: Type[unittest.TestCase]):
    test_case.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browsers, serial_tests):
    for test in serial_tests:
        for browser in browsers:
            run_tests_for_browser(browser, test)


def run_tests_for_browser_parallel(browsers, parallel_tests):
    tasks = [(browser, test_case) for browser in browsers for test_case in parallel_tests]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_tests_for_browser, browser, test_case) for browser, test_case in tasks]


if __name__ == "__main__":
    config_loader = ConfigLoader()
    config = config_loader.load_config()
    is_parallel = config['parallel']
    is_serial = not config['parallel']
    browsers = config["browser_types"]
    grid_url = config["hub"]
    # if is_parallel:
    #     run_tests_for_browser_parallel(browsers, parallel_cases)
    #     run_tests_for_browser_serial(browsers, serial_cases)
    # elif is_serial:
    #     run_tests_for_browser_serial(browsers, test_cases)
    run_tests_for_browser_serial(browsers, demo_cases)

