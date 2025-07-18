def test_benchmarks_section_present():
    """Vérifie que la section Benchmarks et les éléments clés existent dans le dashboard."""
    with open('dashboard/dashboard.html', encoding='utf-8') as f:
        html = f.read()
    assert 'Benchmarks IA' in html
    assert 'id="benchmarks-section"' in html
    assert 'id="benchmarksTable"' in html
    assert 'id="benchmarksChart"' in html
    assert 'id="scoreChart"' in html
    assert 'id="memChart"' in html 