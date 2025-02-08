import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Timestamp': ['2023-09-01 08:00', '2023-09-01 09:00', '2023-09-01 22:00', '2023-09-02 01:00'],
    'User': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'Bytes_Transferred': [500, 600, 5000, 10000]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Detect anomalies (e.g., high data transfer during off-hours)
df['Hour'] = df['Timestamp'].dt.hour
anomalies = df[(df['Hour'] < 8) | (df['Hour'] > 18) & (df['Bytes_Transferred'] > 5000)]

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(df['User'], df['Bytes_Transferred'], color='blue', label='Normal')
plt.bar(anomalies['User'], anomalies['Bytes_Transferred'], color='red', label='Anomalous')
plt.title('Data Transfer by User')
plt.xlabel('User')
plt.ylabel('Bytes Transferred')
plt.legend()
plt.show()