import os
import csv

folder_path = input("Enter the path to the folder: ")
folder_name = os.path.basename(folder_path)
file_names = [f for f in os.listdir(
    folder_path) if os.path.isfile(os.path.join(folder_path, f))]
total_files = len(file_names)

text_file_name = folder_name + ".txt"
csv_file_name = folder_name + ".csv"

with open(os.path.join(os.environ["USERPROFILE"], "Desktop", text_file_name), "w") as f:
    f.write(f"Folder: {folder_name}\n")
    f.write(f"Total Files: {total_files}\n\n")
    for file_name in file_names:
        f.write(file_name + "\n")

with open(os.path.join(os.environ["USERPROFILE"], "Desktop", csv_file_name), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Folder", folder_name])
    writer.writerow(["Total Files", total_files])
    writer.writerow([])
    writer.writerow(["File Names"])
    for file_name in file_names:
        writer.writerow([file_name])

print("Task successful")
