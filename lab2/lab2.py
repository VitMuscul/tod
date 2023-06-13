from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Завантаження датасету Iris
iris = load_iris()

# Поділ датасету на тренувальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

# Створення пайплайну
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Масштабування даних
    ('pca', PCA(n_components=2)),  # Відбір 2 головних компонент
])

from sklearn.linear_model import LogisticRegression

# Додавання моделі класифікації до пайплайну
pipeline.steps.append(('classifier', LogisticRegression()))

from sklearn.model_selection import GridSearchCV

# Список гіперпараметрів та значень для перевірки
param_grid = {
    'classifier__C': [0.1, 1, 10],
}

# GridSearchCV для налаштування гіперпараметрів
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Передбачення на тестовій вибірці
y_pred = grid_search.predict(X_test)

# Оцінка якості моделі
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import joblib

# Збереження пайплайну
joblib.dump(grid_search, 'pipeline.pkl')

# Завантаження пайплайну
loaded_pipeline = joblib.load('pipeline.pkl')
