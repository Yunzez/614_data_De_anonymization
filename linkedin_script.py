from linkedin_api import Linkedin
from tqdm import tqdm  # For progress bar
# Authenticate using your LinkedIn credentials
api = Linkedin("*", "*", refresh_cookies=True)
my_profile = api.get_profile(public_id="zichaocentral")
# The geo_urn_id for Carnation, WA
geo_urn_id = "102610354"
# Search for people in Carnation, WA
search_results = api.search_people(
    regions=[geo_urn_id],
    limit=5000
)
# Function to check if a school is in New York state
def is_school_in_new_york(school_name):
    # List of keywords to identify New York schools
    ny_school_keywords = [
        "New York University", "NYU", "Columbia University", "Cornell University",
        "Syracuse University", "University at Buffalo", "University of Rochester",
        "Rochester Institute of Technology", "Stony Brook University", "Fordham University"
    ]
    return any(keyword.lower() in school_name.lower() for keyword in ny_school_keywords)
# Function to check if a location is in New York state
def is_location_in_new_york(location):
    return "New York" in location or "NY" in location
# List to store filtered profiles
filtered_profiles = []
# Iterate over search results with a progress bar
for person in tqdm(search_results, desc="Processing Profiles"):
    try:
        # Fetch the full profile using urn_id
        profile = api.get_profile(urn_id=person['urn_id'])
        went_to_ny_school = False
        used_to_be_in_ny = False
        # Check education history
        if 'education' in profile:
            for edu in profile['education']:
                school_name = edu.get('schoolName', '')
                if is_school_in_new_york(school_name):
                    went_to_ny_school = True
                    break
        # Check past experience locations
        if 'experience' in profile:
            for exp in profile['experience']:
                location = exp.get('locationName', '')
                if is_location_in_new_york(location):
                    used_to_be_in_ny = True
                    break
        # Add profile to list if criteria are met
        if went_to_ny_school or used_to_be_in_ny:
            filtered_profiles.append(profile)
    except Exception as e:
        print(f"Error processing profile {person['urn_id']}: {e}")
# Print the filtered profiles
print(filtered_profiles)