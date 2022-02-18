from datetime import datetime
from typing import List
import helpers

def link(url, text=None):
    text = text if text else url
    return "<a href=" + url + ">" + text + "</a>"


def style():
    return \
        "<style>" + \
            "table, th, td {" + \
            "border: 1px solid black;" + \
            "border-collapse: collapse;}" + \
            "table {margin-left:auto;margin-right:auto;}" + \
        "</style>"

def tableHeadings():
    return \
         "<tr>" + \
            "<th>#</th>" + \
            "<th>Created</th>" + \
            "<th>Flair</th>" + \
            "<th>Title</th>" + \
            "<th>Reddit URL</th>" + \
            "<th>Website URL</th>" + \
         "</tr>"

def bodyBeforeTable():
    return "Scrapped on: " + datetime.now().strftime("%Y.%m.%d %H:%M:%S")

def tableRow(count: int, submission):
    return \
        "<tr>" + \
            "<td>" + str(count) + "</td>" + \
            "<td>" + helpers.get_nice_time(submission.created_utc) + "</td>" + \
            "<td>" + str(submission.link_flair_text) + "</td>" + \
            "<td>" + submission.title + "</td>" + \
            "<td>" + link("https://www.reddit.com" + submission.permalink) + "</td>" + \
            "<td>" + link(submission.url) + "</td>" + \
        "</tr>"

def createTable(content: List):
    ret = "<!DOCTYPE html><html><head>" + style() + "</head><body>" + bodyBeforeTable() + "<table>" + tableHeadings()
    count = 0
    for sub in content:
        count += 1
        ret += tableRow(count, sub)
    return ret + "</table></body></html>"
