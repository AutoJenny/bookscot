<script>
    document.addEventListener("DOMContentLoaded", function() {
     fetch(directoriesJsonUrl)
     fetch('{% static "json/directories.json" %}')
        .then(response => response.json())
        .then(directories => {
            const homeSearchInput = document.getElementById('searchInput');
            const homeResultsDiv = document.getElementById('searchResults');
            const homeClearBtn = document.getElementById('searchInputClear');

            const headerSearchInput = document.getElementById('headerSearchInput');
            const headerResultsDiv = document.getElementById('headerSearchResults');
            const headerClearBtn = document.getElementById('headerSearchInputClear');

            function setupSearch(inputElement, resultsDiv, clearBtn) {
                inputElement.addEventListener('input', function(e) {
                    var searchTerm = e.target.value.toLowerCase();
                    if (searchTerm) {
                        var filteredResults = directories.filter(function(dir) {
                            return dir.title.toLowerCase().includes(searchTerm) ||
                                   dir.blurb.toLowerCase().includes(searchTerm);
                        });

                        displayResults(filteredResults, searchTerm, resultsDiv);
                        clearBtn.classList.remove('hidden');
                    } else {
                        resultsDiv.innerHTML = '';
                        resultsDiv.style.display = 'none';
                        clearBtn.classList.add('hidden');
                    }
                });

                clearBtn.addEventListener('click', function() {
                    inputElement.value = '';
                    resultsDiv.innerHTML = '';
                    resultsDiv.style.display = 'none';
                    clearBtn.classList.add('hidden');
                });
            }

            function displayResults(results, searchTerm, resultsDiv) {
                if (results.length > 0) {
                    resultsDiv.style.display = 'block';
                } else {
                    resultsDiv.style.display = 'none';
                }
                resultsDiv.innerHTML = '';

                results.forEach(function(dir) {
                    var link = document.createElement('a');
                    link.className = 'search-result-item';
                    link.href = '/directory/' + dir.id;

                    var titleHighlighted = highlightText(dir.title, searchTerm);
                    var blurbHighlighted = highlightText(dir.blurb, searchTerm);

                    link.innerHTML = '<div>' + titleHighlighted + '</div><div class="blurb">' + blurbHighlighted + '</div>';
                    resultsDiv.appendChild(link);
                });
            }

            function highlightText(text, term) {
                var re = new RegExp('(' + term + ')', 'gi');
                return text.replace(re, '<span class="highlight">$1</span>');
            }

            // Set up both search inputs
            if (homeSearchInput && homeResultsDiv && homeClearBtn) {
                setupSearch(homeSearchInput, homeResultsDiv, homeClearBtn);
            }
            if (headerSearchInput && headerResultsDiv && headerClearBtn) {
                setupSearch(headerSearchInput, headerResultsDiv, headerClearBtn);
            }
        });
});

</script>