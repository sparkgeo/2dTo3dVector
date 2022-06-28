# Mountaineer
A CLI to convert 2D vector data to 3D vector data.  

### Information
CLI Docs : Information

Users: Optimal users for this application are open-source, geospatial experts with understanding of Geospatial data formats and a general reliance on command-line input as opposed to GUI input. Users of this software should be familiar with input and output data types, geospatial data conversion, and the necessary fields required to append geospatial data without a user interface. 

Use Case: This application will be able to turn a 2D Vector file into a 3D Vector file by appending height values of the location of the line to associated Z-values from AWS open source tile Server. As a result, one use of this app could be to give height to a line, and to demonstrate changes in elevation in datasets that depict things like trails. A user could run the trail line through the application and visualise the height differences between other trails along the route, or they could see how steep a particular stretch of the trail could be. 

Where used: This application could be used by navigators or route planners to prepare for particularly high or low stretches of trails for hikes, bikes, or whichever other elements where height could be applied to a trail. If packaged as a script, this tool could be used to 3d-ify bike trails through simple input, and be used to generate maps for display or navigational use.


## Usage
CLI Usage: One liner

mountaineer get-elev [input file] [output file]

[input file]: Input file. Default file type is .GeoJSON. Input file length should not exceed 128 characters. 
[output file]: Output file. Located in the same directory as the input file, will default to .GeoJSON.

## Other Options

mountaineer –-help / --h
	Brings up help: shows a baseline command for users, requirements for input

### Description of Process

## get-elev - Z values

AWS
-WKT Temporary file is opened in new geopandas dataframe

-Extent of file geometry is converted into WKT 

-AWS Terrain tile with matching coordinates is pulled

-Z values are copied from the tile/files in question into the temporary file

-WKT file now has appended Z values for height

-Data is exported into GeoJSON and output in local folder

### Systems Diagram
[!](https://mermaid.ink/img/pako:eNptkcFqwzAMhl9F6LpmD-BDoTQlDAqDtdtg5CJiZfOW2J0tF0rpu09Zk0DZdLHx96Hfls_YBMtoMPF3Zt9w6eg9Ul970HpOHIvl8m69fTDwlH2CTcdHqFiuXM9nvA7-yFFAgvLwmYK_carSwDaQBeehJKFWQ_jGWL3uzNAa9hwjqbZ3HaeromwOmrAMGCJLjp7tkKsYKMG9uPZP9spaeCteqMtTz6qcWz5mOeT_r65OMYxhllqNHczfNZ2S8DisqXCBPceenNWxngdWo3ywvhaNbi3Frxprf1EvHywJb6yTENG01CVeIGUJu5Nv0EjMPEnjv4zW5QcveYk2)](https://mermaid.live/edit#pako:eNptkcFqwzAMhl9F6LpmD-BDoTQlDAqDtdtg5CJiZfOW2J0tF0rpu09Zk0DZdLHx96Hfls_YBMtoMPF3Zt9w6eg9Ul970HpOHIvl8m69fTDwlH2CTcdHqFiuXM9nvA7-yFFAgvLwmYK_carSwDaQBeehJKFWQ_jGWL3uzNAa9hwjqbZ3HaeromwOmrAMGCJLjp7tkKsYKMG9uPZP9spaeCteqMtTz6qcWz5mOeT_r65OMYxhllqNHczfNZ2S8DisqXCBPceenNWxngdWo3ywvhaNbi3Frxprf1EvHywJb6yTENG01CVeIGUJu5Nv0EjMPEnjv4zW5QcveYk2)
