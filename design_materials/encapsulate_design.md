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

### 2.1 radius of gyration

#### 2.1.1 Description

This function Compute the radius of gyration (in kilometers) of a set of individuals in a TrajDataFrame.

The radius of gyration is a measure used to quantify the spatial dispersion or the spread of an individual's or object's movements over time. It provides an indication of how far an individual typically moves from their center of activity.

#### 2.1.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the radius of gyration of each individual) stored.

#### 2.1.3 Returns

- Successful (boolean) - Ture: Succeed

### 2.2 jump lengths

#### 2.2.1 Description

This function compute the jump lengths (in kilometers) of a set of individuals in a TrajDataFrame.

#### 2.2.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the jump lengths for  each individual) stored.
- merge (boolean) - True: merge the individuals' lists into one list

#### 2.2.3 Return

- Successful (boolean) - Ture: Succeed

### 2.3 home location

#### 2.3.1 Description

This function compute the home location of a set of individuals in a TrajDataFrame.

#### 2.3.2 Arguments

- input_file (str) - The data file path to be processed.
- output_file (str) - The file path where the processed data(Pandas DataFrame: the home location) stored.

#### 2.3.3 Return

- Successful (boolean) - Ture: Succeed

