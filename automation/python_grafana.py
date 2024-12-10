from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Login to Grafana
    page.goto('http://localhost:3000')
    page.fill('input[name="user"]', 'admin')
    page.fill('input[name="password"]', 'admin')
    page.click('button[type="submit"]')
    
    # Configure Data Source
    page.click('text="Configuration"')
    page.click('text="Data Sources"')
    page.click('button:has-text("Add data source")')
    page.click('text="MySQL"')
    page.fill('input[name="database"]', 'grafanadb')
    page.fill('input[name="user"]', 'arshdeep')
    page.fill('input[name="password"]', 'arsh123')
    page.click('button:has-text("Save & Test")')
    
    # Create Dashboard
    page.click('text="+"')
    page.click('text="Dashboard"')
    page.click('text="Add new panel"')
    page.click('text="Edit"')
    page.select_option('select[aria-label="Data source select container"]', 'MySQL')
    page.fill('textarea[aria-label="Query editor text area"]', 'SELECT * FROM cpu_metrics')
    page.click('button:has-text("Apply")')
    
    # Add Time Series Visualization
    page.click('text="Visualization"')
    page.click('text="Time series"')
    page.click('button:has-text("Apply")')
    
    # Save Dashboard
    page.click('button:has-text("Save dashboard"')
    page.fill('input[aria-label="Save dashboard title"]', 'CPU Metrics Dashboard')
    page.click('button:has-text("Save"')
    
    # Take Screenshot
    page.screenshot(path='dashboard_screenshot.png')
    
    browser.close()

