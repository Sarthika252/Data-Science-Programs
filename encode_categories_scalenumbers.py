import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Create sample dataset
data = {
    'Size': ['Small', 'Medium', 'Large', 'Small',
             'Large', 'Medium', 'Small', 'Large',
             'Medium', 'Small'],

    'Color': ['Red', 'Blue', 'Green', 'Blue',
              'Red', 'Green', 'Red', 'Blue',
              'Green', 'Blue'],

    'Price': [100, 200, 300, 150, 350,
              250, 120, 400, 280, 180],

    'Weight': [1.2, 2.5, 3.5, 1.5, 4.0,
               2.8, 1.3, 4.5, 3.0, 2.0],

    'Purchased': [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 1: Map ordered Size column into numbers
size_mapping = {
    'Small': 1,
    'Medium': 2,
    'Large': 3
}

df['Size'] = df['Size'].map(size_mapping)

print("\nAfter Mapping Size:")
print(df)

# Step 2: One-hot encode Color column
df = pd.get_dummies(
    df,
    columns=['Color'],
    dtype=int
)

print("\nAfter One-Hot Encoding:")
print(df)

# Step 3: Separate features and target
X = df.drop('Purchased', axis=1)
y = df['Purchased']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# Step 5: Apply Min-Max Scaling
minmax_scaler = MinMaxScaler()

X_train_minmax = X_train.copy()
X_test_minmax = X_test.copy()

numeric_columns = ['Price', 'Weight']

X_train_minmax[numeric_columns] = minmax_scaler.fit_transform(
    X_train[numeric_columns]
)

X_test_minmax[numeric_columns] = minmax_scaler.transform(
    X_test[numeric_columns]
)

print("\nMin-Max Scaled Training Data:")
print(X_train_minmax)

# Step 6: Apply Standard Scaling
standard_scaler = StandardScaler()

X_train_standard = X_train.copy()
X_test_standard = X_test.copy()

X_train_standard[numeric_columns] = standard_scaler.fit_transform(
    X_train[numeric_columns]
)

X_test_standard[numeric_columns] = standard_scaler.transform(
    X_test[numeric_columns]
)

print("\nStandard Scaled Training Data:")
print(X_train_standard)

print("\nStandard Scaled Testing Data:")
print(X_test_standard)

# Display dataset shapes
print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)