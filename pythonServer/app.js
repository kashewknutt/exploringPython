document.getElementById('sendRequest').addEventListener('click', function() {
    const data = { data: 'Sample Data' };

    fetch('http://127.0.0.1:5000/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
