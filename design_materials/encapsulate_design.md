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

### 1.4 Clustering

#### 1.4.1 Description

This function cluster the stops of each individual. The stops correspond to visits to the same location at different times, based on spatial proximity.

#### 1.4.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- radius (float) - The parameter `eps` of the function sklearn.cluster.DBSCAN, in kilometers.

#### 1.4.3 Returns

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

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and corresponding gyration.

#### 2.1.2 K Radius of Gyration

##### 2.1.2.1 Description

Compute the k-radii of gyration (in kilometers) of a set of individuals.

In mobility analysis, the k-radius of gyration indicates the characteristic distance travelled by that individual as induced by their k most frequent locations.

##### 2.1.2.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- k (int) - the number of most frequent locations to consider. The default is 2. The possible range of values is [2,+inf].

##### 2.1.2.3 Returns

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and corresponding gyration.

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

Compute the distance (in kilometers) travelled straight line by a set of individuals. The distance straight dSL travelled by an individual `u` is computed as the sum of the distances travelled `u`.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.5.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.5.3 Return

- result (ndarray) - A 2-dimension array indicating the result table with individual id and corresponding list of distance straight line.

#### 2.1.6 Frequency Rank

##### 2.1.6.1 Description

Compute the frequency rank of the location of a set of individuals. The frequency rank K f (ri) of a location ri of an individual u is K f (ri)=1 if location ri is the most visited location, it is K f (ri)=2 if ri is the second-most visited location, and so on.

##### 2.1.6.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.6.3 Return

- result (ndarray) - A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the frequency rank for each location of the individuals.

#### 2.1.7 Location Frequency

##### 2.1.7.1 Description

Compute the visitation frequency of each location, for a set of individuals. Given an individual `u`, the visitation frequency of a location ri is the number of visits to that location by `u`. The higher the value, the more frequently u is located at ri

##### 2.1.7.2 Arguments

- input_file (str) - The data file path to be processed.
- normalize (bool) - if True, the number of visits to a location by an individual is computed as **probability**, i.e., divided by the individual’s total number of visits. The default is True. // 这个可以直接设置为True or False,不需要作为参数，
- as_ranks (bool) - if True, return a list where element i indicates the average visitation frequency of the i-th most frequent location. The default is False. // 这个或者可以不用，直接使用frequency rank
- location_columns (list) - the name of the column(s) indicating the location. The default is [constants.LATITUDE, constants.LONGITUDE]. // 我们也可以规范化命名，这个参数也可以不需要
- output_file (str) - The file path where the processed data stored.

##### 2.1.7.3 Return

- result (ndarray) - A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the location frequency for each location of the individuals.

#### 2.1.8 Individual mobility network

##### 2.1.8.1 Description

Compute the individual mobility network of a set of individuals. An Individual Mobility Network (aka IMN) of an individual `u` is a directed graph `G_u=(V,E)`, where `V` is the set of nodes and `E` is the set of edges. Nodes indicate locations visited by `u`, and edges indicate trips between two locations by `u`. The weight of edges is the number of travel performed by `u` on that edge.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.8.2 Arguments

- input_file (str) - The data file path to be processed.
- self_loop (bool) - if True, adds self loops also. The default is False.
- output_file (str) - The file path where the processed data stored.

##### 2.1.8.3 Return

- result (ndarray) - A 5-dimension numpy array indicating the result table with individual id, origin_location (latitude and longitude), dest_location (latitude and longitude) and the trip_id.

#### 2.1.9 Max Distance From Home

##### 2.1.9.1 Description

Compute the maximum distance (in kilometers) traveled from their home location by a set of individuals. The most frequency location in nighttime is the location of home.

##### 2.1.9.2 Arguments

- input_file (str) - The data file path to be processed.
- start_night (str) - the starting time of the night (format HH:MM). The default is ‘22:00’. using to find home location.
- end_night (str) - the ending time for the night (format HH:MM). The default is ‘07:00’. using to find home location.
- output_file (str) - The file path where the processed data stored.

##### 2.1.9.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the max distance from home.

#### 2.1.10 Maximum distance

##### 2.1.10.1 Description

