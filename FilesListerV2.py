import os
import csv
import json

folder_path = input("Enter the path to the folder: ")
folder_name = os.path.basename(folder_path)
file_info = []

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        file_extension = os.path.splitext(file_name)[1]
        file_info.append(
            {"File Name": file_name, "Size": file_size, "Type": file_extension})

total_files = len(file_info)

text_file_name = folder_name + ".txt"
csv_file_name = folder_name + ".csv"
json_file_name = folder_name + ".json"

text_file_path = os.path.join(
    os.environ["USERPROFILE"], "Desktop", text_file_name)
csv_file_path = os.path.join(
    os.environ["USERPROFILE"], "Desktop", csv_file_name)
json_file_path = os.path.join(
    os.environ["USERPROFILE"], "Desktop", json_file_name)

with open(text_file_path, "w") as f:
    f.write(f"Folder: {folder_name}\n")
    f.write(f"Total Files: {total_files}\n\n")
    for file_data in file_info:
        f.write(f"File: {file_data['File Name']}, Size: {
                file_data['Size']} bytes, Type: {file_data['Type']}\n")

with open(csv_file_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Folder", folder_name])
    writer.writerow(["Total Files", total_files])
    writer.writerow([])
    writer.writerow(["File Names", "File Size (bytes)", "File Type"])
    for file_data in file_info:
        writer.writerow(
            [file_data['File Name'], file_data['Size'], file_data['Type']])

with open(json_file_path, "w") as f:
    json.dump({"Folder": folder_name, "Total Files": total_files,
              "Files": file_info}, f, indent=4)

print("")
print("Task successful")
print("Text file saved at:", text_file_path)
print("CSV file saved at:", csv_file_path)
print("JSON file saved at:", json_file_path)
