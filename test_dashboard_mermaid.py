def test_dashboard_mermaid():
    with open("dashboard.md") as f:
        md = f.read()
    assert "```mermaid" in md and "graph TD" in md
