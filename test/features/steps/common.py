#
# Copyright (c) 2014 ThoughtWorks, Inc.
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import string
import random


def random_username():
    try:
        randomname
    except:
        global randomname
        randomname=''.join(random.choice(string.lowercase) for i in range(8))
    return randomname

def random_password():
    try:
        randompassword
    except:
        global randompassword
        randompassword=''.join(random.choice(string.lowercase) for i in range(16))
    return randompassword


def fill_by_xpath(context, xpath, text):
    field = context.browser.find_element_by_xpath(xpath)
    field.send_keys(text)


def take_screenshot(context, filename):
    context.browser.save_screenshot(filename)


def dump_source_to(context, filename):
    with open(filename, 'w') as out:
        out.write(context.browser.page_source.encode('utf8'))

def wait_until_element_is_visible_by_locator(context, locator_tuple):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located(locator_tuple))
    return context.browser.find_element(locator_tuple[0], locator_tuple[1])


def find_element_by_xpath(context, xpath):
    return wait_until_element_is_visible_by_locator(context, (By.XPATH, xpath))


def find_element_by_id(context, id):
    return wait_until_element_is_visible_by_locator(context, (By.ID, id))


def find_element_by_css_selector(context, css_selector):
    return wait_until_element_is_visible_by_locator(context, (By.CSS_SELECTOR, css_selector))


def find_elements_by_css_selector(context, css_selector):
    return wait_until_elements_are_visible_by_locator(context, (By.CSS_SELECTOR, css_selector))


def find_element_containing_text(context, text, element_type='*'):
    return find_element_by_xpath(context, "//%s[contains(.,'%s')]" % (element_type, text))


def element_should_have_content(context, css_selector, content):
    e = find_element_by_css_selector(context, css_selector)
    assert_that(e.text, equal_to(content))


def click_button(context, title, element='button'):
    button = find_element_containing_text(context, title, element_type=element)
    button.click()

