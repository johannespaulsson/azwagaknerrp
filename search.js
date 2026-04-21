// searchData is loaded from search_data.js

const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

function performSearch() {
    const query = searchInput.value.toLowerCase();
    searchResults.innerHTML = '';
    
    if (query.length < 2) {
        searchResults.style.display = 'none';
        return;
    }

    // Determine path prefix based on where we are
    const isSubpage = window.location.pathname.includes('/characters/') || window.location.pathname.includes('/chapters/');
    const prefix = isSubpage ? '../' : '';

    const matches = searchData.filter(item => 
        item.title.toLowerCase().includes(query) || 
        (item.tags && item.tags.some(tag => tag.toLowerCase().includes(query)))
    ).slice(0, 10);

    if (matches.length > 0) {
        matches.forEach(match => {
            const div = document.createElement('div');
            div.className = 'search-result-item';
            // Handle special cases for index, kontakt, gdpr which are always in root
            let finalUrl = prefix + match.url;
            if (match.url === 'index.html' || match.url === 'kontakt.html' || match.url === 'gdpr.html' || match.url === 'characters.html' || match.url === 'chapters.html' || match.url === 'locations.html' || match.url === 'artifacts.html') {
                finalUrl = prefix + match.url;
            }
            
            div.innerHTML = `<a href="${finalUrl}">${match.title} <small>(${match.type})</small></a>`;
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
