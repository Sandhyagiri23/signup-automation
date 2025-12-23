# Signup Automation – QA Task

## Overview
This project automates the signup flow for:
https://authorized-partner.vercel.app/

Automation is implemented using Playwright with Python.
The flow is automated until the OTP verification step.

OTP handling is not automated as it requires access to a real phone number and external verification.

## Tech Stack
- Language: Python
- Automation Framework: Playwright (Python)
- Browser: Chromium

## Prerequisites
- Python installed
- Playwright installed

Install dependencies:
pip install playwright
playwright install

## How to Run
1. Clone the repository
2. Navigate to the project directory
3. Run the script:python signup_automation.py

## Test Data
- Dynamic email generation is used to avoid duplicate user errors.
- Phone number used for OTP testing must be valid.