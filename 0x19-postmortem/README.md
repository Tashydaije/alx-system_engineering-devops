## Postmortem

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

# Task:

Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. 

# Requirements:

Issue Summary (that is often what executives will read) must contain:
* duration of the outage with start and end times (including timezone)
* what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
* what was the root cause

Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
* when was the issue detected
* how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
* actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
* misleading investigation/debugging paths that were taken
* which team/individuals was the incident escalated to
* how the incident was resolved

Root cause and resolution must contain:
* explain in detail what was causing the issue
* explain in detail how the issue was fixed

Corrective and preventative measures must contain:
* what are the things that can be improved/fixed (broadly speaking)
* a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

Be brief and straight to the point, between 400 to 600 words

## Solution

You can find the Postmortem I wrote on this link: [Postportem](https://docs.google.com/document/d/1TV1ADUZrWKgS6346mIvJVOTyx1hSW39AB-5i48Eyaj0/edit?usp=sharing)

This is a second postmortem article that is quite humorous. Serves to catch YOUR attention. Give it a read!
[Humorous Postportem](https://docs.google.com/document/d/1ar0e2qpav4Ed1gYwK4Vru0JfZB7VqOI68jNF1t_ddBw/edit?usp=sharing)
