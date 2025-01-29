## **Web Scraping with `httpx` and `BeautifulSoup`**

### **Objective:**
- Learn how to fetch web content using Python.
- Extract and parse useful information from HTML.
- Fetch and work with JSON APIs.
- Understand ethical and legal considerations of web scraping.

---

### **1. pip install Dependencies**

**Teacher Notes:**
- Explain that we need specific libraries to handle web scraping.
- `httpx` is used instead of `requests` because it provides **HTTP/2 support, better async handling, and improved connection management**.
- Show how to install dependencies.
- Emphasize the importance of using a virtual environment.

**Code Example:**
```bash
pip install httpx beautifulsoup4
```

---

### **2. Fetching JSON Data from APIs**
> Before scraping HTML, we should first understand how to work with JSON-based APIs, which often provide structured data directly.

**Teacher Notes:**
- Explain that many websites provide APIs to retrieve structured data in JSON format.
- Show how to fetch and parse JSON using `httpx`.
- Demonstrate error handling and response validation.

**Code Example:**
```python
import httpx

# Example JSON API (Public API)
url = "https://jsonplaceholder.typicode.com/posts/1"

response = httpx.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
```

🔹 **Why `httpx`?**
- Supports **HTTP/2** (`requests` does not).
- **Timeouts and error handling** are more robust.

---

### **3. Fetching HTML Content with `httpx`**

**Teacher Notes:**
- Explain that `httpx.get()` retrieves web pages.
- Highlight common HTTP response codes (e.g., `200 OK`, `404 Not Found`).
- Emphasize checking `robots.txt` before scraping.

**Code Example:**
```python
import httpx

# URL to scrape
url = "https://example.com"

# Fetching the content
response = httpx.get(url)

# Checking status code
if response.status_code == 200:
    print("Page fetched successfully!")
    print(response.text[:500])  # Print the first 500 characters of the page content
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
```

---

### **4. Parsing HTML with BeautifulSoup**

**Teacher Notes:**
- `BeautifulSoup` is used to extract information from HTML.
- Show how to find elements (`title`, `h1`, `a` links).
- Explain how `find()` and `find_all()` work.

**Code Example:**
```python
from bs4 import BeautifulSoup

# Example HTML content (use response.text in a real case)
html_content = """
<html>
    <head><title>Example Page</title></head>
    <body>
        <h1>Welcome to Example.com</h1>
        <p>This is a paragraph of text.</p>
        <a href="https://example.com/page2">Link to Page 2</a>
    </body>
</html>
"""

# Parsing the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract the title
title = soup.title.string
print(f"Page Title: {title}")

# Extract the first <h1> tag
h1_text = soup.find("h1").text
print(f"H1 Text: {h1_text}")

# Extract all links
links = soup.find_all("a")
for link in links:
    print(f"Link: {link['href']}")
```
---

### **5. Respecting Robots.txt and Terms of Service**
> Scraping must be done ethically and legally.

**Teacher Notes:**
- Explain `robots.txt` and why websites use it.
- Show how to check a site’s `robots.txt`.
- Encourage students to **check Terms of Service** before scraping.

**Code Example:**
```python
import httpx

# Checking robots.txt
robots_url = "https://example.com/robots.txt"

response = httpx.get(robots_url)
if response.status_code == 200:
    print("robots.txt:")
    print(response.text)
else:
    print("robots.txt not found!")
```

---

### **Summary: Why Use `httpx` Instead of `requests`?**
| Feature            | `requests` | `httpx` |
|--------------------|-----------|---------|
| Default HTTP Version | HTTP/1.1 | HTTP/1.1 (HTTP/2 optional) |
| Native HTTP/2 Support | ❌ No | ✅ Yes (with `http2=True`) |
| Asynchronous Support | ❌ No | ✅ Yes (`AsyncClient`) |
| Better Connection Handling | ✅ Yes | ✅ Yes (More flexible) |
| Redirect Handling | ✅ Yes | ✅ Yes |

🔹 **When to use `requests`?**  
For simple synchronous HTTP requests where you don’t need HTTP/2 or async capabilities.

🔹 **When to use `httpx`?**  
When you need **HTTP/2, async requests, better error handling, or performance improvements**.

---

### **Lab Exercise**
#### **Objective:**  
Students will practice making `GET` requests to JSON APIs and scraping HTML.

#### **Tasks:**
1. **Fetch JSON Data**  
   - Retrieve data from **SWAPI** (`https://swapi.dev/api/people/1/`) and print the character’s name.
   - Retrieve a list of posts from **Typicode** (`https://jsonplaceholder.typicode.com/posts`) and print the first three titles.

2. **Scrape a Web Page**  
   - Fetch HTML from `example.com` and extract the `<title>`, first `<h1>`, and all `<a>` links.

3. **Check `robots.txt`**  
   - Fetch and display `robots.txt` from `https://example.com`.

