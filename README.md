# My Personal Portfolio Website

Welcome to my personal portfolio website! This project showcases my skills, projects, and experience as a web developer, focusing on backend engineering using Python, Flask, HTML, CSS, Boostrap and little of JavaScript.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Responsive Design](#responsive-design)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This is a work-in-progress portfolio website designed to showcase my web development skills. The website features various sections, including an introduction, project showcases, a contact form, and more. The primary goal of this project is to create an engaging and visually appealing portfolio that reflects my skills as a web developer and backend engineer.

## Features

- **Responsive Design**: The website is designed to be fully responsive, adapting to various screen sizes, from mobile phones to large desktop monitors.
- **Dynamic Project Showcase**: Displays a flexible number of project images and descriptions, ensuring each project is presented beautifully.
- **Google Analytics**: Implements a google analysis to check the stat of visit to websites.
- **Data Receival**: Users can reach out to the admin of the website and receive prompt response after.
- **Personal Information**: The about section of this projects gives concrete information of the admin and skills.

## Technologies Used

- **Frontend**:
  - HTML5, CSS3
  - JavaScript (for interactive features and animations)
- **Backend**:
  - Python (Flask framework)
  - CSV (Database management)
- **Version Control**:
  - Git, GitHub
- **Design and Assets**:
  - Custom fonts and images
  - Responsive layout and CSS animations

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/portfolio-website.git
   cd portfolio-website
   ```

2. **Create a Virtual Environment and Activate** (optional but recommended):

   ```bash/macos/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

   ```Windows
   py -3 -m venv .venv
   source venv/Scipts/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Development Server**:

   ```bash
   flask --app server run --debug --port=5000
   ```

5. **View the Website**:
   Open your web browser and navigate to `http://localhost:5000` or `http://<your-IP-address>:5000` to view it on another device.

## Usage

This project serves as both a portfolio and a showcase of my web development skills. It includes detailed examples of my work, as well as interactive elements that demonstrate my proficiency in various technologies. Feel free to explore the codebase and adapt it to your own needs.

### Accessing the Website on Mobile Devices

To access the website on a mobile device:

- Ensure your mobile device and development server are on the same local network.
- Enter `http://<your-IP-address>:5000` in your mobile browser.

## Project Structure

```plaintext
portfolio-website/
│
├── static/
│   ├── style.css/
│   ├── script.js/
│   ├── main.css/
│   └── assets
|        ├── favicon.ico
|        ├── images
|              ├── Work (001-006)
│
├── templates/
│   ├── index.html
│   ├── work.html
│   ├── register.html
│   ├── thank-you.html
|   ├── works.html
|   ├── contact.html
│
├── server.py
├── requirements.txt
└── README.md
``'

```
