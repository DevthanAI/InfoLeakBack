const form = document.getElementById('my-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const id = document.getElementById('id-input').value;
    const phone = document.getElementById('phone-input').value;

    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "initial_information": [id, phone] })
    });

    window.location.href = '/results';
});
