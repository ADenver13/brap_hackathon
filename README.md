# Rodent Activity Tracker (R.A.T)

This project was created over the course of a day for [Hacking Injustice @ Harvard](engineeringhope.org).
Presentation slides can be accessed [here](https://docs.google.com/presentation/d/1yxv_SrG5sZYOAOY0Oull5OrrWXExseQXS_oYpUotULE/edit?usp=sharing)

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Data Format](#data-format)
- [Screenshots](#screenshots)
- [License](#license)

### Project Description

This project provides a dashboard template for tracking the rat population in the City of Boston using open-source data. This project is designed to make it easier to add other data sources and create a single source of truth. This includes the other piece of our group's project, tracking sewer rat populations through introducing biomarkers and tracking that in wastewater.

### Features
- Animated Map: View rodent sightings as an animation by month.
- Customizable Map Styles: Choose from a variety of map styles.
- Interactive Map: Zoom, pan, and hover for more information on sightings.
- Filtering: Filter data by month or specific locations.

### Technologies Used
- Plotly: For creating interactive maps and charts.
- Pandas: For data manipulation and analysis.
- Dash: To create an interactive web application for the visualization.

### Installation Instructions
To run the project locally, follow these steps:

- Clone the repository: ```git clone https://github.com/ADenver13/brap_hackathon.git```

Install the required dependencies using pip:

```pip install -r requirements.txt```

### Usage
- To run the project locally, you can use the following command:
```python app.py```
- This will start a local server, and you can access the application in your browser at: http://127.0.0.1:8050/

### Interacting with the Maps
Zoom in and out of the map for detailed views.
Hover over the points to see more information about each sighting.
Animation: The map will update monthly to show how the sightings evolve over time.

### Data Format
- The dataset can be downloaded from [here](https://data.boston.gov/dataset/311-service-requests)
- It will be necessary to combine multiple years, you can do this in excel, notepad, or using any online tool.
- Afterwards, run `data_processing.py` to add month and year columns and filter out for rodent only calls.

### Screenshots
![Screenshot 2025-03-02 012239](https://github.com/user-attachments/assets/15d9866e-b5dd-4fe4-bacf-e7c3b2f25ad6)
![Screenshot 2025-03-02 022602](https://github.com/user-attachments/assets/61cd76e4-bc68-4f2d-b3a4-4f263084fca4)
![Screenshot 2025-03-02 022800](https://github.com/user-attachments/assets/20bc5a69-e4e0-4e86-9445-8556e3a50780)

### License

This project is licensed under the MIT License - see the license file for details.
