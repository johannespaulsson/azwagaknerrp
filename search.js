// Sökfunktion för Kebabylon Wiki
(function() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (!searchInput || !searchResults) return;

    function performSearch() {
        const query = searchInput.value.toLowerCase().trim();
        searchResults.innerHTML = '';
        
        if (query.length < 2) {
            searchResults.style.display = 'none';
            return;
        }

        // Kontrollera om searchData finns (laddas från search_data.js)
        if (typeof searchData === 'undefined') {
            console.error('Search data not loaded');
            return;
        }

        // Avgör sökväg (om vi är i en undermapp)
        const isSubfolder = window.location.pathname.includes('/characters/') || window.location.pathname.includes('/chapters/');
        const prefix = isSubfolder ? '../' : '';

        const matches = searchData.filter(item => {
            const inTitle = item.title.toLowerCase().includes(query);
            const inTags = item.tags && item.tags.some(tag => tag.toLowerCase().includes(query));
            const inType = item.type.toLowerCase().includes(query);
            return inTitle || inTags || inType;
        }).slice(0, 10);

        if (matches.length > 0) {
            matches.forEach(match => {
                const div = document.createElement('div');
                div.className = 'search-result-item';
                
                // Om länken redan innehåller mappen (t.ex. 'characters/'), lägg bara på prefix
                const finalUrl = prefix + match.url;
                
                div.innerHTML = `<a href="${finalUrl}" style="color: #ffcc00; text-decoration: none; display: block; padding: 10px; border-bottom: 1px solid #444;">
                    <span style="font-weight: bold;">${match.title}</span><br>
                    <small style="color: #888; text-transform: uppercase; font-size: 0.7em;">${match.type}</small>
                </a>`;
                searchResults.appendChild(div);
            });
            searchResults.style.display = 'block';
        } else {
            const div = document.createElement('div');
            div.className = 'search-result-item';
            div.style.padding = '10px';
            div.style.color = '#666';
            div.innerText = 'Inga träffar i arkivet...';
            searchResults.appendChild(div);
            searchResults.style.display = 'block';
        }
    }

    searchInput.addEventListener('input', performSearch);
    searchInput.addEventListener('focus', () => {
        if (searchInput.value.length >= 2) searchResults.style.display = 'block';
    });

    // Stäng resultat vid klick utanför
    document.addEventListener('click', (e) => {
        if (e.target !== searchInput && e.target !== searchResults) {
            searchResults.style.display = 'none';
        }
    });
})();
