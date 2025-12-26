from playwright.sync_api import sync_playwright

def fetch_with_real_edge(url):
    edge_path = "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="/mnt/c/Users/tarci/AppData/Local/Microsoft/Edge/User Data/Default",
            executable_path=edge_path,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ]
        )

        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
        return html

if __name__ == "__main__":
    url = 'https://www.zara.com/mt/en/technical-hooded-jacket-p04695500.html'
    html_content = fetch_with_real_edge(url)
    
    if html_content:
        print("\n--- HTML CONTENT START ---\n")
        print(html_content)
        print("\n--- HTML CONTENT END ---\n")
