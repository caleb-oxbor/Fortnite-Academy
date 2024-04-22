document.addEventListener('DOMContentLoaded', function() {
    // Get the value of the username input field
    //var usernameInput = document.getElementById('username');
    //var username = usernameInput.value;
    // Fetch data from the backend
    fetch('/player_stats', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        //body: JSON.stringify({ username: username }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data received from server:', data); // Log the data object

        if (!Array.isArray(data)) {
            console.error('Data received is not an array.');
            return;
        }

        // Check the type of each element in the array
        data.forEach((element, index) => {
            if (typeof element !== 'object') {
                console.error(`Element at index ${index} is not an object.`);
            }
        });

        const soloStatsData = data.find(dataset => dataset.label === 'solo_kd');
        if (!soloStatsData) {
            console.error('Solo stats data not found');
            return;
        }

        // Create a new Chart
        var ctx = document.getElementById('barchart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: soloStatsData.data.labels,
                datasets: [{
                    label: 'My Dataset',
                    data: soloStatsData.data.values,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});
