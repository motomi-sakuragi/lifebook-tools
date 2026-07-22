import platform
import psutil
from datetime import datetime

def print_section(title):
    print()
    print(title)

now = datetime.now()

print("=" * 40)
print("Project Compass")
print("PC Health Checker")
print(f"Scan Time : {now.strftime('%Y/%m/%d %H:%M:%S')}")
print("=" * 40)

print_section("OS Information:")
print(platform.system(),platform.release())     # Windowsのリリース
print(platform.version())     # 詳細バージョン

print_section("CPU Information:")
print(platform.machine())     # CPUアーキテクチャ
print(platform.processor())   # CPU情報
cpu = psutil.cpu_percent(interval=1)
print(f"CPU使用率: {cpu}%")

print_section("Memory Information:")
memory = psutil.virtual_memory()
memory_gb = memory.total / (1024 ** 3)
print(f"搭載メモリ: {memory_gb:.1f} GB")
print(f"メモリ使用率: {psutil.virtual_memory().percent}%")

print_section("Disk Information:")
disk = psutil.disk_usage("/")
print(f"ディスク容量: {disk.total / (1024 ** 3):.1f} GB")
print(f"使用中: {disk.used / (1024 ** 3):.1f} GB")
print(f"空き: {disk.free / (1024 ** 3):.1f} GB")

print()

print("=" * 40)
memory_percent = psutil.virtual_memory().percent
disk_percent = disk.percent

if memory_percent < 90 and disk_percent < 90:
    print("Everything OK")
else:
    print("Warning")
print("=" * 40)