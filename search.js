const searchData = []; // Will be populated by the generator

const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

function performSearch() {
    const query = searchInput.value.toLowerCase();
    searchResults.innerHTML = '';
    
    if (query.length < 2) {
        searchResults.style.display = 'none';
        return;
    }

    const matches = searchData.filter(item => 
        item.title.toLowerCase().includes(query) || 
        item.tags.some(tag => tag.toLowerCase().includes(query))
    ).slice(0, 10);

    if (matches.length > 0) {
        matches.forEach(match => {
            const div = document.createElement('div');
            div.className = 'search-result-item';
            div.innerHTML = `<a href="${match.url}">${match.title} <small>(${match.type})</small></a>`;
            searchResults.appendChild(div);
        });
        searchResults.style.display = 'block';
    } else {
        searchResults.style.display = 'none';
    }
}

searchInput.addEventListener('input', performSearch);

// Close results when clicking outside
document.addEventListener('click', (e) => {
    if (e.target !== searchInput) {
        searchResults.style.display = 'none';
    }
});
