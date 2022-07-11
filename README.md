You should install with pip awscli for installing aws command line interface.
- pip install awscli

create virtualenv for x86_64 architecture (it required for macos m1)
- /usr/local/Homebrew/bin/python3.9 -m venv de_env
- source de_env/bin/activate
- pip install --upgrade pip && pip install -r requirements.txt

Data source is a taxi trip data from New York. I downloaded from below link:
- https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Dataset between 2009 to current date. Totally data size is 42 GB. If you want to know more details of dataset, you can check the link.

If you don't connect redshift cluster from local, you must create a new VPC that allow your ip address or public routing.