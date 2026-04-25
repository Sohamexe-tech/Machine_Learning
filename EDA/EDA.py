import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# ── Step 1: Shape & Types ──────────────────────────────
print(df.shape)       # (891, 12)
print(df.dtypes)
print(df.head())

# ── Step 2: Missing Values ────────────────────────────
print(df.isnull().sum())
# Age: 177 missing, Cabin: 687 missing, Embarked: 2 missing

# Visualize missing data
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values (yellow = missing)')
plt.show()

# ── Step 3: Target Distribution ──────────────────────
print(df['Survived'].value_counts())
sns.countplot(x='Survived', data=df)
plt.title('Survived: 0=No, 1=Yes')
plt.show()

# ── Step 4: Univariate Analysis ──────────────────────
sns.histplot(df['Age'].dropna(), kde=True, bins=30)
plt.title('Age Distribution')
plt.show()

sns.countplot(x='Pclass', data=df)
plt.title('Passenger Class Distribution')
plt.show()

# ── Step 5: Bivariate Analysis (feature vs target) ───
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.show()

# ── Step 6: Correlation Matrix ────────────────────────
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlations')
plt.show()

# ── Step 7: Feature Engineering (basic) ──────────────
df['Age'].fillna(df['Age'].median(), inplace=True)   # fill age with median
df['Embarked'].fillna('S', inplace=True)             # fill with most common
df.drop('Cabin', axis=1, inplace=True)               # too many nulls, drop it

df['Sex']      = df['Sex'].map({'male': 0, 'female': 1})      # encode
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}) # encode

print(df[['Age', 'Sex', 'Pclass', 'Survived']].head())
print("\n✅ Data is clean and ready for modeling!")