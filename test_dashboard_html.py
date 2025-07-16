def test_dashboard_html_links():
    with open("dashboard.html") as f:
        html = f.read()
    assert "<table" in html and "DOC.md" in html and "GENESIS.md" in html
