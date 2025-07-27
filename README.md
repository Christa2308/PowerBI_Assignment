
Name: Uwamahoro Christa  

ID: 25869

Link: https://drive.google.com/drive/folders/1YZPujYWeUzXJO8al9nhWNJ6ytKzZyl7s?usp=sharing
 
  # Introduction 
### 1. Data Understanding and Preparation
We load the Uber Fares dataset into a Pandas DataFrame using Python to prepare it for analysis. A DataFrame provides a structured way to store and manipulate tabular data, making it easy to explore, clean the dataset and handle missing values. 
<img width="1041" height="776" alt="codes for clean and missing data" src="https://github.com/user-attachments/assets/cfa7e0fe-bad6-4c49-aeb6-ef20e50d22be" />

It's Output
<img width="1325" height="825" alt="output for clean and missing data" src="https://github.com/user-attachments/assets/573f9030-7ff7-493d-bd34-6c9c599c764b" />

### 2. Exploratory Data Analysis (EDA)
We then perform Exploratory Data Analysis (EDA) to gain an initial understanding of the data. EDA helps identify the dataset's structure, dimensions, and variable types, and provides insight into the quality of the data by checking for missing values, duplicates, and inconsistencies. 
<img width="931" height="420" alt="descriptive statistics" src="https://github.com/user-attachments/assets/6605a94e-a1bc-4646-99a5-a7c561f4c196" />

It's Output
<img width="1214" height="454" alt="output for descriptive statistics" src="https://github.com/user-attachments/assets/47ca56f1-ee7b-4eef-98b0-548e174c5e8a" />

The following is a visualization showing fare distribution patterns
<img width="800" height="500" alt="Fare distribution" src="https://github.com/user-attachments/assets/6715c0fa-fd18-4cb8-8a88-6c41675a2d26" />

### 3. Feature Engineering 
We enhance the Uber Fares dataset by creating new analytical features that provide deeper insights into ride patterns. From the pickup timestamp, we extract hour, day, and month, categorize rides by day of the week, and create a peak/off‑peak time indicator to distinguish busy travel periods 
<img width="831" height="343" alt="new analytic features" src="https://github.com/user-attachments/assets/e09e9011-41ec-4687-be08-340b2d505808" />

It's Output
<img width="634" height="315" alt="output for new analytical features" src="https://github.com/user-attachments/assets/046d69e0-67ed-4a1c-aead-dbe7bfd04f82" />

After feature creation, we identify and encode categorical variables (such as day of week, month, and peak time) to make the dataset ready for analysis and visualization in Power BI. 
<img width="1313" height="323" alt="Identify and properly encode categorical variables" src="https://github.com/user-attachments/assets/26981e3f-15ed-4803-a1a4-771b7654b225" />

It's Output
<img width="1557" height="296" alt="output for Identify and properly encode categorical variables" src="https://github.com/user-attachments/assets/9ce65526-cd4d-422c-bb6e-e781f7625194" />

### 4. Data Analysis in Power BI and Dashboard Creation in Power BI
In this stage, we use Power BI Desktop to analyze and visualize the enhanced Uber Fares dataset. The cleaned dataset is imported into Power BI to create interactive and professional dashboards that provide insights into ride and fare patterns.
<img width="1102" height="886" alt="import dataset in PBI" src="https://github.com/user-attachments/assets/2e8519ae-c63f-4b84-a503-deb7843380dd" />

This dashboard provides a comprehensive overview of Uber ride and fare patterns with key metrics and visualizations:
 <img width="1072" height="667" alt="Overview" src="https://github.com/user-attachments/assets/092d3e48-4d86-4d9e-9f8e-084c47291a24" />

 Visualizations
1. Donut Charts 
Average Fare by Hour – Shows average fare distribution across different hours. 
Average Fare by Month – Shows fare variation across months.
2. Area Chart 
Ride Count by Day – Displays daily ride trends for the month, showing peak and off-peak demand.
3. Table – Days of the Week Analysis 
Displays day_of_week, Average Fare, Average Fare by Peak, Ride Count, and Total Fare Amount.
<img width="1057" height="538" alt="Visualization donut" src="https://github.com/user-attachments/assets/4bee4a6b-072d-4ed6-b179-53137c712c2a" />

4. Box & Whisker Chart 
Total Fare Amount by Hour and Year – Shows fare distribution patterns over multiple years, highlighting variability and outliers.
 <img width="492" height="264" alt="Box plot" src="https://github.com/user-attachments/assets/2ce4274d-3c8b-4715-8349-0e2b7d0fe054" />
 
RideCount by Hour and Year (Left Chart) 
What It Shows: 
Distribution of ride counts per hour across different years (2009–2015). 
Box: Represents interquartile range (middle 50% of data). 
Whiskers: Show min and max ride counts. 
Dots: Represent individual data points (hourly ride counts).

AverageFareByPeak by Hour and Year (Right Chart) 
What It Shows: 
Average fares (during peak times) by hour across years (2009–2015). 
The box shows fare variations, median, and outliers.
<img width="1067" height="329" alt="box plot 2" src="https://github.com/user-attachments/assets/e36a4059-2cdd-4d51-8b60-ec280e4e5d52" />

Histogram with Scatter Overlay
X-Axis (fare_amount and bins): Fare amounts grouped into bins. 
Y-Axis (Histogram Count): Number of trips within each fare bin. 
Green Bars: Show how many rides fall into each fare range.
<img width="514" height="322" alt="histogram" src="https://github.com/user-attachments/assets/9bb79d7b-ed82-4d90-adfb-c4903d9d69a9" />

