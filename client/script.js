document.addEventListener('DOMContentLoaded', function() {
  // Add event listener to search button
  document.getElementById('search').addEventListener('click', function() {
    // Get selected query values
    const year = document.getElementById('year').value;
    const method = document.getElementById('method').value;
    const host = document.getElementById('host').value;
    const facility = document.getElementById('facility').value;

    // Check if any query value is selected
    if (year || method || host || facility) {
      // Perform search and display results
      // performSearch(year, method, host, facility);
      const proxyUrl = 'http://34.234.201.187/';
      const targetUrl = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps+where+default_flag=1&format=csv';
      const apiUrl = proxyUrl + targetUrl;
      fetch(apiUrl, {
        mode: 'cors'
      })
      .then(response => response.blob())
      .then(blob => {
        // Create a FormData object to send the CSV file
        const formData = new FormData();
        formData.append('csvFile', blob, 'data.csv');

        // Pass the CSV data to the server-side endpoint
        fetch('http://localhost:7071/api/csv2json', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(jsonData => {
          // Process the JSON data returned from the server
          console.log(jsonData);
        })
        .catch(error => console.error('Error converting CSV to JSON:', error));
      })
      .catch(error => console.error('Error fetching data:', error));
    } else {
      // Display error message
      document.getElementById('error-message').textContent = 'Please select at least one query value.';
    }
  });

  // Rest of the code...
});
