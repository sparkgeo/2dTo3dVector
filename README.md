# Mountaineer
## Additions
A CLI to convert 2D vector data to 3D vector data.   
CLI Usage: One liner

mountaineer [input file] [lat] [lon] [output file]

[input file]: Input file. File type can be .KML, .SHP, .GeoJSON (preferred). These are geospatial formats that contain Lat/long coordinates. Input file length should not exceed 128 characters. 

[lat]: Latitude field. Required to create WKT
[lon]: Longitude field. Required to create WKT

[output]: User-input Output file name. File will be placed in the same folder as the input file. File length should not exceed 128 characters. File output will DEFAULT to .GeoJSON, but other outputs can be selected by changing the file extension. 


Other commands:

mountaineer – help
	Brings up help: shows a baseline command for users, accepted file types, accepted inputs and outputs

mountaineer q - exits the CLI and returns user to terminal 



Description of Process

Locally
-CLI awaits for user input, user input being a path to a 2d geometry file stored locally.
-File can be points, lines, or polygon for geometry
-File is opened in Geopandas within a new dataframe
-File is checked for proper geometry values for its data type, type of file is read back via console for verification.
-File is scanned for latitude and longitude headers
-Latitude and Longitude values are exported from file into a temporary file, as Well Known Text (WKT)

AWS
-WKT Temporary file is opened in new geopandas dataframe
-Extent of file is read back into lat/long and is pulled from AWS
-AWS Terrain tile matching extent of file is copied from AWS
-Z values are copied from the tile/files in question into a new file containing the Z Values
-Intersect is run on tiles where Z values are appended to the temp WKT file from before
-WKT file now has Z values as a field
-Data can be exported as a GEOJSON default file format, although KML and SHP will be accepted as well.


CLI Docs : MISC information

Users: Optimal users for this application are open-source, geospatial experts with understanding of Geospatial data formats and a general reliance on command-line input as opposed to GUI input. Users of this software should be familiar with input and output data types, geospatial data conversion, and the necessary fields required to append geospatial data without a user interface. 

Use Case: This application will be able to turn a 2D Vector file into a 3D Vector file by appending height values of the location of the line to associated Z-values from AWS open source tile Server. As a result, one use of this app could be to give height to a line, and to demonstrate changes in elevation in datasets that depict things like trails. A user could run the trail line through the application and visualise the height differences between other trails along the route, or they could see how steep a particular stretch of the trail could be. 

Where used: This application could be used by navigators or route planners to prepare for particularly high or low stretches of trails for hikes, bikes, or whichever other elements where height could be applied to a trail. If packaged as a script, this tool could be used to 3d-ify bike trails through simple input, and be used to generate maps for display or navigational use.


![Embedded Diagram](/mountaineer_v1.png?raw=true "Optional Title")
