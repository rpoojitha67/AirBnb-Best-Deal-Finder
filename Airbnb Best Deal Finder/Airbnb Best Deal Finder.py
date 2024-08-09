import pandas as pd

# Load the dataset using raw string notation
data = pd.read_csv(r"C:\Users\pooji\Desktop\airbnb.csv")

# Function to filter listings by location
def filter_listings_by_location(data, location):
    location = location.lower()
    filtered_data = data[data['State'].str.lower() == location]
    return filtered_data

# Function to filter listings by preferences
def filter_listings_by_preferences(data, min_price, max_price, property_type):
    property_type = property_type.lower()
    filtered_data = data[(data['Listing Price'] >= min_price) &
                         (data['Listing Price'] <= max_price) &
                         (data['Property Type'].str.lower() == property_type)]
    return filtered_data

# Function to sort listings by rating
def sort_listings_by_rating(data):
    sorted_data = data.sort_values(by='Review Score', ascending=False)
    return sorted_data

# Function to get the best deal
def get_best_deal(data, num_results=5):
    best_deals = data.head(num_results)
    return best_deals

# Main function
def main():
    print("Welcome to the Airbnb Best Deal Finder!")
    location = input("Enter your preferred state: ")
    min_price = float(input("Enter the minimum price (per night): "))
    max_price = float(input("Enter the maximum price (per night): "))
    property_type = input("Enter the preferred property type (e.g., Apartment, House, etc.): ")

    print(f"Location: {location}, Min Price: {min_price}, Max Price: {max_price}, Property Type: {property_type}")

    filtered_data = filter_listings_by_location(data, location)
    print("Filtered Data by Location:")
    print(filtered_data)

    if filtered_data.empty:
        print("No listings found for the specified location.")
        return

    filtered_data = filter_listings_by_preferences(filtered_data, min_price, max_price, property_type)
    print("Filtered Data with Preferences:")
    print(filtered_data)

    if filtered_data.empty:
        print("Sorry, no matching listings found for your preferences.")
    else:
        sorted_data = sort_listings_by_rating(filtered_data)
        best_deals = get_best_deal(sorted_data)
        print("Top 5 Best Deals in your preferred location:")
        print(best_deals)

if __name__ == "__main__":
    main()

