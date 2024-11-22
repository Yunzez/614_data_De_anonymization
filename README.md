# 614_data_De_anonymization

## what did we do (motivations):
As we learned from the [How To Break Anonymity of the Netflix Prize Dataset](https://arxiv.org/abs/cs/0610105) paper, data anonymity can be broken easily if the data are not treated carefully. Now 17 years has passed, we wonder if this is still true. 
We focus on two major open dataset website [New York State Open Data](https://data.ny.gov/), and [Washington State Open Data](https://data.wa.gov/), as they both claimed to have achieved data anonymity.

we will focus on people who moved from New York State to Washington state King Country, between 2023/1/1 to 2025/1/1, we try to correlate these datasets to increase the possibility of identifying each potentiall individuals. 

### why did we choose NYS to WA
because NYS and WA keep very detailed records of their license transfer and car registration, giving us some opportunities to do some exploration 

## data source:
[New York State Driver License, Permit, and Non-Driver Identification Cards Issued](https://data.ny.gov/Transportation/Driver-License-Permit-and-Non-Driver-Identificatio/a4s2-d9tt/about_data),
Data columns: #todo: fill this out 
we filtered by: 
- between 2023 to 2024, 
- Only out of state resident
- Only resident in WA, King County
- The license status has to be surrendered, meaning that the residents have moved out and claimed another driver license in the another state
- Only drivers license, we exclude all the ID 
- we added Year of Issue, knowing that NYS driver license are valid for 8 years, we added an Estimated Year of Move, which we assume at least 1 year before their license expire

[Driver Licenses and ID Cards Transferred to Washington](https://data.wa.gov/demographics/Driver-Licenses-and-ID-Cards-Transferred-to-Washin/769e-73q6/about_data)
Data columns: #todo: fill this out 
we filtered by: 
- between 2023 to 2024, 
- Only Driver License,
- Only from New York State

[Washington State Vehicle Registration Transactions by Department of Licensing](https://data.wa.gov/Transportation/Vehicle-Registration-Transactions-by-Department-of/brw6-jymh/about_data)
Data columns: #todo: fill this out 
we filtered by: 
- between 2023 to 2024,
- Vehicle Type is not MOTORCYCLE,
- Vehicle Primary Use is Passenger Vehicle
- Only in King County
- Owner Type is only Individual Owner
- Transaction Type is "Original Registration" (Buying a new car) or "Registration at time of Transfer" (Buying a second handed car)
- we added City names based on postal code, reference: (https://worldpopulationreview.com/zips/washington/king-county) so we can cross reference other data

## our reasoning for the filtering
1. we narrow down our search to 2023 to 2024 so it's less data for us to process
2. we picked king county because it has the largest number of data, it's harder to pinpoint people, leaving some safety space for ethical reasons, if we want to identify people easier, we can aim for counties that are less popular 
3. we only picked license records in NYS that are surrendered since there are already new records being documented in Washington state, meaning them has transfered their license 
4. to prove our attack works, we aim to find the resident that moved to Carnation, King County from New York State, there are two records showing that these two individuals transfer their ID

```markdown
| Year of Birth | Sex | City      | State | Zip  | Residence County | License Class | Status     | Privilege | Year of Expiration |
|---------------|-----|-----------|-------|------|------------------|---------------|------------|-----------|--------------------|
| 1995          | F   | CARNATION | WA    | 98014| OUT-OF-STATE     | D             | SURRENDERED| FULL      | 2024               |
| 1996          | F   | CARNATION | WA    | 98014| OUT-OF-STATE     | D             | SURRENDERED| FULL      | 2027               |
```

```markdown
then, we utilize the car transaction data trying to correlate what car they may have purchased around this time:

| Make           | Count |
|----------------|-------|
| TOYOTA         | 129   |
| SUBARU         | 106   |
| HONDA          | 69    |
| FORD           | 65    |
| CHEVROLET      | 63    |
| TESLA          | 56    |
| JEEP           | 40    |
| KIA            | 40    |
| NISSAN         | 37    |
| BMW            | 35    |
| MAZDA          | 34    |
```

Driver Licenses and ID Cards Transferred to Washington has became not helpful as they are extremly generic and hard to link to identifiable information even based on assumptions. You can see in the dataset named DriverIDWash_2023_2024_NewYork_in_King.csv

### **What We Can Infer About the Two Individuals**
1. **Demographics**:
   - Both are females born in 1995 and 1996, making them 27–28 years old.
   - They now reside in **Carnation**, King County, and likely hold Washington State licenses after surrendering their NYS licenses.

2. **Vehicle Ownership**:
   - Based on Carnation’s vehicle registration data, they likely drive popular makes like **Toyota**, **Subaru**, or **Honda**.
   - If they own less common makes (e.g., BMW, Tesla), they would stand out more in the data.

3. **Vehicle Characteristics**:
   - Likely practical cars like sedans (e.g., Toyota Corolla) or SUVs (e.g., Subaru Outback), suited for suburban/rural living.
   - Vehicles likely registered in 2023–2024.

4. **Move Timeline**:
   - Their license surrender aligns with vehicle registrations in 2023–2024, suggesting they moved and registered vehicles during this period.

---

## We did find one individual that might potentially matches this creteria of birth year, sex, and moving pattern through linkedin and X(twitter) after a very time consuming search, but we will not disclose their identity here.

## **What to Do Next (Hypothetical Exploration)**
To further the exploration and enhance the de-anonymization attack, leveraging external data sources could provide additional insights. However, due to ethical concerns, we will not proceed with pinpointing any individuals. Hypothetically, the following steps could be taken if ethical and legal permissions were obtained:

---

### **1. Utilize Social Media APIs**
- **Platforms**: APIs from platforms like Reddit, Facebook, Instagram, or X (Twitter) could help link behavioral patterns to individuals.
- **Approach**:
  - Search for public posts or accounts mentioning **moving to Washington** or specifically **Carnation, King County**.
  - Filter results using demographics (e.g., `Year of Birth`, `Sex`, and `City`) inferred from the datasets.
  - Look for patterns in content, such as posts about surrendering NY licenses, registering vehicles, or moving experiences.

### **2. Public Data Sources**
- **Real Estate Records**:
  - Use publicly available property records to find new homeowners in Carnation who match the inferred demographic profile.
  - Cross-reference purchase dates with the timeframe of license surrender.
- **Voter Registration**:
  - If voter registration data is public in Washington, it could help match individuals by `Year of Birth`, `Sex`, and `ZIP Code`.
- **Local News or Community Forums**:
  - Search local news, community bulletins, or forums for people sharing their relocation stories.

### **3. Behavioral Correlation**
- Combine vehicle registration data with social media activity:
  - Look for mentions of specific vehicles (e.g., "Just bought a Toyota RAV4!") in public posts.
  - Cross-match demographic and geographic details from the datasets with online content.

### **4. Advanced Techniques**
- **Network Analysis**:
  - Create a bipartite graph linking datasets with social media accounts or other auxiliary data.
  - Identify clusters where the same attributes appear across multiple datasets.
- **Image Analysis**:
  - If vehicle images are public (e.g., in social media posts), use AI tools to identify car models and colors matching the registration data.

### **5. Ethical and Legal Considerations**
- **Consent**:
  - Ensure all data collection aligns with ethical guidelines and legal frameworks.
- **Privacy Awareness**:
  - Emphasize the risks of cross-referencing public and private datasets.
- **Educational Purpose**:
  - Focus on showcasing vulnerabilities in anonymization methods rather than targeting individuals.

---

### **Final Decision**
We will stop the exploration here due to ethical concerns. This exercise highlights the potential privacy risks when combining seemingly anonymized datasets with auxiliary information. It also underscores the need for stricter data anonymization standards and responsible data usage. 

Let me know if you'd like assistance with ethical data analysis approaches or privacy-preserving techniques. 🚀