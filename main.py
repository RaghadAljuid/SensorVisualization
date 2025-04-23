import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

# 1. توليد بيانات حساسات تجريبية
np.random.seed(0)
time = pd.date_range(start='2025-01-01', periods=100, freq='H')
temperature = np.random.normal(loc=75, scale=5, size=100)
temperature[5:10] = np.nan  # قيم مفقودة
temperature[25] = 200  # قيمة شاذة

df = pd.DataFrame({'Time': time, 'Temperature': temperature})

# 2. تنظيف البيانات
# تعويض القيم المفقودة (linear interpolation)
df['Temperature'] = df['Temperature'].interpolate(method='linear')

# إزالة القيم الشاذة (Z-score)
z_scores = np.abs(stats.zscore(df['Temperature']))
df = df[(z_scores < 3)]

# 3. تحويل البيانات (تطبيع)
scaler = MinMaxScaler()
df['Temperature_Norm'] = scaler.fit_transform(df[['Temperature']])

# 4. عرض جزء من البيانات المُنظّفة
print("📌 Sample of Curated Data:")
print(df.head())

# 5. رسم البيانات
plt.figure(figsize=(10,5))
plt.plot(df['Time'], df['Temperature'], label='Raw Temperature', color='orange')
plt.title('Temperature Over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°F)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
