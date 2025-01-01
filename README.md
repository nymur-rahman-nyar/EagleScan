# Cybersecurity Target Analysis Tool
![demo_eaglescan-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/a3a6d40b-b54c-42b8-a99c-80d2c4ee12bd)

## Overview
This project is a **Cybersecurity Target Analysis Tool** designed to gather and generate comprehensive reports about a target URL. It integrates multiple tools and functionalities, including domain analysis, network mapping, IP discovery, and more. The output is saved as a structured report, making it an essential tool for penetration testers and cybersecurity enthusiasts.

## Features
- **Directory Management**: Automatically creates directories for storing reports.
- **Top-Level Domain (TLD) Analysis**: Extracts the top-level domain of the target URL.
- **IP Address Retrieval**: Fetches the IP address associated with the domain.
- **Nmap Scanning**: Performs a fast nmap scan (`-F` flag) to gather details about open ports and services.
- **Robots.txt Retrieval**: Fetches and analyzes the `robots.txt` file of the target website.
- **WHOIS Lookup**: Retrieves WHOIS information for the domain.

## Technologies Used
- **Python 3.6+**
- **Libraries**:
  - `tld`: For extracting top-level domains.
  - `fpdf`: For generating PDF reports.
  - `urllib`: For making HTTP requests.
- **Tools**:
  - `nmap`: Network mapper for scanning IPs and services.
  - `whois`: For gathering public domain registration data.

## Requirements
1. **Python Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install tld fpdf
