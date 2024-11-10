async function fetchWordFrequencies() {
    const url = document.getElementById('urlInput').value;
    const response = await fetch('http://127.0.0.1:5000/api/fetch', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
    });
    const data = await response.json();
    displayFrequencies(data);
}

function displayFrequencies(data) {
    const tableBody = document.getElementById('resultTable').querySelector('tbody');
    tableBody.innerHTML = '';
    data.forEach(entry => {
        const row = `<tr><td>${entry.word}</td><td>${entry.frequency}</td></tr>`;
        tableBody.innerHTML += row;
    });
}