Compute the maximum distance (in kilometers) traveled by a set of individuals. The maximum distance is defined as the maximum distance between two data point for every individual.

##### 2.1.10.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.10.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the maximum distance for this individual.

#### 2.1.11 Number of Location

##### 2.1.11.1 Description

Compute the number of distinct locations visited by a set of individuals.

##### 2.1.11.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.11.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the number of location for this individual.

#### 2.1.12 Number of visits

##### 2.1.12.1 Description

Compute the number of visits (i.e., data points) for each individual.

##### 2.1.12.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.12.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the number of visits for this individual.

#### 2.1.13 Random entropy

##### 2.1.13.1 Description

Compute the random entropy of a set of individuals. In this tool, we think every location is visited with equal probability, and the random entropy is defined as Erand(u)=log2(Nu) , where Nu is the number of distinct locations visited by individual `u`. The more places the user went, the higher the value

##### 2.1.13.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.13.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the random entropy for this individual.

#### 2.1.14 Random entropy

##### 2.1.14.1 Description

Compute the real entropy of a set of individuals. The real entropy depends not only on the frequency of visitation, but also the order in which the nodes were visited and the time spent at each location, thus capturing the full spatio-temporal order present in an `u`'s mobility patterns. he random entropy of an individual `u` is defined as $$ E(u) = - \sum_{T'_u}P(T'_u)log_2[P(T_u^i)] $$ where P(Tu′) is the probability of finding a particular time-ordered subsequence Tu′ in the trajectory Tu.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.14.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.14.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the real entropy for this individual.

#### 2.1.15 recency rank

##### 2.1.15.1 Description

Compute the recency rank of the location of a set of individuals. The recency rank K s (ri) of a location ri of an individual u is K s (ri)=1 if location ri is the last visited location, it is K s (ri)=2 if ri is the second-last visited location, and so on.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.15.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.15.3 Return

- result (ndarray) - A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the recency rank for each location of the individuals. (sorted in ascending order )

#### 2.1.16 uncorrelated entropy

##### 2.1.16.1 Description

Compute the temporal-uncorrelated entropy of a set of individuals. The temporal-uncorrelated entropy of an individual `u` is defined as $$ E_{unc}(u) = - \sum_{j=1}^{N_u} p_u(j) log_2 p_u(j) $$ where pu(j) is the number of distinct locations visited by `i` and pu(j) is the historical probability that a location `j` was visited by `u`. The temporal-uncorrelated entropy characterizes the heterogeneity of `u`s visitation patterns.

##### 2.1.16.2 Arguments

- input_file (str) - The data file path to be processed.
- normalize (bool) - if True, the value will in range [0,1], The default is False. // 这个可以直接设置为True or False,不需要作为参数，
- output_file (str) - The file path where the processed data stored.

##### 2.1.16.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the temporal-uncorrelated entropy for this individual.

#### 2.1.17 recency rank

##### 2.1.17.1 Description

Compute the waiting times (in seconds) between the movements of each individual. The wait time is defined as the time between two consecutive points.

Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

##### 2.1.17.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.1.17.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with individual id and the list record the wait time between every two consecutive points for every individual.

### 2.2 Collective Measures

#### 2.2.1 Homes per Location

##### 2.2.1.1 Description

This function computes the number of home locations in each location.

The number of home locations in a location is computed as: $$ N_{homes}(j) = |\{h_u | h_u = j, u \in U \}| $$ where indicates the home location of an individual and is the set of individuals.

The result(output file) of this measure is as follows:

```
         lat         lng  num_homes
0  39.739154 -104.984703       15
1  37.584103 -122.366083        6
2  40.014986 -105.270546        5
3  37.580304 -122.343679        5
4  37.774929 -122.419415        4
```

##### 2.2.1.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.2.1.3 Returns

- result (triple) - location tuple (lat,lng) of the place with most homes.

#### 2.2.2 Mean Square Displacement

##### 2.2.2.1 Description

Compute the mean square displacement across the individuals.

The mean squared displacement is a measure of the deviation of the position of an object with respect to a reference position over time. It is defined as: $$ MSD = \langle |r(t) - r(0)| \rangle = \frac{1}{N} \sum_{i = 1}^N |r^{(i)}(t) - r^{(i)}(0)|^2 $$ where $$N$$ is the number of individuals to be averaged, vector $$x^{(i)}(0)$$ is the reference position of the $$i$$-th individual, and vector $$x^{(i)}(t)$$ is the position of the $$i$$-th individual at time $$t$$.

##### 2.2.2.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.
- days (*int, optional*) – the days since the starting time. The default is 0.

##### 2.2.2.3 Returns

- result (double) - the msd value.

#### 2.2.3 Random location entropy

##### 2.2.3.1 Description

Compute the random location entropy of the locations.

The random location entropy of a location $$j$$ captures the degree of predictability of $$j$$ if each individual visits it with equal probability, and it is defined as: $$ LE_{rand}(j) = log_2(N_j) $$ where $$N_j$$ is the number of distinct individuals that visited location $$j$$.

The result(output file) of this measure is as follows:

```
             lat         lng  random_location_entropy
10286  39.739154 -104.984703                 6.129283
49      0.000000    0.000000                 5.643856
5991   37.774929 -122.419415                 5.523562
12504  39.878664 -104.682105                 5.491853
5377   37.615223 -122.389979                 5.247928
```

##### 2.2.3.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.2.3.3 Returns

- result (triple) - location tuple (lat,lng) of the place with the highest random location entropy.

#### 2.2.4 Uncorrelated Location Entropy

##### 2.2.4.1 Description

Compute the temporal-uncorrelated location entropy of the locations.

The temporal-uncorrelated location entropy $$LE_{unc}(j)$$ of a location $$j$$ is the historical probability that $$j$$ is visited by an individual $$u$$. Formally, it is defined as : $$ LE_{unc}(j) = -\sum_{i=j}^{N_j} p_jlog_2(p_j) $$ where $$N_j$$ is the number of distinct individuals that visited $$j$$ and $$p_j$$ is the historical probability that a visit to location $$j$$ is by individual $$u$$.

The result(output file) of this measure is as follows:

```
             lat         lng  uncorrelated_location_entropy
12504  39.878664 -104.682105                       3.415713
5377   37.615223 -122.389979                       3.176950
10286  39.739154 -104.984703                       3.118656
12435  39.861656 -104.673177                       2.918413
12361  39.848233 -104.675031                       2.899175
```

##### 2.2.4.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.2.4.3 Returns

- result (triple) - location tuple (lat,lng) of the place with the highest uncorrelated location entropy.

#### 2.2.5 Visits per location

##### 2.2.5.1 Description

Compute the number of visits to each location.

The result(output file) of this measure is as follows:

```
         lat         lng  n_visits
0  39.739154 -104.984703      3392
1  37.580304 -122.343679      2248
2  39.099275  -76.848306      1715
3  39.762146 -104.982480      1442
4  40.014986 -105.270546      1310
```

##### 2.2.5.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.2.5.3 Returns

- result (triple) - location tuple (lat,lng) of the place with most visits.

#### 2.2.6 Visits per Time Unit

##### 2.2.4.1 Description

Compute the number of data points per time unit (hour).

The result(output file) of this measure is as follows:

```
                           n_visits
datetime
2008-03-22 05:00:00+00:00         2
2008-03-22 06:00:00+00:00         2
2008-03-22 07:00:00+00:00         0
2008-03-22 08:00:00+00:00         0
2008-03-22 09:00:00+00:00         0
```

##### 2.2.4.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data stored.

##### 2.2.4.3 Returns

- result (date time) - time with most visits.

## 3. Model

#### 3.1 Markov Diary Generator

##### 3.1.1 Description

simulate or predict trajectory data from the input trajectory (the input data must preprocessed by cluster)data by using Markov Diary Learner and Generator. The resulting composite movement diary includes the movement of individuals between clusters.

A Mobility Diary Learner (MDL) is a data-driven algorithm to compute a mobility diary MD from the mobility trajectories of a set of real individuals. We use a Markov model to describe the probability that an individual follows her routine and visits a typical location at the usual time, or she breaks the routine and visits another location. First, MDL translates mobility trajectory data of real individuals into abstract mobility trajectories. Second, it uses the obtained abstract trajectory data to compute the transition probabilities of the Markov model MD(t)

##### 3.1.2 Argument

- input_file (str) - The input data file path(the data must preprocessed by cluster)
- output_file (str) - The file path where store generated data.
- n_individuals(int) - the number of individual in the input data
- start_time(datetime) - the starting date of the generation.
- diary_length (int) – the length of the diary in hours.

##### 3.1.3 Return

- result (ndarray) - A 2-dimension numpy array indicating the result table with time and the cluster_id.

#### 3.2 Gravity Model

##### 3.2.1 Description

simulate or predict trajectory data from the input flow data by using Gravity Model.

The Gravity model of human migration posits that the probability \(T_{ij}\) of moving from location \(i\) to \(j\) is proportional to \(\frac{P_i P_j}{r_{ij}}\), where \(P_i\) and \(P_j\) are the populations of locations \(i\) and \(j\), and \(r_{ij}\) is the distance between them. This model assumes that the number of trips leaving \(i\) is proportional to its population, the attractiveness of \(j\) is proportional to its population, and there is a cost effect in terms of distance traveled.

A generalized form of this model is \(T_{ij} = K m_i m_j f(r_{ij})\), where \(K\) is a constant, \(m_i\) and \(m_j\) relate to the number of trips, and \(f(r_{ij})\) is a decreasing function of distance.

Constrained gravity models address limitations. In a singly constrained model, the number of people originating from \(i\) is a known quantity \(O_i\), and the model estimates the destination:

\[ T_{ij} = K_i O_i m_j f(r_{ij}) = O_i \frac{m_i f(r_{ij})}{\sum_k m_k f(r_{ik})} \]

Proportionality constants \(K_i\) depend on the origin's location. A doubly-constrained model, fixing the total travelers arriving at \(j\) as \(D_j\), calculates:

\[ T_{ij} = K_i O_i L_j D_j f(r_{ij}) \]

##### 3.2.2 Argument

- input_file (str) - The input data file path
- output_file (str) - The file path where store generated data.

##### 3.2.3 Return

- result (ndarray) - A 3-dimension numpy array indicating the result table with origin area, destination area and flow.

## 4. Visualization

#### 4.1 Plot Trajectory

##### 4.1.1 Description

This function plots the trajectories on a plotly map.

##### 4.1.2 Argument

- input_file (str) - The data file path to be processed.(must contain "lat", "lng" rows)
- output_file (str) - The output graph file path(a json file).

#### 4.2 Plot Scatter

##### 4.2.1 Description

This function plots the scatter points on a plotly map.

##### 4.2.2 Argument

- input_file (str) - The data file path to be processed.(must contain "lat", "lng" rows)
- output_file (str) - The output graph file path(a json file).

#### 4.3 Plot Trajectory and Scatter

##### .3.1 Description

This function plots the trajectories and scatter points on a plotly map.

##### 4.3.2 Argument

- trajectory_input_file (str) - The trajectory data file path to be processed.(must contain "lat", "lng" rows)
- scatter_input_file (str) - The scatter points data file path to be processed.(must contain "lat", "lng" rows)
- output_file (str) - The output graph file path(a json file).

#### 4.4 Plot Dynamic Trajectory

##### 4.4.1 Description

This function dynamically plots the trajectories on an interactively plotly map.

##### 4.4.2 Argument

- input_file (str) - The data file path to be processed.(must contain "lat", "lng" rows)
- output_file (str) - The output graph file path(a json file).

#### 4.5 Plot Heatmap Density

##### 4.5.1 Description

This function plots the heatmap from a series of trajectories on a plotly map. This function requires the density values to be stored in the input file.

##### 4.5.2 Argument

- input_file (str) - The data file path to be processed.(must contain "lat", "lng", "density" rows)
- output_file (str) - The output graph file path(a json file).

#### 4.6 Plot Heatmap

##### 4.6.1 Description

This function plots the heatmap from a series of trajectories on a plotly map. This function calculates the density values from the intensity of points.

##### 4.6.2 Argument

- input_file (str) - The data file path to be processed.(must contain "lat", "lng" rows)
- output_file (str) - The output graph file path(a json file).