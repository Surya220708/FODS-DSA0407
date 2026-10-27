
import pandas as pd

property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Chennai', 'Madurai', 'Chennai',
                 'Coimbatore', 'Madurai'],
    'bedrooms': [3, 5, 4, 6, 5],
    'area': [1500, 2500, 2000, 3000, 2800],
    'listing_price': [4000000, 6000000, 5000000,
                      7500000, 6500000]
})

print("Average Listing Price by Location:")
print(property_data.groupby('location')
      ['listing_price'].mean())

count = (property_data['bedrooms'] > 4).sum()
print("\nProperties with more than 4 bedrooms:", count)

largest = property_data.loc[property_data['area'].idxmax()]

print("\nProperty with Largest Area:")
print(largest)
