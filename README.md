# **ServerSideLab**

This project provides various server-side vulnerabilities for educational and testing purposes. It helps security professionals and developers learn about common server-side issues such as Server-Side Template Injection (SSTI), Server-Side Includes (SSI), Extensible Stylesheet Language Transformations (XSLT) injection, and Server-Side Request Forgery (SSRF).

## **Table of Contents**

- [Introduction](#introduction)
- [Vulnerabilities](#vulnerabilities)
  - [SSTI](#ssti)
  - [SSI](#ssi)
  - [XSLT](#xslt)
  - [SSRF](#ssrf)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **Introduction**

ServerSideLab is a Flask-based web application that demonstrates several common server-side vulnerabilities. It provides a controlled environment where security researchers and developers can practice identifying and exploiting these vulnerabilities safely.

The application includes routes for the following vulnerabilities:

- **SSTI** (Server-Side Template Injection)
- **SSI** (Server-Side Includes)
- **XSLT Injection**
- **SSRF** (Server-Side Request Forgery)

Each vulnerability has its own set of routes for discovery and advanced challenges. The goal is to help users understand how these vulnerabilities work and how to prevent them in real-world applications.

---

## **Vulnerabilities**

### **SSTI** - Server-Side Template Injection
SSTI occurs when an attacker is able to inject template code into a server-side template. This allows them to execute arbitrary code on the server.

- **Discovery**: `/ssti/discovery`
- **Try Hard**: `/ssti/tryhard`

### **SSI** - Server-Side Includes
SSI is a feature that allows dynamic content insertion into static HTML pages. It can be exploited by attackers to include malicious server-side files or execute arbitrary commands on the server.

- **Discovery**: `/ssi/discovery`
- **Try Hard**: `/ssi/tryhard`

### **XSLT** - Extensible Stylesheet Language Transformations Injection
XSLT injection is a form of attack where malicious XSLT is injected into XML data to perform unwanted actions or gain access to sensitive information.

- **Discovery**: `/xslt/discovery`
- **Try Hard**: `/xslt/tryhard`

### **SSRF** - Server-Side Request Forgery
SSRF occurs when an attacker is able to make a server send requests to internal or external resources without authorization. This can lead to data leaks or remote code execution.

- **Discovery**: `/ssrf/discovery`
- **Try Hard**: `/ssrf/tryhard`

---

## **Installation**

Follow these steps to get the project running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ServerSideLab.git
   cd ServerSideLab
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

   The app will start running on `http://127.0.0.1:5000`.

---

## **Usage**

Once the application is running, you can access the following endpoints:

- **SSTI**:
  - `/ssti/discovery`: Learn about SSTI and how it can be exploited.
  - `/ssti/tryhard`: A more challenging SSTI scenario to practice.
  
- **SSI**:
  - `/ssi/discovery`: Discover the basics of SSI vulnerability.
  - `/ssi/tryhard`: Advanced SSI challenge to test your skills.

- **XSLT**:
  - `/xslt/discovery`: Introduction to XSLT injection.
  - `/xslt/tryhard`: More complex XSLT exploitation challenge.

- **SSRF**:
  - `/ssrf/discovery`: Learn about SSRF and its attack vectors.
  - `/ssrf/tryhard`: Test your knowledge on SSRF exploitation.

---

## **Contributing**

Contributions to this project are welcome! If you find any issues, want to suggest improvements, or have new vulnerability types to add, feel free to fork the repository and create a pull request.

### Steps for contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature/your-feature`).
6. Create a pull request.

### Enjoy exploring and securing your web applications! 😎🚀
