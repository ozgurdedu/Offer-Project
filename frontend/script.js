const apiUrl =  'http://127.0.0.1:8000/api/offers/';

fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP Error! Status : ${response.status}');
        }
        response.json();
    })
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Fetch error: ', error);
    })