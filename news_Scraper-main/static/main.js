document.addEventListener('DOMContentLoaded', () => {
    fetch('/headlines')
        .then(response => response.json())
        .then(data => {
            const headlinesList = document.querySelector('ul');
            headlinesList.innerHTML = ''; // Clear existing list
            data.headlines.forEach(headline => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = "https://www.bbc.com"; // Fixed URL for all headlines
                a.textContent = headline.text;
                a.target = '_blank';
                a.rel = 'noopener noreferrer';
                li.appendChild(a);
                headlinesList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching headlines:', error));
});