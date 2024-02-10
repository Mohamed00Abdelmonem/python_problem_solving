import requests
from bs4 import BeautifulSoup

url = 'https://sa.investing.com/indices/major-indices'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Set a timeout for the request
timeout = 10

try:
    # Make the HTTP request
    response = requests.get(url, headers=headers, timeout=timeout)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing the data you want to scrape
        table = soup.find('table', class_='genTbl closedTbl crossRatesTbl elpTbl')

        if table:
            # Extract data from the table
            rows = table.find_all('tr')
            for row in rows:
                # Assuming the data is in the columns of each row
                columns = row.find_all(['td', 'th'])
                row_data = [column.get_text(strip=True) for column in columns]

                # Process and print or store the data as needed
                print(row_data)
        else:
            print("Table not found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error during the request: {e}")
