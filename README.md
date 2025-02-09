<!---
README.md for the `DailyLanguageDose` repository.
-->




<!-- PROJECT INFO -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alexanderblinn/DailyLanguageDose">
    <img src="app/img/logo.jpeg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Daily Language Dose</h3>

  <p align="center">
    Daily Language Dose is a tool designed to help you learn
    and practice a new language daily by sending you mails with vocabulary.
    <br />
    <a href="https://github.com/alexanderblinn/DailyLanguageDose/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alexanderblinn/DailyLanguageDose/blob/main/README.md">View Demo</a>
    ·
    <a href="https://github.com/alexanderblinn/DailyLanguageDose/issues">Report Bug</a>
    ·
    <a href="https://github.com/alexanderblinn/DailyLanguageDose/issues">Request Feature</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project
Daily Language Dose is an tool designed to facilitate daily language learning and practice. The module extracts vocabulary, pronunciation, translations, and example sentences from a text file, which can be easily updated. This curated content is then delivered via email. The system can be seamlessly automated using cron jobs on Ubuntu servers, Task Scheduler on Windows, or launchd on macOS to ensure timely delivery of daily or more frequent emails. The email template features a retro design.

<p align="center">
  <img src="img/email.jpg" alt="Email Template" width="200">
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

To get started, create `params.py` in `/app/conf/` and add your credentials and email settings, e.g.,
  ```python
  # params.py

  # SMTP server settings
  SMTP_SERVER = "mail.gmx.net"
  SMTP_PORT = 465
  USERNAME = "your username"
  PASSWORD = "your password"

  # Sender email address
  FROM_ADDR = "your_email@example.com"

  # List of recipient email addresses
  TO_ADDRS = [
    "email@example.com",
    "another_email@example.com"
  ]

  # Email subject
  SUBJECT = "Your Daily Language Dose"

  # Absolute path to the text file containing translations
  PATH = "/home/user/DailyLanguageDose/app/conf/translations.txt"
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Project Link: [https://github.com/alexanderblinn/DailyLanguageDose](https://github.com/alexanderblinn/DailyLanguageDose)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alexanderblinn/DailyLanguageDose.svg?style=for-the-badge
[contributors-url]: https://github.com/alexanderblinn/DailyLanguageDose/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alexanderblinn/DailyLanguageDose.svg?style=for-the-badge
[forks-url]: https://github.com/alexanderblinn/DailyLanguageDose/network/members
[stars-shield]: https://img.shields.io/github/stars/alexanderblinn/DailyLanguageDose.svg?style=for-the-badge
[stars-url]: https://github.com/alexanderblinn/DailyLanguageDose/stargazers
[issues-shield]: https://img.shields.io/github/issues/alexanderblinn/DailyLanguageDose.svg?style=for-the-badge
[issues-url]: https://github.com/alexanderblinn/DailyLanguageDose/issues
[license-shield]: https://img.shields.io/github/license/alexanderblinn/DailyLanguageDose.svg?style=for-the-badge
[license-url]: https://github.com/alexanderblinn/DailyLanguageDose/blob/main/LICENSE
