Minh Hoang
12/13/2019
Language: Python 3
Instruction Link: https://www.youtube.com/watch?v=Bg9r_yLk7VY

Purpose: This project is to create a program that will check the price of an item on Amazon hourly and will send an email to you if it drops lower than what you are looking for.
There are 2 files:
    scraper.py: The completed sample with a link for a TV to check if the price could drop below $2500.
    scraper01.py:
        inputs from user:
            the link
            the price they want to drop to
            the time they want the program to run
        output: if the price is lower than the price you want, the program will send the link and print "EMAIL SENT".
Requirement:
    1/Download package Requests and bs4.
        _From command line: pip install requests bs4

What I learn:
_First project with Python.
_Scraping information on website using bs4 and requests library.
_How to send an email through coding using smtplib.
