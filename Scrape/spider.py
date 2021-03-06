import time

from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

# TODO: replace this by your account info
NAME = ''
PASSWORD = ''
driver = Chrome()


def login(name='', pwd=''):
    login_url = 'https://leetcode.com/accounts/login/'

    if name and pwd:
        driver.get(login_url)
        driver.implicitly_wait(15)
        user = driver.find_element_by_id("username-input")
        pwd = driver.find_element_by_id("password-input")
        user.send_keys(NAME)
        pwd.send_keys(PASSWORD)

        signin = driver.find_element_by_id("sign-in-button")
        flag = True
        # TODO: make this less ugly - we need to wait for the page to
        # fully load before login can be clicked
        while (flag):
            try:
                time.sleep(0.5)
                signin.click()
                flag = False
            except WebDriverException:
                time.sleep(0.5)
        time.sleep(5)
        if (driver.current_url != login_url):
            print('Login succeeded')
            return True
        else:
            print('Login failed - check username and password')
            return False
    print('Need to provide a username and password!')
    return False


def show_all_problems():
    viewall = '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select/option[4]'
    driver.find_element_by_xpath(viewall).click()


def get_unlocked_problems():
    table = driver.find_element_by_class_name('reactable-data')
    unlockers = table.find_elements_by_xpath("tr/td[3]/div/span[1]/i[contains(@class, 'fa fa-unlock')]/../..")
    problem_pages = {}
    for unlock in unlockers:
        element = unlock.find_element_by_xpath("a")
        title = element.text
        href = element.get_attribute("href")

        problem_pages[title] = href
        print(title)
        print(href)

    return problem_pages


def get_problem_submission_page_urls():
    table = driver.find_element_by_class_name('reactable-data')
    # collect problem titles and links
    problemPages = {}
    for row in table.find_elements_by_tag_name("tr"):
        title = row.find_element_by_tag_name("a").text
        href = row.find_element_by_tag_name("a").get_attribute("href")
        # don't collect the links to solutions presented on leetcode
        if not "article" in href:
            problemPages[title] = href + "/discuss/?currentPage=1&orderBy=most_votes&query="
    return problemPages


def find_popular_discussions(url, res, problem):
    driver.get(url)
    driver.implicitly_wait(5)

    topic_items = driver.find_elements_by_xpath("//div[contains(@class, 'topic-item-wrap')]")

    for item in topic_items:
        score_element = item.find_element_by_xpath('div/div[2]/div[1]/div')

        link_element = item.find_element_by_xpath('div/div[1]/div/a')
        link = link_element.get_attribute("href")

        title_element = link_element.find_element_by_xpath('div/div')
        title = title_element.text

        score_text = score_element.text
        if 'K' in score_text:
            score = int(float(score_text.replace('K', '')) * 1000)
        else:
            score = int(score_text)

        if score >= 500:
            print('[{}]\t<{}>\t{}\n{}\n'.format(score, problem, title, link))
            res.append((score, problem, title, link))


def find_discussion_by_author(url, res, problem, author):
    driver.get(url)
    driver.implicitly_wait(5)

    topic_items = driver.find_elements_by_xpath("//div[contains(@class, 'topic-item-wrap')]")

    for item in topic_items:
        author_element = item.find_element_by_xpath('div/div[1]/div[2]/span/span/a')
        if author_element.text == author:
            link_element = item.find_element_by_xpath('div/div[1]/div[1]/a')
            link = link_element.get_attribute("href")

            title_element = link_element.find_element_by_xpath('div/div')
            title = title_element.text
            print(f'{problem}\t{title}\n{link}')

            res.append((problem, title, link))


def write_popular_discussion_to_file(res):
    with open('popular discussions.txt', 'w', encoding='utf-8') as file:
        for score, problem, title, link in res:
            file.write('[{}]\t<{}>\t{}\n{}\n'.format(score, problem, title, link))


def write_author_discussion_to_file(res, author):
    with open(f'{author} discussions.txt', 'w', encoding='utf-8') as file:
        for problem, title, link in res:
            file.write('<{}>\t{}\n{}\n'.format(problem, title, link))


def output_to_file(title, difficulty, content):
    with open("unlock_problems/[{}] {}.html".format(difficulty, title), 'w', encoding='utf-8') as file:
        file.write("<p><strong>[{}] {}</strong></p>\n".format(difficulty, title))
        file.write(content)


def output_to_file2(problem, title, content):
    with open("StefanPosts/{}.html".format(problem), 'w', encoding='utf-8') as file:
        file.write("<p><strong>{}</strong></p>\n".format(problem))
        file.write("<p><strong>{}</strong></p>\n".format(title))
        file.write(content)


def scrape_unlock_problems():
    driver.get("https://leetcode.com/problemset/algorithms/")
    show_all_problems()

    problemUrls = get_unlocked_problems()

    for problem, url in problemUrls.items():
        driver.get(url)
        driver.implicitly_wait(5)

        title_node = driver.find_element_by_id('question-title')
        title = title_node.text

        print(title)

        difficulty = title_node.find_element_by_xpath("../div[2]/div").text

        content = driver.find_element_by_xpath("//div[contains(@class, 'darker-content')]")

        output_to_file(title, difficulty, content.get_attribute('innerHTML'))


def scrape_popular_discussions():
    driver.get("https://leetcode.com/problemset/algorithms/")
    show_all_problems()

    problem_urls = get_problem_submission_page_urls()
    res = []

    for problem, url in problem_urls.items():
        find_popular_discussions(url, res, problem)
        print('finish: {}'.format(problem))

    write_popular_discussion_to_file(res)


def scrape_discussion_by_author(author):
    driver.get("https://leetcode.com/problemset/algorithms/")
    show_all_problems()

    problem_urls = get_problem_submission_page_urls()
    res = []

    for problem, url in problem_urls.items():
        find_discussion_by_author(url, res, problem, author)

    write_author_discussion_to_file(res, author)


import re

def scrape_post_by_url():
    with open('StefanPochmann discussions.md') as f:
        for i, line in enumerate(f.readlines()):
            if i % 2:
                driver.get(line)
                time.sleep(1)
                driver.implicitly_wait(5)

                content = driver.find_element_by_xpath("//div[contains(@id, 'discuss-container')]/div/div/div[2]/div[1]/div[2]/div[2]/div")
                output_to_file2(problem, title, content.get_attribute('innerHTML'))
            else:
                problem, title = line.strip('\n').replace('<', '').replace('>', '').split('\t')


if __name__ == '__main__':
    if login(NAME, PASSWORD):
        scrape_post_by_url()
        # scrape_discussion_by_author('StefanPochmann')
        # scrape_popular_discussions()
        # scrape_unlock_problems()
    else:
        print("Login failed!")
