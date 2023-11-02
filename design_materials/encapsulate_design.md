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

This function compute the radius of gyration (in kilometers) of a set of individuals.

The radius of gyration is a measure used to quantify the spatial dispersion or the spread of an individual's or object's movements over time. It provides an indication of how far an individual typically moves from their center of activity.

##### 2.1.1.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.1.3 Returns

- result (ndarray) - A 2-dimension numpy array indicating the result table with indivisual id and corresponding gyration.

#### 2.1.2 K Radius of Gyration

##### 2.1.2.1 Description

Compute the k-radii of gyration (in kilometers) of a set of individuals.

In mobility analysis, the k-radius of gyration indicates the characteristic distance travelled by that individual as induced by their k most frequent locations.

##### 2.1.2.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- k (int) - the number of most frequent locations to consider. The default is 2. The possible range of values is [2,+inf].

##### 2.1.2.3 Returns

- result (ndarray) - A 2-dimension numpy array indicating the result table with indivisual id and corresponding gyration.

#### 2.1.3 Jump lengths

##### 2.1.3.1 Description

This function compute the jump lengths (in kilometers) of a set of individuals. A jump length (or trip distance) is defined as the geographic distance between two consecutive points. 

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.3.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.3.3 Return

- result (ndarray) - A 2-dimension array indicating the result table with individual id and corresponding list of jump lengths.

#### 2.1.4 Home Location

##### 2.1.4.1 Description

This function compute the home location of a set of individuals. The home location is defined as the location `v` for every individual `u` visits most during nighttime.

##### 2.1.4.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- start_night_time (str) - The start time of the night. The default is '22:00'.
- end_night_time (str) - The end time of the night. The default is '06:00'.

##### 2.1.4.3 Return

- result (ndarray) : A 3-dimension numpy array indicating the result table with individual id and corresponding home location (latitude and longitude).

#### 2.1.5 Distance Straight Line

##### 2.1.5.1 Description

Compute the distance (in kilometers) travelled straight line by a set of individuals in a TrajDataFrame. The distance straight d<sub>SL</sub> travelled by an individual `u` is computed as the sum of the distances travelled `u`.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.5.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.5.3 Return

- result (ndarray) - A 2-dimension array indicating the result table with individual id and corresponding list of distance straight line.

#### 2.1.6 Frequency Rank

##### 2.1.6.1 Description

Compute the frequency rank of the location of a set of individuals in a TrajDataFrame. The frequency rank K <sub>f</sub> (r<sub>i</sub>) of a location r<sub>i</sub> of an individual u is K <sub>f</sub> (r<sub>i</sub>)=1 if location r<sub>i</sub> is the most visited location, it is K <sub>f</sub> (r<sub>i</sub>)=2 if r<sub>i</sub> is the second-most visited location, and so on.

##### 2.1.6.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.6.3 Return

- result (ndarray) - A 4-dimension numpy array indicating the result table with indivisual id, location (latitude and longitude) and the frequency rank for each location of the individuals.

#### 2.1.7 Location Frequency

##### 2.1.7.1 Description

Compute the visitation frequency of each location, for a set of individuals in a TrajDataFrame.  Given an individual `u`, the visitation frequency of a location r<sub>i</sub> is the number of visits to that location by `u`.  The higher the value, the more frequently u is located at r<sub>i</sub> 

##### 2.1.7.2 Arguments

- input_file (str) - The data file path to be processed.
- normalize (bool) - if True, the number of visits to a location by an individual is computed as **probability**, i.e., divided by the individual’s total number of visits. The default is True. // 这个可以直接设置为True or False,不需要作为参数，
- as_ranks (bool) - if True, return a list where element i indicates the average visitation frequency of the i-th most frequent location. The default is False. // 这个或者可以不用，直接使用frequency rank
- location_columns (list) - the name of the column(s) indicating the location. The default is [constants.LATITUDE, constants.LONGITUDE]. // 我们也可以规范化命名，这个参数也可以不需要
- output_file (str) - The file path where the processed data stored.

##### 2.1.7.3 Return

- result (ndarray) -  A 4-dimension numpy array indicating the result table with indivisual id, location (latitude and longitude) and the location frequency  for each location of the individuals.

#### 2.1.8 Individual mobility network

##### 2.1.8.1 Description

Compute the individual mobility network of a set of individuals in a TrajDataFrame. An Individual Mobility Network (aka IMN) of an individual `u` is a directed graph `G_u=(V,E)`, where `V` is the set of nodes and `E` is the set of edges. Nodes indicate locations visisted by `u`, and edges indicate trips between two locations by `u`.  The weight of edges is the number of travel performed by `u` on that edge.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.8.2 Arguments

- input_file (str) - The data file path to be processed.
- self_loop (bool) - if True, adds self loops also. The default is False.
- output_file (str) - The file path where the processed data stored.

