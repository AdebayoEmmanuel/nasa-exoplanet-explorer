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
      // const apiUrl = `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,ra,dec+from+ps+where+upper(soltype)+like+'%CONF%'+and+pl_masse+between+0.5+and+2.0`;

      // Fetch data from the API
      // const url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,ra,dec+from+ps+where+upper(soltype)+like+%27%CONF%27+and+pl_masse+between+0.5+and+2.0';
      const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
      const targetUrl = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps+where+default_flag=1&format=csv';
      const apiUrl = proxyUrl + targetUrl;
      // fetch(apiUrl, {
      //   mode: 'cors'
      // })
      // .then(response => response.text())
      // .then(data => console.log(data))
      // .catch(error => console.error('Error fetching data:', error));
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

  // Add event listener to clear button
  document.getElementById('clear').addEventListener('click', function() {
    // Clear selected query values
    document.getElementById('year').value = '';
    document.getElementById('method').value = '';
    document.getElementById('host').value = '';
    document.getElementById('facility').value = '';

    // Clear error message
    document.getElementById('error-message').textContent = '';

    // Clear results table
    clearResults();
  });

  // Function to perform search and display results
  function performSearch(year, method, host, facility) {
    // Construct the query string
    const query = `select pl_name,pl_masse,ra,dec from ps where default_flag=1`;
    const queryParams = `&year=${year}&method=${method}&host=${host}&facility=${facility}&format=csv`;

    // Construct the full URL with query parameters
    const apiUrl = `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps+where+default_flag=1&format=csv`;

    // Fetch data from the API
    fetch(apiUrl)
      .then(response => response.text())
      .then(data => displayResults(data))
      .catch(error => console.error('Error fetching data:', error));
  }

  // Function to clear results table
  function clearResults() {
    // Clear results table content
    document.getElementById('results-table').innerHTML = '';
  }

  // // Function to display results in table
  // function displayResults(data) {
  //     // Split the CSV data into rows
  //     const rows = data.trim().split('\n');

  //     // Create table header
  //     const headers = rows[0].split(',');
  //     const tableHeader = `<tr>${headers.map(header => `<th>${header}</th>`).join('')}</tr>`;

  //     // Create table body
  //     const tableBody = rows.slice(1).map(row => {
  //         const columns = row.split(',');
  //         return `<tr>${columns.map(column => `<td>${column}</td>`).join('')}</tr>`;
  //     }).join('');

  //     // Display results in table
  //     document.getElementById('results-table').innerHTML = tableHeader + tableBody;
  // }
});
