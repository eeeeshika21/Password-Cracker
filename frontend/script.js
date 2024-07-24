document.getElementById('cracker-form').addEventListener('submit', async function(e) {
    e.preventDefault(); // Prevent form from submitting the traditional way

    const hash = document.getElementById('password-hash').value;
    const attackType = document.getElementById('attack-type').value;

    // Send a POST request to the backend with the hash and attack type
    const response = await fetch('http://localhost:5000/crack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ hash, attackType }),
    });

    if (response.ok) {
        const result = await response.json();
        document.getElementById('result').textContent = result.password || 'Password not found';
    } else {
        document.getElementById('result').textContent = 'Error: ' + (await response.json()).error;
    }
});
