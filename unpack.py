import os
import subprocess

directory = "."

failed_log = "failed_unpacking.log"
success_log = "success_unpacking.log"

with open(failed_log, "w") as f:
    f.write("Failed to unpack the following files:\n")
with open(success_log, "w") as f:
    f.write("Successfully unpacked the following files:\n")

def log_failure(filename, reason):
    with open(failed_log, "a") as f:
        f.write(f"{filename}: {reason}\n")

def log_success(filename):
    with open(success_log, "a") as f:
        f.write(f"{filename}\n")

def unpack_upx(file_path):
    try:
        subprocess.run(["upx", "-d", file_path], check=True)
        log_success(file_path)
    except subprocess.CalledProcessError:
        try:
            subprocess.run(["upx", "-d", "-f", file_path], check=True)
            log_success(file_path)
        except subprocess.CalledProcessError:
            log_failure(file_path, "UPX unpacking failed, even with -f option")

def unpack_nspack(file_path):
    log_failure(file_path, "NsPacK unpacking not implemented (custom unpacker needed)")

def unpack_aspack(file_path):
    log_failure(file_path, "ASPack unpacking not implemented (custom unpacker needed)")

def unpack_dotnet_protector(file_path, protector_name):
    log_failure(file_path, f"{protector_name} unpacking not implemented (use deobfuscation tool)")

def process_file(file_path):
    filename = os.path.basename(file_path)
    if "upx" in filename:
        unpack_upx(file_path)
    elif "nspack" in filename:
        unpack_nspack(file_path)
    elif "aspack" in filename:
        unpack_aspack(file_path)
    elif any(protector in filename for protector in ["obfuscar", "netreactor", "skater", "vmprotect", "pespin"]):
        unpack_dotnet_protector(file_path, "Custom Protector")
    else:
        log_failure(file_path, "Unknown or unsupported packer/protector")

keywords = ["upx", "nspack", "aspack", "obfuscar", "netreactor", "skater", "vmprotect", "pespin"]

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".exe") and any(keyword in file for keyword in keywords):
            file_path = os.path.join(root, file)
            process_file(file_path)

print("Unpacking process completed. Check the log files for results.")
