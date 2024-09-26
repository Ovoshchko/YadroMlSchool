import numpy as np
import os

def compute_radii(points):
    return np.sqrt(points[:, 0]**2 + points[:, 1]**2)

# Функция для анализа распределения радиусов
def analyze_distribution(points):
    radii = compute_radii(points)
    
    # Плотность точек на различных радиусах
    density_0_03 = np.sum(radii <= 0.3) / len(radii)  # Плотность в центре (радиус <= 0.3)
    density_03_07 = np.sum((radii > 0.3) & (radii <= 0.7)) / len(radii)  # Плотность в средней зоне
    density_07_1 = np.sum((radii > 0.7) & (radii <= 1.0)) / len(radii)  # Плотность на границе

    # Центр масс для проверки отклонений
    center_of_mass = np.mean(points, axis=0)

    return density_0_03, density_03_07, density_07_1, center_of_mass

# Функция для предсказания алгоритма
def predict_algorithm(points):
    density_0_03, density_03_07, density_07_1, center_of_mass = analyze_distribution(points)
    
    # В Алгоритме 1 плотность в центре (density_0_03) выше, чем на границе (density_07_1)
    if density_0_03 > density_07_1 and np.linalg.norm(center_of_mass) < 0.1:
        return 1  # Алгоритм 1 (Полярные координаты)
    else:
        return 0  # Алгоритм 0 (Отсечение)

# Функция для обработки всех файлов в катал
def process_directory(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):  # Предполагаем, что файлы данных имеют расширение .txt
            filepath = os.path.join(directory, filename)
            points = np.genfromtxt(filepath, delimiter=',', skip_header=1)  
            algorithm = predict_algorithm(points)
            results.append(algorithm)
    return results

# Основная программа
directory = '/mnt/c/Artem/YadroMlSchool/IntroTest/Files'  # Укажите путь к каталогу с файлами
results = process_directory(directory)

# Вывод списка алгоритмов
print(results)
