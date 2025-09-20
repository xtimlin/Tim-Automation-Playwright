# Project Setup
## Mac Setup
1. Creating a Virtual Environment `python -m venv venv`
2. Activating the Virtual Environment `source .venv/bin/activate`
3. Upgrade pip `python -m pip install --upgrade pip`
4. Install python packages `pip install -r requirements.txt`
5. Install Playwright `playwright install`


## Setup Windows
1. Creating a Virtual Environment `python -m venv .venv`
2. Activating the Virtual Environment `.\.venv\Scripts\activate`
3. Upgrade pip `python -m pip install --upgrade pip`
4. Install python packages `pip install -r requirements.txt`
5. Install Playwright `playwright install`

# Run Test
```commandline
pytest                                              # default run with chrome in headless
pytest --headed                                     # run with headed mode

pytest --browser=chromium                           # run with chromium browser 
pytest --browser=firefox                            # run with firefox browser 
pytest --browser=webkit                             # run with webkit browser

pytest --base-url=https://consumeraffairs.com/      # run with different enveriment url


pytest --browser=chromium --headed --slowmo=200 --base-url=https://consumeraffairs.com/
```



# Project Status and Environment Notes
## [Main branch](https://github.com/xtimlin/Tim-Automation-Playwright)
* The main branch of this project is configured to run tests against https://consumeraffairs.com/.
* Due to the website's bot detection system, my automation scripts will fail. This is an expected behavior, not a bug in the code.
* I highly recommend running this against to the staging environment if you want to try.

## [Expand_testing](https://github.com/xtimlin/Tim-Automation-Playwright/tree/expand_testing)
* I have created a separate branch called expand_testing that targets https://practicetestautomation.com/.
* All tests on this branch are running successfully, both locally and in [GitHub Actions](https://github.com/xtimlin/Tim-Automation-Playwright/actions/runs/17880307297).


