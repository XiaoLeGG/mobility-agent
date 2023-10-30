# Tools list

## 1. Preprocessing

### 1.1 Noise Filtering

#### 1.1.1 Description

This function help filter the useless or unreasonable points such as object suddenly moves too fast or object moves in a short and fast circles.

#### 1.1.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- max_speed (float) - Indicate that the points with a speed from previous point that beyond the max_speed will be deleted.
- include_loop (bool) optional - Whether to delete short and fast loops in the trajectories.
- loop_intensity (float) optional - Determines the intensity of deleting loops.

#### 1.1.3 Returns

- deleted_points (int) - The number of deleted points.

### 1.2 Stop Detection

#### 1.2.1 Description

Find the points in trajectory that can represent point-of-interest such as schools, restaurants, and bars, or user-specific places such as home and work locations.

#### 1.2.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- stay_time (float) - The minimum minutes that the object stays in the point.
- radius (float) - The radius to represent the maximum size of a point.

#### 1.2.3 Returns

- detected_points (int) - The collected points.

### 1.3 Compression

#### 1.3.1 Description

This function compress the consecutive points.

#### 1.3.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- radius (float) - The minimum distance (in km) between consecutive points of the compressed trajectory.

#### 1.3.3 Returns

- detected_points (int) - The collected points.

## 2. Mobility Measures

### 2.1 Individual Measures

#### 2.1.1 Radius of Gyration

##### 2.1.1.1 Description

This function Compute the radius of gyration (in kilometers) of a set of individuals in a TrajDataFrame.

The radius of gyration is a measure used to quantify the spatial dispersion or the spread of an individual's or object's movements over time. It provides an indication of how far an individual typically moves from their center of activity.

##### 2.1.1.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the radius of gyration of each individual) stored.

##### 2.1.1.3 Returns

- Successful (boolean) - Ture: Succeed.

#### 2.1.2 k_radius_of_gyration

##### 2.1.2.1 Description

Compute the k-radii of gyration (in kilometers) of a set of individuals in a TrajDataFrame.

In mobility analysis, the k-radius of gyration indicates the characteristic distance travelled by that individual as induced by their k most frequent locations.

##### 2.1.2.2 Arguments

- input_file (str) - The data file path to be processed.
- k(int) - the number of most frequent locations to consider. The default is 2. The possible range of values is [2,+inf].
- output_file (str) - The file path where the processed data(Pandas DataFrame: the k-radii of gyration of the individuals) stored.

##### 2.1.2.3 Returns

- Successful (boolean) - Ture: Succeed.

#### 2.1.3 Jump lengths

##### 2.1.3.1 Description

This3 function compute the jump lengths (in kilometers) of a set of individuals in a TrajDataFrame. A jump length (or trip distance) is defined as the geographic distance between two consecutive points. 

##### 2.1.3.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the jump lengths for  each individual) stored.
- merge (boolean) - True: merge the individuals' lists into one list

##### 2.1.3.3 Return

- Successful (boolean) - Ture: Succeed.

#### 2.1.4 Home Location

##### 2.1.4.1 Description

This function compute the home location of a set of individuals in a TrajDataFrame.

##### 2.1.4.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the home location, as a (latitude, longitude) pair, of the individuals) stored.

##### 2.1.4.3 Return

- Successful (boolean) - Ture: Succeed.

#### 2.1.5 Distance Straight Line

##### 2.1.5.1 Description

Compute the distance (in kilometers) travelled straight line by a set of individuals in a TrajDataFrame.

##### 2.1.5.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the straight line distance traveled by the individuals) stored.

##### 2.1.5.3 Return

- Successful (boolean) - Ture: Succeed.

#### 2.1.6 Frequency Rank

##### 2.1.6.1 Description

Compute the frequency rank of the location of a set of individuals in a TrajDataFrame. The frequency rank K <sub>f</sub> (r<sub>i</sub>) of a location r<sub>i</sub> of an individual u is K <sub>f</sub> (r<sub>i</sub>)=1 if location r<sub>i</sub> is the most visited location, it is K <sub>f</sub> (r<sub>i</sub>)=2 if r<sub>i</sub> is the second-most visited location, and so on.

##### 2.1.6.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the frequency rank for each location of the individuals) stored.

##### 2.1.6.3 Return

- Successful (boolean) - Ture: Succeed.

#### 2.1.7 Location Frequency

##### 2.1.7.1 Description

Compute the visitation frequency of each location, for a set of individuals in a TrajDataFrame.  Given an individual `u`, the visitation frequency of a location r<sub>i</sub> is the number of visits to that location by `u`.  The higher the value, the more frequently u is located at r<sub>i</sub> 

##### 2.1.7.2 Arguments

- input_file (str) - The data file path to be processed.
- normalize (bool) - if True, the number of visits to a location by an individual is computed as probability, i.e., divided by the individual’s total number of visits. The default is True. // 这个可以直接设置为True or False,不需要作为参数
- as_ranks (bool) - if True, return a list where element i indicates the average visitation frequency of the i-th most frequent location. The default is False.
- location_columns (list) - the name of the column(s) indicating the location. The default is [constants.LATITUDE, constants.LONGITUDE]. // 我们也可以规范化命名，这个参数也可以不需要
- output_file (str) - The file path where the processed data((Pandas DataFrame: the location frequency for each location for each individual) or (List: the ranks list for each individual)) stored.

##### 2.1.7.3 Return

- Successful (boolean) - Ture: Succeed.

#### 2.1.8 Individual mobility network

##### 2.1.8.1 Description

Compute the individual mobility network of a set of individuals in a TrajDataFrame. An Individual Mobility Network (aka IMN) of an individual `u` is a directed graph `G_u=(V,E)`, where `V` is the set of nodes and `E` is the set of edges. Nodes indicate locations visisted by `u`, and edges indicate trips between two locations by `u`.  The weight of edges is the number of travel performed by `u` on that edge.

##### 2.1.8.2 Arguments

- input_file (str) - The data file path to be processed.
- self_loop (bool) - if True, adds self loops also. The default is False.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the home locatioTrajDataFramen) stored.

##### 2.1.8.3 Return

- Successful (boolean) - Ture: Succeed

#### 2.1.9 Max Distance From Home

##### 2.1.9.1 Description

Compute the maximum distance (in kilometers) traveled from their home location by a set of individuals in a TrajDataFrame. 

##### 2.1.9.2 Arguments

- input_file (str) - The data file path to be processed.
- start_night (str) - the starting time of the night (format HH:MM). The default is ‘22:00’.
- end_night (str) - the ending time for the night (format HH:MM). The default is ‘07:00’.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the maximum distance from home of the individuals.) stored.

##### 2.1.9.3 Return

- Successful (boolean) - Ture: Succeed

