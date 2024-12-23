# 100 Nova

Welcome to the **100 Nova** Challenge! This lab is designed to simulate a static website with hidden flag files, which can be discovered through fuzzing techniques.

Flag format is: `MLA{FLAG}`

## Overview

The website consists of a landing page, a `robots.txt` file, and 100 randomly generated folders with names in hexadecimal format. Each folder may contain a file called `flag.txt`, which contains a secret flag. The goal is to use fuzzing tools (e.g., ffuf) to discover the `flag.txt` file by leveraging the contents of `robots.txt` and brute-forcing the folder names.

This repository provides two scripts to generate the website and its structure:

- **Python Script**: A Python-based solution for generating the site and folders.
- **Bash Script**: A Bash-based solution for generating the site and folders.

## Requirements

- Python 3.x (for Python script)
- Bash (for Bash script)

## Getting Started

### Using the Python Script

1.  Clone this repository:

    ```bash
    git clone https://github.com/mohammadlotfia/MLA.git
    cd MLA/LABs/100Nova_Fuzzing_Lab
    ```

    or just download the Python file:

    ```bash
    wget https://raw.githubusercontent.com/MohammadLotfiA/MLA/refs/heads/main/LABs/100Nova_Fuzzing_Lab/create_lab.py
    ```

2.  Run the Python script to generate the website and folders:

    ```bash
    python3 create_lab.py
    ```

    This will create a `100nova` directory with the following structure:

    ```
    100nova/
    ├── index.html
    ├── robots.txt
    └── [100 random folders]
       └── [flag.txt] (in a random folder)
    ```

3.  The `robots.txt` file contains a list of disallowed folder paths, which can be used to guide fuzzing techniques to find the flag.

4.  Use fuzzing tools like [FFUF](https://github.com/ffuf/ffuf) to discover the `flag.txt` file.

### Using the Bash Script

1.  Clone this repository:

    ```bash
    git clone https://github.com/mohammadlotfia/MLA.git
    cd MLA/LABs/100Nova_Fuzzing_Lab
    ```

    or just download the Bash file:

    ```bash
    wget https://raw.githubusercontent.com/MohammadLotfiA/MLA/refs/heads/main/LABs/100Nova_Fuzzing_Lab/create_lab.sh
    ```

2.  Make the Bash script executable:

    ```bash
    chmod +x create_lab.sh
    ```

3.  Run the Bash script to generate the website and folders:

    ```bash
    ./create_lab.sh
    ```

    Similar to the Python script, this will create a `100nova` directory with the following structure:

    ```
    100nova/
    ├── index.html
    ├── robots.txt
    └── [100 random folders]
       └── [flag.txt] (in a random folder)
    ```

## Host the Site

### Hosting the Website Locally with Python

If you have Python installed, you can easily serve the website locally using Python's built-in HTTP server. Here's how:

1. **Navigate to the `100Nova_Fuzzing_Lab` directory**:
   After running the script to generate the site, go to the directory where the site was created:

   ```bash
   cd 100nova
   ```

2. **Start the Python HTTP server**:
   For Python 3.x, use the following command to start a simple HTTP server on port 8000:

   ```bash
   python3 -m http.server 8000
   ```

   This will serve the files in the `100nova` folder at `http://localhost:8000`.

   Once the server is running, you can access the website at `http://localhost:8000` in your browser.

## Fuzzing the Site

Tutorials are on YouTube channel at [here]().

### Summary

Check the website and its source code. You can see the hint of `flag.txt` as our target. Use any recon (or listing) tool (like [dirbuster](https://www.kali.org/tools/dirbuster/)) to discover the common file names and/or directories via a word-list. From then, you can use fuzzing tools to proceed to finding the flag.

### Detailed Steps

1. **Use `ffuf` to discover common files and directories**:
   Download a common word-list for recon from either here or SecLists (Discovery/Web-Content/common.txt).

   ```bash
   wget https://github.com/MohammadLotfiA/MLA/raw/refs/heads/main/LABs/100Nova_Fuzzing_Lab/common.txt
   ```

2. **Run the `ffuf` and filter the response code 200**:

   ```bash
   ffuf -w common.txt -u http://localhost:8000/FUZZ -mc 200
   ```

   The results hint at a `robots.txt` file.

3. **Download the `robots.txt` file and create a payload**:
   Looking at the `robots.txt` file, there are 100 different folders with the `Disallow` tag.

   Download the `robots.txt` file.

   ```bash
   wget http://localhost:8000/robots.txt
   ```

   And remove the `Disallow` tag. This will be the payload to FUZZ and capture the flag.

   ```bash
   sed 's/Disallow: \///g' robots.txt > payload.txt
   ```

4. **Re run the `ffuf` to find the FLAG**:
   The target is `flag.txt` in one of those folder listed in `robots.txt` file.

   Run the command to find the FLAG.

   ```bash
   ffuf -w payload.txt -u http://localhost:8000/FUZZ/flag.txt -mc 200
   ```

I hope you enjoyed. Happy Hacking, MLA-IT Education (^\_^)
