# GitHubGetIssuesAndPullRequests
*A script that interacts with the GitHub API to retrieve a repository's information*

---

## What is GitHubGetIssuesAndPullRequests?
`GitHubGetIssuesAndPullRequests` primarily contains `getissuesandpullrequests.py`, a command line Python script that retrieves all the text for titles and bodies for issues and pull requests for a given GitHub repository.

In addition, to demonstrate the output of the script, I've included the directories `GitHubInfo-ApacheSpark` and `GitHubInfo-NotepadPlusPlus`, which are the actual outputs I received after running the script in mid-May 2020. I've also included a small program `sampleanalysis.py` that demonstrates what one could do with the results of `getissuesandpullrequests.py`.

## How to run getissuesandpullrequests.py
First, set up a personal access token with GitHub (see *The GitHub personal access token* section below). Then, look at line 29 in the code and modify as necessary. (If you just want to see what the output of the script returns, `GitHubInfo-ApacheSpark` and `GitHubInfo-NotepadPlusPlus` are actual outputs of the script.)

Also, make sure you have the packages in the `requirements.txt` file:
```
pip install -r requirements.txt
```

`getissuesandpullrequests.py` needs these three command line arguments in this order:
1. Owner's GitHub username for the repository
2. Repository name
3. Output directory

For example, if you wanted to retrieve information on the [Apache Spark repository](https://github.com/apache/spark), then the first argument would be *apache* because the username of the owner of the Apache Spark repository is *apache*. The second argument would be *spark* since *spark* is the name of the Apache Spark repository. Finally, the third argument would be whatever directory you'd want the output information to be put into (perhaps *GitHubInfo-ApacheSpark*). The command to run the script would look like this:
```
python getissuesandpullrequests.py apache spark GitHubInfo-ApacheSpark
```

If you wanted to get information for the [Notepad++ repository](https://github.com/notepad-plus-plus/notepad-plus-plus), the command would be this:
```
python getissuesandpullrequests.py notepad-plus-plus notepad-plus-plus GitHubInfo-NotepadPlusPlus
```

The third argument (the output directory) does not need to exist prior to running the script. If it does exist, the script will put the output information into that directory. The script will also overwrite any files in the directory that matches the hardcoded names for the output files.

## How to read (and use) the output information
If you open `GitHubInfo-NotepadPlusPlus`, you'll notice there's twelve files -- six regarding issues and six regarding pull requests. The more human-readable files are the ones without *plain* in the filename; the plain files are useful for passing to programs that can analyze textual information.

Running `sampleanalysis.py` will print out the twenty most frequent terms in the Notepad++ issue titles. To run `sampleanalysis.py`, use this command:
```
python sampleanalysis.py
```

`sampleanalysis.py` is not a very sophisticated script; it's just intended to give an idea on what the outputs of `getissuesandpullrequests.py` can be used for. I don't remove any stop words (words like *a* and *the*) in this sample analysis.

(You'll notice `GitHubInfo-ApacheSpark` has no files for issues. That's because the Apache Spark project doesn't use GitHub for their issue tracking.)

## The GitHub personal access token
Click [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to read about setting up a personal access token.
