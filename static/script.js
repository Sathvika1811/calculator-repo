document.getElementById('calc-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    const input1 = document.getElementById('input1').value;
    const input2 = document.getElementById('input2').value;
    const operation = document.getElementById('operation').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input1: parseFloat(input1), input2: parseFloat(input2), operation })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Result: ${data.result}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
