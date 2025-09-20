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

I highly recommend running this against to the staging environment because the production environment has bot checks that will likely cause the tests to fail.

