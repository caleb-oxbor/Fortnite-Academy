document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from the backend
    fetch('/player_stats')
    .then(response => response.json())
    .then(data => {
        console.log(data);

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
