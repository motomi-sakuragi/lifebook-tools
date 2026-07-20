import platform

print("Project Compass")
print("PC Health Checker")

print(platform.system())
print(platform.release())     # Windowsのリリース
print(platform.version())     # 詳細バージョン
print(platform.machine())     # CPUアーキテクチャ
print(platform.processor())   # CPU情報