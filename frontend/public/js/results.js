const resultContainer = document.getElementById('result-container');

async function displayResults() {
    const response = await fetch('/results');

    if (response.ok) {
        const data = await response.json();
        resultContainer.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } else {
        resultContainer.innerHTML = '<p>Error retrieving results</p>';
    }
}

displayResults();
