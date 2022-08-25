# BASIC EXAMPLE FROM https://docs.prefect.io/
print("basicExample with Imports running........")
from prefect import flow, task
import httpx
import hello
import getStars
hello.my_function()

@task(retries=3)
getStars.get_stars(repo)

@flow
def github_stars(repos):
    for repo in repos:
        get_stars(repo)

# call the flow!
github_stars(["PrefectHQ/Prefect", "PrefectHQ/prefect-aws",  "PrefectHQ/prefect-dbt"])