import time

from selenium import webdriver
# These 3 methods are for ExplicitWaits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Exception library
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, \
    ElementClickInterceptedException

import pandas as pd


def scrap_web(location, job):
    website = 'https://www.glassdoor.com/Job/'

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(chrome_options)

    driver.get(website)

    time.sleep(5)

    search_job = driver.find_element(By.ID, 'sc.keyword')
    search_job.send_keys(job)

    search_location = driver.find_element(By.ID, 'sc.location')
    search_location.send_keys(location, Keys.ENTER)

    jobs_info = []

    # Let's get the number of pages with jobs
    num_pages = ""
    while True:
        try:
            num_pages = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'paginationFooter'))).text
        except TimeoutException:
            print('The number of pages is not present.')
            driver.refresh()
            continue
        except WebDriverException:
            driver.refresh()
            continue
        else:
            break

    num_pages = num_pages.split()[-1]

    time.sleep(3)
    accept_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    accept_cookies.click()

    first_job = True

    for page in range(int(num_pages)):
        time.sleep(4)
        # Get all the jobs present in the current page
        jobs = driver.find_element(By.XPATH, '//*[@id="MainCol"]/div[1]/ul').find_elements(By.TAG_NAME, 'li')

        for job in jobs:
            try:
                time.sleep(1)
                try:
                    job.click()
                except Exception:
                    print("Click?")

                while first_job:
                    try:
                        close_login = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//*[@id='LoginModal']/div/div/div[2]/button")))
                        close_login.click()
                    except TimeoutException:
                        print('The login modal is not present')
                        driver.refresh()
                        continue
                    except WebDriverException:
                        print("Unexpected webdriver exception")
                        driver.refresh()
                        continue
                    except Exception:
                        print("Login modal??")
                    else:
                        first_job = False
                        break

                time.sleep(1)

                job_data = {}

                try:
                    published_ago = job.find_element(By.CSS_SELECTOR, '[data-test="job-age"]').text
                except NoSuchElementException:
                    published_ago = -1

                try:
                    salary = job.find_element(By.CLASS_NAME, 'salary-estimate').text
                except NoSuchElementException:
                    salary = -1

                try:
                    rating = driver.find_element(By.CSS_SELECTOR, 'span[data-test="detailRating"]').text
                except TimeoutException:
                    print('The rating is not present.')
                    continue
                except NoSuchElementException:
                    rating = -1
                    continue
                except Exception:
                    print("rating??")

                try:
                    employer = driver.find_element(By.CSS_SELECTOR, '[data-test="employerName"]').text
                except NoSuchElementException:
                    employer = -1

                try:
                    job_title = driver.find_element(By.CSS_SELECTOR, 'div[data-test="jobTitle"]').text
                except NoSuchElementException:
                    job_title = -1

                try:
                    location_job = driver.find_element(By.CSS_SELECTOR, '[data-test="location"]').text
                except NoSuchElementException:
                    location_job = -1

                job_data['PublishedAgo'] = published_ago
                job_data['Salary'] = salary
                job_data['Rating'] = rating
                job_data['Employer'] = employer
                job_data['JobTitle'] = job_title
                job_data['Location'] = location_job

                container = driver.find_element(By.CLASS_NAME, 'd-flex.flex-wrap')
                cells = container.find_elements(By.CLASS_NAME, 'css-rmzuhb.e1pvx6aw0')

                for cell in cells:
                    name = cell.find_element(By.CLASS_NAME, 'css-1taruhi.e1pvx6aw1').text
                    value = cell.find_element(By.CLASS_NAME, 'css-i9gxme.e1pvx6aw2').text

                    job_data[name] = value

                print(job_data)
                jobs_info.append(job_data)

            except TimeoutException:
                print('Timeout al esperar la página del trabajo.')
            except WebDriverException as e:
                print('Error al hacer clic en el trabajo:', str(e))
            except Exception as e:
                print('Error desconocido:', str(e))

        next_page = driver.find_element(By.CSS_SELECTOR, 'button.nextButton.job-search-opoz2d')
        next_page.click()

    df = pd.DataFrame(jobs_info)

    df.to_csv('datos.csv', index=False)

    driver.quit()


if __name__ == "__main__":
    location = ""
    job = "AI Engineer"
    scrap_web(location, job)
