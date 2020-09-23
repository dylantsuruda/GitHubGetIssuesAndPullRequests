# Standard Python libraries
import sys
import os
import pathlib
import time
from datetime import datetime

# Python GitHub API wrapper library
# https://github.com/sigmavirus24/github3.py
# pip install github3.py
import github3


# For calculating runtime
print("Time at start: " + str(datetime.now().time()))
start_time = time.time()

if len(sys.argv) != 4:
    sys.exit("Incorrect usage -- look at the README for command line argument details")

repo_owner = sys.argv[1]
repo_name = sys.argv[2]
output_directory = sys.argv[3]
filename_path_prefix = os.path.join(output_directory, "")

# I have a personal access token for GitHub stored as an environment variable called "GITHUB_PERSONAL_ACCESS_TOKEN".
# You'll need to create your own GitHub personal access token to access the GitHub API.
# The README has more information about the personal access token.
github = github3.login(token=os.environ['GITHUB_PERSONAL_ACCESS_TOKEN'])
repository = github.repository(repo_owner, repo_name)
issues_pullrequests = repository.issues(state="all")  # Retrieves both issues and pull requests

has_issues = False
issue_title = ""
issue_titleplain = ""
issue_body = ""
issue_bodyplain = ""
issue_titlebody = ""
issue_titlebodyplain = ""
issue_document_count = 0

has_pullrequests = False
pullrequest_title = ""
pullrequest_titleplain = ""
pullrequest_body = ""
pullrequest_bodyplain = ""
pullrequest_titlebody = ""
pullrequest_titlebodyplain = ""
pullrequest_document_count = 0

for issue_pullrequest in issues_pullrequests:
    number = str(issue_pullrequest.number)
    title = str(issue_pullrequest.title)
    body = str(issue_pullrequest.body)
    if issue_pullrequest.pull_request_urls is None:
        # Then this is an issue, not a pull request
        has_issues = True
        issue_title += ("Document " + str(issue_document_count) + "\n" + "#" + number + ": "
            + title + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_titleplain += (title + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_body += ("Document " + str(issue_document_count) + "\n" + "#" + number + ":\n"
            + body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_bodyplain += (body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_titlebody += ("Document " + str(issue_document_count) + "\n" + "#" + number
            + " Title: " + title + "\n" + "#" + number + " Body:\n" + body
            + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_titlebodyplain += (title + "\n" + body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        issue_document_count += 1
    else:
        # Then this is a pull request
        has_pullrequests = True
        pullrequest_title += ("Document " + str(pullrequest_document_count) + "\n" + "#" + number + ": "
            + title + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_titleplain += (title + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_body += ("Document " + str(pullrequest_document_count) + "\n" + "#" + number + ":\n"
            + body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_bodyplain += (body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_titlebody += ("Document " + str(pullrequest_document_count) + "\n" + "#" + number
            + " Title: " + title + "\n" + "#" + number + " Body:\n" + body
            + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_titlebodyplain += (title + "\n" + body + "\n" + "-D-E-L-I-M-I-T-E-R-" + "\n")
        pullrequest_document_count += 1
    # The GitHub API limits the amount a user can request information from the API, so I'm making the script
    # wait if I get close to the rate limit.
    if issues_pullrequests.ratelimit_remaining < 10:
        rates = github.rate_limit()
        print()
        print("----PAUSING PROGRAM AND WAITING FOR RATE LIMIT TO RESET----")
        print("----CURRENT TIME: " + str(datetime.now().time()) + "----")
        sec_to_wait = int(rates.get("resources").get("core").get("reset") - time.time())
        sec_to_wait += 60  # Adding sixty seconds just in case
        print("----APPROXIMATE TIME TO WAIT: " + str(sec_to_wait/60) + " MINUTES----")
        time.sleep(sec_to_wait)
        print()
        print("----RATE LIMIT RESET AND CONTINUING PROGRAM----")
        print("----CURRENT TIME: " + str(datetime.now().time()) + "----")
        print()

# Creates a directory if it doesn't already exist
pathlib.Path(output_directory).mkdir(parents=True, exist_ok=True)

if has_issues:
    with open(filename_path_prefix + "issuestitle" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_title)
    with open(filename_path_prefix + "issuestitleplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_titleplain)
    with open(filename_path_prefix + "issuesbody" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_body)
    with open(filename_path_prefix + "issuesbodyplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_bodyplain)
    with open(filename_path_prefix + "issuestitlebody" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_titlebody)
    with open(filename_path_prefix + "issuestitlebodyplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(issue_titlebodyplain)

if has_pullrequests:
    with open(filename_path_prefix + "pullrequeststitle" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_title)
    with open(filename_path_prefix + "pullrequeststitleplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_titleplain)
    with open(filename_path_prefix + "pullrequestsbody" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_body)
    with open(filename_path_prefix + "pullrequestsbodyplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_bodyplain)
    with open(filename_path_prefix + "pullrequeststitlebody" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_titlebody)
    with open(filename_path_prefix + "pullrequeststitlebodyplain" + ".txt", "w", encoding="utf-8") as file:
        file.write(pullrequest_titlebodyplain)

print("Runtime: " + str(time.time() - start_time) + " seconds")
print("Time at finish: " + str(datetime.now().time()))
