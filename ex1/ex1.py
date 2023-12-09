from influxdb_client import Point
import requests
from bs4 import BeautifulSoup
import json
import time

from influxdb_conn import send_data


def scrape_website(url, org):
    start_time = time.time()
    # Initialize variables to store the current page and the last page number
    current_page = 1
    last_page_num = None
    products = []

    while True:
        # Construct the URL for the current page
        current_url = f"{url}?page={current_page}"

        # Send an HTTP request to the current URL
        response = requests.get(current_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all product containers
            product_containers = soup.find_all(class_="product-meta")

            # Iterate through each product container
            for product_container in product_containers:
                # Extract relevant information
                title = (product_container.find(class_="product-title").text.strip()
                    if product_container.find(class_="product-title") else "N/A")

                description = (product_container.find(class_="product-description-short").text.strip()
                    if product_container.find(class_="product-description-short") else "N/A")

                regular_price = ("".join(product_container.find(class_="regular-price").text.split('\u00a0')[0])
                    if product_container.find(class_="regular-price") else "N/A")

                discounted_price = ("".join(product_container.find(class_="price").text.split('\u00a0')[0])
                                    if product_container.find(class_="price") else "N/A")
                # Create a dictionary for each product
                product_data = {
                    "organization": org,
                    "title": title,
                    "description": description,
                    "regular_price": regular_price,
                    "discounted_price": discounted_price
                }

                # Append the product dictionary to the products list
                products.append(product_data)

            # Update the last page number
            last_page = soup.find_all('a', class_='js-search-link')[-2]
            last_page_num = last_page.get_text(
                strip=True) if last_page else None

            # Check if there is a next page
            if last_page_num and current_page < int(last_page_num):
                current_page += 1
                print(f"Moving to page {current_page}...of {last_page_num}")
            else:
                break

        else:
            print(f"Error: Status code {response.status_code}")
            break

    points = []
    for product in products:
        #print("org: " + product["organization"] + "; product: " + product["title"] + "; price: " + product["regular_price"] + "; dic: " + product["discounted_price"])
        point1 = Point(str(product["organization"])).tag("product", str(product["title"])).field("regular_price", float(product["regular_price"].replace(',', '.')))
        point2 = Point(str(product["organization"])).tag("product", str(product["title"])).field("discounted_price", float(product["discounted_price"].replace(',', '.')))
        point2 = Point(str(product["organization"])).tag("product", str(product["title"])).field("description", product["description"])
        points.append(point1)
        points.append(point2)
    send_data(points)

    # with open("agua_data.json", "w") as file:
    #     json.dump(products, file, indent=2)
    #     print('File created with success')

      
def main():
    url_to_scrape = 'https://casapeixoto.pt/6877-natal-2023'
    # url_to_scrape = 'https://casapeixoto.pt/483-agua'
    scrape_website(url_to_scrape, "casapeixoto")

if __name__ == "__main__":
    main()