##### 2.1.8.3 Return

- result (ndarray) - A 5-dimension numpy array indicating the result table with indivisual id, origin_location (latitude and longitude), dest_location (latitude and longitude) and the trip_id.

#### 2.1.9 Max Distance From Home

##### 2.1.9.1 Description

Compute the maximum distance (in kilometers) traveled from their home location by a set of individuals in a TrajDataFrame. The most frequency location in nighttime is the location of home. 

##### 2.1.9.2 Arguments

- input_file (str) - The data file path to be processed.
- start_night (str) - the starting time of the night (format HH:MM). The default is ‘22:00’. using to find home location.
- end_night (str) - the ending time for the night (format HH:MM). The default is ‘07:00’. using to find home location.
- output_file (str) - The file path where the processed data stored.

##### 2.1.9.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the max distance from home. 

#### 2.1.10 Maximum distance

##### 2.1.10.1 Description

Compute the maximum distance (in kilometers) traveled by a set of individuals in a TrajDataFrame. The maximum distance is defined as the maximum distance between two data point for every individual.

##### 2.1.10.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.10.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the maximum distance for this individual. 

#### 2.1.11 Number of Location

##### 2.1.11.1 Description

Compute the number of distinct locations visited by a set of individuals in a TrajDataFrame.

##### 2.1.11.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.11.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the number of location for this individual. 

#### 2.1.12 Number of visits

##### 2.1.12.1 Description

Compute the number of visits (i.e., data points) for each individual in a TrajDataFrame.

##### 2.1.12.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.12.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the number of visits for this individual. 

#### 2.1.13 Random entropy

##### 2.1.13.1 Description

Compute the random entropy of a set of individuals in a TrajDataFrame. In this tool, we think every location is visited with equal probability, and the random entropy is defined as E<sub>rand</sub>(u)=log<sub>2</sub>(N<sub>u</sub>) , where N<sub>u</sub> is the number of distinct locations visited by individual `u`. The more places the user went, the higher the value 

##### 2.1.13.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.13.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the random entropy for this individual. 

#### 2.1.14 Random entropy

##### 2.1.14.1 Description

Compute the real entropy of a set of individuals in a TrajDataFrame. The real entropy depends not only on the frequency of visitation, but also the order in which the nodes were visited and the time spent at each location, thus capturing the full spatio-temporal order present in an `u`'s mobility patterns. he random entropy of an individual `u` is defined as
$$
E(u) = - \sum_{T'_u}P(T'_u)log_2[P(T_u^i)]
$$
where P(T<sub>u</sub>′) is the probability of finding a particular time-ordered subsequence T<sub>u</sub>′ in the trajectory T<sub>u</sub>. 

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.14.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.14.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the real entropy for this individual. 

#### 2.1.15 recency rank

##### 2.1.15.1 Description

Compute the recency rank of the location of a set of individuals in a TrajDataFrame. The recency rank K <sub>s</sub> (r<sub>i</sub>) of a location r<sub>i</sub> of an individual u is K <sub>s</sub> (r<sub>i</sub>)=1 if location r<sub>i</sub> is the last visited location, it is K <sub>s</sub> (r<sub>i</sub>)=2 if r<sub>i</sub> is the second-lastvisited location, and so on.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.15.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.15.3 Return

- result (ndarray) - A 4-dimension numpy array indicating the result table with indivisual id, location (latitude and longitude) and the recency rank for each location of the individuals. (sorted in ascending order )

#### 2.1.16 uncorrelated entropy

##### 2.1.16.1 Description

Compute the temporal-uncorrelated entropy of a set of individuals in a TrajDataFrame. The temporal-uncorrelated entropy of an individual `u` is defined as 
$$
E_{unc}(u) = - \sum_{j=1}^{N_u} p_u(j) log_2 p_u(j)
$$
where p<sub>u</sub>(j) is the number of distinct locations visited by `i` and p<sub>u</sub>(j) is the historical probability that a location `j` was visited by `u`. The temporal-uncorrelated entropy characterizes the heterogeneity of `u`s visitation patterns.

##### 2.1.16.2 Arguments

- input_file (str) - The data file path to be processed.
- normalize (bool) - if True, the value will in range [0,1], The default is False. // 这个可以直接设置为True or False,不需要作为参数，
- output_file (str) - The file path where the processed data stored.

##### 2.1.16.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the temporal-uncorrelated entropy for this individual. 

#### 2.1.17 recency rank

##### 2.1.17.1 Description

Compute the waiting times (in seconds) between the movements of each individual in a TrajDataFrame. The wait time is  defined as the time between two consecutive points. 

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.17.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.17.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with indivisual id and the list record the wait time between every two consecutive points for every individual.











