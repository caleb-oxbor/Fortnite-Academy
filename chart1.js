document.addEventListener('DOMContentLoaded', function() {
    fetch('/player_stats', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'username=' + encodeURIComponent('YourUsernameHere')
    })
    .then(response => response.json())
    .then(data => {
        const soloKdData = data.find(dataset => dataset.label === 'Solo KD');
        if (!soloKdData) {
            console.error('Solo KD data not found');
            return;
        }

        var ctx = document.getElementById('barchart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: soloKdData.data.labels,
                datasets: [{
                    label: 'KD Comparison',
                    data: soloKdData.data.values,
                    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
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