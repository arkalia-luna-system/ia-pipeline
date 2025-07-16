def test_dashboard_monitoring():
    with open("dashboard.html") as f:
        html = f.read()
    assert "Logs récents" in html and "chart.js" in html and "setInterval" in html
