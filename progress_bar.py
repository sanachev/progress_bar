import sys
import time

# Функция принимает на вход измеримое значение(цель), текущее значение и название метрики
# Выводит прогресс бар в консоль
# Образец:
# Load data             [#######################...........................]  47%

def progress_bar(label: str, current: int, total: int) -> None:
    """
    label - название метрики (до 21 символа)
    total - конечное значение метрики
    current - текущее значение метрики
    """
    percent = current / total if total else 0
    progress = int(50 * percent)
    bar = "#" * progress + "." * (50 - progress)
    sys.stdout.write(f"\r{label:<21} [{bar}] {int(percent*100):3d}%")
    sys.stdout.flush()
    if current >= total:
        sys.stdout.write("\n")


# Test

if __name__ == "__main__":
    total = 100
    label = "Load data"

    for i in range(total + 1):
        progress_bar(label, i, total)
        time.sleep(0.05)
